from odoo import models,fields,api



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    
    customer_id = fields.Many2one('res.partner',string="Customer Data",related="company_id.partner_id", readonly=0)
   