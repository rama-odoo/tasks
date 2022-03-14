# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Stock/Sale approval',
    'summary': """
       This module is approve boolean field. Its name is Zero Stock Approval.
        If true then sales user can confirm the sale order and read only user. 
    """,
    'description':
    """ Task id: 2763104
        If true then sales user can confirm the sale order and read only user""",
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ["product", "contacts", "deliver_shipping"],
    'data': [
        'views/sale_order_views.xml',
        'security/sale_order_security.xml'

    ],
    'installable': True,
    'application': True,
}
