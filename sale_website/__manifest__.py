# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'website & record',
    'summary': """
        This module is Currently reorder is not possible from the web [ for portal users] 
        Add button to reorder on the sales page as shown in the image below.
    """,
    'description': """
        Task id : "2763113"
       Add button to reorder on the sales page as shown in the image below and
       When the reorder button is clicked it will add all the items in the given sale order to the existing cart.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ["website_sale", "sale_management"],

    'data': [
        'views/web_inherit_template_website_layout.xml'

    ],
    'installable': True,
    'application': True,
}
