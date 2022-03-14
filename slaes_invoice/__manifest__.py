# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale/Invoice UOM category.',
    'summary': """
        This module is add one or more products and uom for customers
         When product is select, uom  filtered to show only other uom possible in the uom category in field. 
        and When customer is selected,
        and lines are added the product display the uom from customer profile else the default odoo behaviour applies.""",
    'description': """
    Task id : 2763105
        product is display the uom from customer profile  else the default odoo behaviour applies.
     """,
    'depends': ["account", "product", "contacts", "sale_management", "sale", "stock", "deliver_shipping", "zero_stock_approval"],
    'data': [
        'views/res_partner_view.xml',
        'security/ir.model.access.csv',

    ],
    'installable': True,
    'application': True,
}
