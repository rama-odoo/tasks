# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Order & customization',
    'version': '1.0',
    'author': 'Odoo India',
    'summary': 'this model',
    'depends': ['sale_management',
                'l10n_in',
                'purchase',
                'web_studio'],

    'data': [
        'data/sale_order_data.xml',
        'data/external_layout_boxed.xml',
        'data/purchase_order_form_data.xml',
        'data/account_move_form_data.xml',
        'data/automation_action_data.xml',

        'views/sale_order_inherit_view.xml',
        'views/purchase_order_form_views.xml',
        'views/account_move_form_views.xml',
        'views/sale_order_report_views.xml',
        'views/purchase_order_report_views.xml',
        'views/mail_template_emil_layouts.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
