# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Manufacture order -Bijak',
    'category': 'Manufacturing/Manufacture order',
    'version': '15.2',
    'author': 'Odoo PS-IN',
    'summary': 'create a stamp report add field and images.',
    'description': """
this model is create a new action button and add a stamp barcode report,add Product name, qty, Mrp, Packed On, best before, packed by company name and add some logo in report.
    """,
    'depends': ['mrp'],
    'data': [
        'report/manufacture_report_action.xml',
        'report/manufacture_order_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
