{
    'name' : 'Slaes_invoice',
    'description': """task id = 2763105""",
    'depends':["base","account","product","contacts","sale_management","sale","stock","deliver_shipping","zero_stock_approval"],
    'data':[
        'views/res_partner_view.xml', 
        'security/ir.model.access.csv',
       
    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3',
}
