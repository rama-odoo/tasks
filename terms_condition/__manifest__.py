 # -*- encoding: utf-8 -*-
 # Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' :'Terms & Conditions',
    'summary': """
        This module is create terms for delivery and general terms report for sale.""",
    'description': """
        This module is create terms report for sale.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ['base'],

    'data': [
        'views/sale_order_delivery_terms_views.xml',
        'views/sale_order_terms_views_menu.xml',
        'views/terms_template.xml',
        'views/sale_order_general_terms_views.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
}


