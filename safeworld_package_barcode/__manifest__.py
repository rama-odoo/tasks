# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name':'Safeworld -Reporting package barcode',
    'version':'15.0',
    'author':'Odoo PS-IN',
    'summary':'this model is replace report in report_package_barcode report in stock quant package and add field customer name,date sale order number client po number.',
    'depends':  [
        'stock',
        'sale_management'
    ],
    'data': [
        'report/customer_barcode_package_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}