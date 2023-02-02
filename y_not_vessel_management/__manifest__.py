# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Y Not Vessel Management',
    'version': '1.0',
    'author': 'Odoo India',
    'description': """
        -Task ID - 3122387
        Create a new menu and pivot view for "Delivery by vessel" and remove readonly field on 'Transfer' and write a python code to fetch vessel from sale order when picking are created and transfer has no backorder.
    """,
    'category': 'Development',
    'summary': 'Y Not Vessel Management',
    'depends': ['sale_management', 'account', 'stock'],
    'data': [
        'views/custom_vessel_stock_picking.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
