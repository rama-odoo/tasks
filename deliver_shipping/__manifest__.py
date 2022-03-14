# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Delivere & shipping', 
    'summary': """
        The goal of this specification is to have a field where we can put an appointment date and to calculate the delivery date in the function of this appointment if there is one.
    """,
    'description': """
    Task id :2763103
        The goal of this specification is to have a field where we can put an appointment date and to calculate the delivery date in the function of this appointment if there is one.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends':["product","contacts","sale_management","sale","stock"],
    'data':[
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable':True,
    'application':True,
}
