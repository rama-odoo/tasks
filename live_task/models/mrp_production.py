from odoo import fields, models, api


class MrpProduction(models.Model):

    _inherit = "mrp.production"

    product_ids = fields.Many2many('product.product', compute='_compute_components', string="components")

    @api.depends("move_raw_ids.product_id")
    def _compute_components(self):
        for record in self:
            record.product_ids = record.move_raw_ids.product_id.ids
