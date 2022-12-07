# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Invoice Report',
    'version': '1.1',
    'category': 'Accounting/Move',
    'description': """
- Tax invoice report and commrcial invoice report in invoice.
ID: 2961478
    """,
    'author': 'Odoo PS-IN',
    'summary': 'Tax Invoice report and commrcial invoice report.',
    'depends': [
        'account',
        'sale_management',
        'stock',
        'l10n_in',
        # 'l10n_in_einvoice',
    ],
    'data': [
        'data/paperformat.xml',
        'views/account_move_views.xml',
        'views/res_company_view.xml',
        'views/account_reports.xml',
        'views/report_tax_invoice.xml',
        'views/report_commercial_invoice.xml',
        'views/res_partner_bank_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}