# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'zero_stock_approval',
    'description':"""task id = 2763104""",
    'depends':["base","product","contacts","sale_management","sale","stock","deliver_shipping"],
    'data':[
        'views/sale_order_views.xml',
        'security/sale_order_security.xml'  

    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}
