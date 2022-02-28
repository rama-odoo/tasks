from odoo import models, _,fields,api


class ResPartner(models.Model):
   
    _inherit = 'res.partner'

    product_uom_detail_ids = fields.One2many(comodel_name='product.uom.detail',
                                             inverse_name='partner_id',
                                             string='Product Uom',
                                             required=False)

