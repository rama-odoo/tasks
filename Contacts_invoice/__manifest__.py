{
    'name': 'contacts & invoice',
    'summary': """
        This module is  create a boolean field in invoice wizard.
    """,

    'description': """
       
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['contacts','stock','account','sale_management'],
    'data': [
            "views/view_partner_form.xml",
    ],

    'installable': True,
    'application': True,
}