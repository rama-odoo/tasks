{
    'name': 'Stock picking',
    'summary': """ this model is create a boolean field. it is checkout then show loc/name field in wizard.""",
    'description': """
        show a loc/name field in wizard.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['stock'],
    'data': [
        'views/stock_view_picking_type_form.xml',
        'views/view_stock_move_operations.xml',
        'views/view_production_lot_form.xml',
    ],

    'installable': True,
    'application': True,
}
