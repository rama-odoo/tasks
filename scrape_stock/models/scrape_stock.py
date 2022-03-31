# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _
from odoo.exceptions import UserError


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    
    def action_validate(self):
        stock = self.env['ir.config_parameter'].sudo().get_param('costmer_recruitment.is_validate')
        if not stock:
                raise UserError(_("Operation not supported"))

        return super(StockScrap,self).action_validate()
