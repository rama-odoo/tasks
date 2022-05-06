from odoo import models, _, fields

class StockMove(models.Model):
    _inherit = "stock.move"

   
    def _adjust_procure_method(self):
        for move in self:
            needed_qty = move.product_qty
            forecasted_qty = move.product_id.virtual_available
            if needed_qty > forecasted_qty:
                move.procure_method = 'make_to_order'
            else:
                move.procure_method = 'make_to_stock'
