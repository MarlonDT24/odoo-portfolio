# -*- coding: utf-8 -*-
# from odoo import http


# class AccountInvoiceCustomizer(http.Controller):
#     @http.route('/account_invoice_customizer/account_invoice_customizer', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_invoice_customizer/account_invoice_customizer/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_invoice_customizer.listing', {
#             'root': '/account_invoice_customizer/account_invoice_customizer',
#             'objects': http.request.env['account_invoice_customizer.account_invoice_customizer'].search([]),
#         })

#     @http.route('/account_invoice_customizer/account_invoice_customizer/objects/<model("account_invoice_customizer.account_invoice_customizer"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_invoice_customizer.object', {
#             'object': obj
#         })

