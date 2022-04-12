from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    customer_id = fields.Many2one('res.partner', string="Customer Data",
                                  config_parameter='costmer_recruitment.default_customer_id')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            "costmer_recruitment.customer_id", self.customer_id.id)
