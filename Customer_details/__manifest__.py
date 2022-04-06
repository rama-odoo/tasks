{
    'name':'Customer & data', 
    'summary': """
        This module is  create for customer name and zip .
    """,

    'description': """
       zip show in form 
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['contacts','sale_management','purchase'],
  
    'data' :[
      'views/view_order_form_inherit.xml'
     
    ],
    'installable': True,
    'application': True,
}
