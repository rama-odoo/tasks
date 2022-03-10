# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'multiple_work',
    'description': """task id = 2763112""",
    'depends':["base","mrp"],
    'data':[
        'views/production_order_action_start_views.xml',
    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}
