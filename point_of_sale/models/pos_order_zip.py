from odoo import models,fields


class PosOrderZip(models.Model):
    _inherit = "pos.order"


    zip = fields.Char(related = "partner_id.zip")

   