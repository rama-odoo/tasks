# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'The Dream Factory Kenya Ltd',
    'version': '1.0',
    'author': 'Odoo India',
    'description': """
         Task ID - 3177441
         Customise the reports.
    """,
    'summary': 'this model is create a field report side in SalesOrders/Quotation, purchase order, bills, invoices, inventory transfers',
    'depends': ['account','sale_management','purchase','stock'],
    'data': [
        'views/sale_order_custom_report.xml',
        'views/purchase_order_custom_report.xml',
        'views/account_invoice_custom_report.xml',
        'views/inventory_transfers_custom_report.xml',

    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
