{
    'name': 'Manufacturing Order',
    'summary': """ this model is create a data in manufactring side""",
    'description': """
        create data in manufactring side
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['mrp','sale_management','stock'],
    'data': [
        'views/mrp_production_tree_view.xml',
    ],


    'installable': True,
    'application': True,
}
