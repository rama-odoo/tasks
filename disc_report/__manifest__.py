# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name':'Discount_report',
    'description':"""task id = 2763107 """,
    'depends':["base","sale","sale_management"],
    'data':[
        'views/sale_order_line_views.xml'
    ],

    'installable':True,
    'application':True,
    'license':'LGPL-3',
}
