{
    'name' : 'Delivere_shipping',  #TaskID-123
    'depends':["base","product","contacts","sale_management","sale","stock"],
    'description': """task id :2763103""",
    'data':[
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}
