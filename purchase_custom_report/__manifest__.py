# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'purchase_report_custom',
    'summary': """
        This module is show billing status in report for purchase order.
    """,
    'description': """
        This module is show billing status in report for purchase order.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ["purchase"],

    'data': [
        'report/purchase_order_form_report.xml'
    ],
    'installable': True,
    'application': True,
}
