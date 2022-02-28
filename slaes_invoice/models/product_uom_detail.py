from odoo import models, _, fields, api


class ProductUomDetail(models.Model):

    _name = 'product.uom.detail'

    product_id = fields.Many2one('product.product')
    uom_id = fields.Many2one('uom.uom')
    partner_id = fields.Many2one('res.partner')
    uom_category = fields.Many2one(related='product_id.uom_id.category_id')
   