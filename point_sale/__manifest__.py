{
    'name':'Point & Sales', 
    'summary': """
        This module is  create for user side.
    """,

    'description': """
       validate field 
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['point_of_sale','contacts'],

    'assets': {
    'point_of_sale.assets': [
        '/point_sale/static/src/js/PayCustomer.js',
    ],
    },
    'installable': True,
    'application': True,
}
