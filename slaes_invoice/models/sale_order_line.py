from odoo import models,api, fields
    
class SaleOrderLine(models.Model):
   
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def product_id_change(self):
        res = super().product_id_change()
        for data in self :
            if data.order_id.partner_id:
                if data.order_id.partner_id.product_uom_detail_ids:
                    uom_details_ids = data.order_id.partner_id.product_uom_detail_ids
                    for record in uom_details_ids:
                        if data.product_id == record.product_id:
                            data.product_uom = record.uom_id
                      
        return res


        