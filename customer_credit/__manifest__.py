# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'customer & credit',
    'summary': """
        Customer “Credit Limit” and “total Receivable” Fields in Customer Profile.
        If the total receivable amount exceeds the credit limit,then the system should show a warning about that and restrict processing sales orders and invoices.
    """,
    'description': """
    Task id : 2763107
        Customer “Credit Limit” and “total Receivable” Fields in Customer Profile. 
         If the total receivable amount exceeds the credit limit, then the system should show a warning about that and restrict processing sales orders and invoices.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ['contacts', "sale_management", "sale", "account"],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}
