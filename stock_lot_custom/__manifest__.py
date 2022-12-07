# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock Lot Custom',
    'version': '15.2',
    'author': 'Odoo India',
    'summary': 'this model is add the fields, which is stored on the serial number of FG (Serial number of components)',
    'description': """
    The First two columns Device(IMEI Number) and Sim-1(Mobile Number) will be Show by default type column and the third one Sim-2(Mobile Number) will be hide by default type column.
    """,
    'depends': [
        'stock'
    ],
    'data': [
        'data/stock_quant_data.xml',
        'views/stock_quant_tree_view.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
