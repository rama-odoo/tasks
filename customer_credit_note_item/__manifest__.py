# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Customer Credit Note Item/Price Calculation',
    'version': '1.0',
    'author': 'Odoo India',
    'category': 'Accounting/Move',
    'description': """
         Task ID - 3075941
        Open any customer invoice and click add credit note button > Select partial refund and click reverse button to generate a credit note, and Create a new column in credit notes where the Credit Discount can be manually entered by user. Percentage of credit will be entered manually so that unit price will be updated according to percentage.,and Item price should show as per the discount value selected from additional info tab.
    """,
    'summary': '',
    'depends': ['account_accountant'],
    'data': [
        'views/account_move_inherit_view_form.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
