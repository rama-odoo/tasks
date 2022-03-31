# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
# from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_validate = fields.Boolean(string="scrape", config_parameter='costmer_recruitment.is_validate')

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'scrape_stock.is_validate', self.is_validate)

        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update(
            is_validate=ICPSudo.get_param(
                'scrape_stock.is_validate'),
        )
        print("\n\n valu is print::::::::", res)
        return res
