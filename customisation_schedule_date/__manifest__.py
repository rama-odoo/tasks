# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale order & customisation schedule',
    'version': '1.0',
    'author': 'Odoo India',
    'summary': 'In this task be create a compute method in custome side.',
    'depends': ['sale_management'],
    'description': """
         Task ID - 3014922 """,
    'data': [
        'data/sale_order_automation_action.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
