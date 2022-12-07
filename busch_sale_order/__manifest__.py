# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'sale & order',
    'summary': 'Two Column is required in Sales Order Line OTD (On Time Delivery),Promise VS Request ,Delay Days',
    'depends': ['sale_management','stock'],
    'data': [
        'data/model_x_order_lines.xml',
        'data/x_order_lines_fields.xml',
        # 'data/action_automation_sale_order.xml',
        'data/field_sale_order_line.xml',
        'view/sale_order_line_views.xml',
        'view/sale_order_line_tree_views.xml',
        'view/sale_order_tree_view_report.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
