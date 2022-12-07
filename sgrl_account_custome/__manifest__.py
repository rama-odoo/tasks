# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name':'Invoice-Report /sgrl',
    'category': 'Accounting/Move',
    'description': "tax invoice report and commrcial invoice report in invoice",
    'summary':'this model is create to Tax Invoice report and commrcial invoice report.',
    'depends': ['account','sale_management','stock','l10n_in'],
    'data': [
        # 'views/account_move_views.xml',
        # 'views/automated_action.xml',
        # 'report/account_invoice_report.xml',
        # 'report/tax_invoice_report.xml',
        # 'report/commercial_invoice_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}