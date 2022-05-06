from odoo import models, fields, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    courses_id = fields.Many2one('slide.channel')
