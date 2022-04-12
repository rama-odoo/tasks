{
    'name': 'Scrape_stock',
    'summary': """
        This module is  create field for validate.
    """,

    'description': """
       validate field 
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['stock', 'account', 'stock_account'],

    'data': [
        'views/res_config_settings_view_form.xml'
    ],
    'installable': True,
    'application': True,
}
