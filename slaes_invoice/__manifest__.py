{
    'name' : 'Slaes_invoice',
    'depends':["base","product","contacts","sale_management","sale","stock","deliver_shipping","zero_stock_approval"],
    'data':[
        'views/res_partner_view.xml',
        # 'views/sale_order_views.xml', 
        'security/ir.model.access.csv',
       
    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}