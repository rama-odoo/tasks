from odoo import models,api,fields

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.onchange('product_id')
    def _onchange_product_id(self):
       res = super()._onchange_product_id()
       for data in self :
            if data.move_id.partner_id:
                if data.move_id.partner_id.product_uom_detail_ids:
                    uom_details_ids = data.move_id.partner_id.product_uom_detail_ids
                    for record in uom_details_ids:
                        if data.product_id == record.product_id:
                            data.product_uom_id = record.uom_id

       return res
