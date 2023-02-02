# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'PRO-FORMA Invoice & Sale Order /rayzon',
    'category': 'Accounting/Move',
    'description':
        """
        Task ID-3083616
        add images and terms and conditions, and attach sale order report in this report.
        """,
    'summary':'this model is add proforma format in sale order(pro-forma invoice) report.',
    'depends': [
        'account',
        'sale_management',
        ],
    'data': [
        'data/model_sale_terms_condition.xml',
        'data/sale_order_data.xml',
        'views/sale_order_form_view.xml',
        'views/menu_sale_order.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}