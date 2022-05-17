{
    'name': 'Prorated Deduction of Down Payments',
    'summary': """ this model is create invoice in so form and connect a deduction rate in wizard and connect down payment.""",
    'description': """
        connect a deduction rate in down payment.
    """,
    'author': 'Odoo Ps',
    'version': '1.0.0',

    'depends': ['sale_management','account','stock'],
    'data': [
        'wizard/sale_view_sale_advance_payment_inv.xml',
        'views/sale_order_view_form.xml',
    ],

    'installable': True,
    'application': True,
}
