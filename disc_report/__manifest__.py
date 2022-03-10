# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name':'Discount_report',
    'description':"""task id = 2763107 """,
    'depends':["base","sale","sale_management", 'account'],
    'data':[
        'views/sale_order_line_views.xml',
        'views/account_move_line_views.xml',
        'report/sale_report_templates.xml',
        'report/report_invoice.xml'
    ],

    'installable':True,
    'application':True,
    'license':'LGPL-3',
}
