# -*- coding: utf-8 -*-
{
    'name': "Account Invoice Customizer",
    'version': '17.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': "Personalización de facturas de cliente para Odoo 17",
    'description': """
        Módulo que extiende las facturas de cliente añadiendo:
        - Campos personalizados (número de expediente, notas internas)
        - Validaciones al confirmar la factura
        - Lógica automática en la confirmación
        - Reporte PDF personalizado
    """,

    'author': "Marlon Torres",
    'website': "https://github.com/MarlonDT24",
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'report/invoice_report.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

