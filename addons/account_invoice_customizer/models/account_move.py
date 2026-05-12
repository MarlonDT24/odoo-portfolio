# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    # ── Campos personalizados ────────────────────────────────────────────

    expedition_number = fields.Char(
        string='Número de expediente',
        help='Número de expediente interno del cliente',
        copy=False,
    )

    internal_notes = fields.Text(
        string='Notas internas',
        help='Notas visibles solo para el equipo interno, no en el PDF',
    )

    custom_validated = fields.Boolean(
        string='Validado internamente',
        default=False,
        copy=False,
        help='Indica que la factura ha pasado la validación interna',
    )

    # ── Campos computados ────────────────────────────────────────────────

    days_overdue = fields.Integer(
        string='Días de retraso',
        compute='_compute_days_overdue',
        help='Días que lleva la factura sin pagar desde su vencimiento',
    )

    total_with_label = fields.Char(
        string='Total formateado',
        compute='_compute_total_with_label',
        help='Total de la factura formateado con texto',
    )

    # ── Lógica de campos computados ─────────────────────────────────────

    @api.depends('invoice_date_due', 'payment_state')
    def _compute_days_overdue(self):
        """
        Calcula los días de retraso en el pago.
        Solo aplica a facturas confirmadas y no pagadas.
        """
        today = fields.Date.today()
        for move in self:
            if (
                move.move_type == 'out_invoice'
                and move.state == 'posted'
                and move.payment_state != 'paid'
                and move.invoice_date_due
                and move.invoice_date_due < today
            ):
                delta = today - move.invoice_date_due
                move.days_overdue = delta.days
            else:
                move.days_overdue = 0

    @api.depends('amount_total', 'currency_id')
    def _compute_total_with_label(self):
        """
        Formatea el total con el símbolo de moneda.
        Útil para mostrar en reportes y vistas.
        """
        for move in self:
            if move.amount_total and move.currency_id:
                move.total_with_label = (
                    f"{move.amount_total:.2f} {move.currency_id.symbol}"
                )
            else:
                move.total_with_label = '0.00 €'

    # ── Validaciones ─────────────────────────────────────────────────────

    @api.constrains('expedition_number')
    def _check_expedition_number(self):
        """
        Valida que el número de expediente no esté duplicado
        en facturas del mismo cliente.
        """
        for move in self:
            if not move.expedition_number:
                continue
            duplicate = self.search([
                ('expedition_number', '=', move.expedition_number),
                ('partner_id', '=', move.partner_id.id),
                ('id', '!=', move.id),
                ('move_type', '=', 'out_invoice'),
            ])
            if duplicate:
                raise ValidationError(
                    f'El número de expediente {move.expedition_number} '
                    f'ya existe para el cliente {move.partner_id.name}.'
                )

    # ── Lógica en confirmación ───────────────────────────────────────────

    def action_post(self):
        """
        Herencia del método de confirmación de factura.
        Se ejecuta cuando el usuario pulsa 'Confirmar'.
        Añadimos validaciones y lógica automática antes
        de que Odoo ejecute su lógica estándar.
        """
        for move in self:
            if move.move_type != 'out_invoice':
                continue

            # Validación: facturas de más de 1000€ requieren expediente
            if (
                move.amount_total > 1000
                 
            ):
                raise ValidationError( 
                    'Las facturas superiores a 1.000€ requieren '
                    'un número de expediente antes de confirmar.'
                )

            # Log automático para auditoría
            _logger.info(
                'Confirmando factura %s para cliente %s por importe %s€',
                move.name,
                move.partner_id.name,
                move.amount_total,
            )

        # Llamamos al método original de Odoo — SIEMPRE al final
        return super().action_post()