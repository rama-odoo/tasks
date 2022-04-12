# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales Quotation Report ',
    'summary': """
        This module is create sale quotations report for sale.
    """,
    'description': """
        This module is create sale quotations report for sale.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',
    'depends': ["sale_management", "contacts", "product", "terms_condition"],

    'data': [
        'views/sale_views.xml',
        'report/report_template.xml',
        'report/sale_report_templates.xml',

    ],
    'installable': True,
    'application': True,
}
