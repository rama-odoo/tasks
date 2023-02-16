# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Yoosha Sale Custom',
    'summary': 'Yoosha Sale Custom',
    "version": "16.0.1.0",
    'website': 'https://www.odoo.com',
    'author': 'Odoo PS',
    'description': """
        - TASK ID - 3175106
        - Create new custom report in sale order.
    """,
    'category': 'Custom Development',
    'depends': [
        'sale_management',
    ],
    'data': [
        'data/fields_sale_order.xml',
        'views/custom_sale_order_line_view.xml',
        'report/report_action.xml',
        'report/external_layout_custom.xml',
        'report/custom_sale_order_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
