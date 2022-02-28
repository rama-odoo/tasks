from odoo import models, _, fields, api


class ResPartner(models.Model):
    
    _inherit = 'res.partner'

    days_deliver = fields.Integer(string="Days to Deliver")
   