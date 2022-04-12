{
    'name':'Point & Sales', 
    'summary': """
        This module is  create for user side.
    """,

    'description': """
      customer is add then validate field and customer is not add then popup add customer.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['point_of_sale','contacts'],
    'data' :[
        'views/view_pos_inherit_form.xml'
        ],
    'assets': {
    'point_of_sale.assets': [
        '/point_sale/static/src/js/PayCustomer.js',
    ],
    },
    'installable': True,
    'application': True,
}
