{
    'name' : 'zero_stock_approval',
    'depends':["base","product","contacts","sale_management","sale","stock","deliver_shipping"],
    'data':[
        'views/sale_order_views.xml',
        'security/sale_order_security.xml'  

    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}