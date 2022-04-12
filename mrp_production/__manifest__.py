# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Mrp_production',
    'summary': """
        This module is show product_id in purchase order.
    """,
    'description': """
         This module is show product_id in purchase order.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ["mrp"],
    'data': [
        'views/mrp_production_views.xml'
    ],
    'installable': True,
    'application': True,
}
