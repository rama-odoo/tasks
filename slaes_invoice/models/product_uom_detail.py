from odoo import models, _, fields, api


class ProductUomDetail(models.Model):

    _name = 'product.uom.detail'

    product_id = fields.Many2one('product.template')
    uom_id = fields.Many2one('uom.uom')
    partner_id = fields.Many2one('res.partner')
    uom_category = fields.Many2one(related='product_id.uom_id.category_id')
    # available_uom_ids = fields.Many2many("uom.uom",compute="_compute_uom_ids")
    

    # def _compute_uom_ids(self):
    #     print("::::::::::::::::::\n\n\n\n", record.available_uom_ids)
    #     for record in self:
    #         record.available_uom_ids = record.uom_categ_id.uom_ids.ids
    #         print("::::::::::::::::::\n\n\n\n", record.available_uom_ids)