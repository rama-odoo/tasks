# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'test',
    'version': '1.0',
    'author': 'Odoo India',
    'summary': 'this model is create a field and compute filed When 3 step route enabled for receiving material, Material first move in input location from vendor location.',
    'depends': ['stock','purchase'],
    'data': [
        'data/stock_picking_data.xml',
        'views/stock_picking_form_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}