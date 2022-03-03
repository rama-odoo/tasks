# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,fields,api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'
 
    @api.constrains('amount_untaxed')
    def _check_total_receivable_sale(self):
        credit_total = self.amount_total + self.partner_id.credit
        if credit_total > self.partner_id.credit_limit:
            raise UserError(("The Total receivable amount executed by credit limit."))
     