# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Multiple_work_orders',
    'summary': """
     the Action menu, after selecting multiple work orders, to show additional action choice.
    """,
    'description': """
    Task id : 2763112
    the Action menu, after selecting multiple work orders, to show additional action choice.
    Start Timer,Stop Timer and Done
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ["mrp"],
    'data': [
        'views/production_order_action_start_views.xml',
    ],
    'installable': True,
    'application': True,
}
