# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Discount_report',
    'summary': """
       Some customers of Colona have long-term discounts but sometimes, they also benefit from temporary discounts in addition. The two discounts must be visible on the sale order to communicate clearly with the client.
    """,
    'description': """
    Task id : "2763108"
    Some customers of Colona have long-term discounts but sometimes, they also benefit from temporary discounts in addition. The two discounts must be visible on the sale order to communicate clearly with the client.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ["sale", "sale_management", 'account'],
    'data': [
        'views/sale_order_line_views.xml',
        'views/account_move_line_views.xml',
        'report/sale_report_templates.xml',
        'report/report_invoice.xml'
    ],

    'installable': True,
    'application': True,
}
