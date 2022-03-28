{
    'name':'Customer & Recruitment', 
    'summary': """
        This module is  create a recuritment for user date is deleted in contact record  .
    """,

    'description': """
        delete a recruitment 
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['website','hr_recruitment','contacts','sale_management'],
  
    'data' :[
        'views/res_config_settings_view_form.xml',
        'views/view_company_inherit_form.xml'
    ],
    'installable': True,
    'application': True,
}
