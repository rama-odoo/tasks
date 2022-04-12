{
    'name': 'Shop & Products',
    'summary': """
        This module is  create a field in shop.
    """,

    'description': """
       new hold field 
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['website_sale', 'sale_management', 'stock'],
    'data': [
        'views/web_inherit_template_website.xml',
        'views/web_inherit_template_website_contactus.xml'
    ],

    'installable': True,
    'application': True,
}
