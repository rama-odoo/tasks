# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'PRO-FORMA Invoice & Sale Order /rayzon',
    'category': 'Accounting/Move',
    'description': "add images and terms and conditions, and attach sale order report in this report.",
    'summary':'this model is add proforma format in sale order(pro-forma invoice) report.',
    'depends': [
        'account',
        'sale_management',
        ],
    'data': [
        'views/proforma_format_sale_order_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}