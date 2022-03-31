# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, tools


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.ensure_one()
        settings_partner = int(self.env['ir.config_parameter'].sudo(
        ).get_param('costmer_recruitment.customer_id')) or False
        return {'domain': {'partner_id': [('id', '!=', settings_partner)]}}
