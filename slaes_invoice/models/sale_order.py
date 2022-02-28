from odoo import models,api, fields


class SaleOrder(models.Model):
   
    _inherit ='sale.order.line'

    @api.onchange('product_id')
    def product_id_change(self):
        pass
        