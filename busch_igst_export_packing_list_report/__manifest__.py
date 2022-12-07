# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Busch IGST Export and Packing List Reports',
    'version': '1.0',
    'author': 'Odoo PS',
    'category': '',
    'summary': 'Busch Tax,Commercial and Packing List Reports',
    'description': """
         Task ID - 2655322,2755566
        - created tax invoice which display all amount in INR.
        - created commercial invoice, here taxes are not shown.
        - created packing list, which categorize product according
        the Source Package.
        - Added Boolean field which allows to display 
        rate and qty of service type product.
        - Added Many2many field with compute method, in order to 
        get the only list of transfer will come which is related 
        to only that sales order.
        - Create a new report packing label, Added ship to and
        from address,sale order no, customer no, current date
        at the time of taking print and for every destination package
        it will appear on new page
    """,
    'depends': [
        'account_accountant',
        'sale_management',
        'stock',
        'web',
        'l10n_in',
    ],
    'data': [
        "data/fields.xml",
        "report/packing_list.xml",
        "report/shipping_label.xml",
        "report/custom_invoice_report.xml",
        "report/external_layout_custom.xml",
        "report/report.xml",
        "views/product_views.xml",
        "views/view_move_form.xml",
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
