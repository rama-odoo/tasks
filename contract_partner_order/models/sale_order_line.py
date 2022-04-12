# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api, fields
from datetime import datetime


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    date_time = fields.Date(string="Date")

    @api.onchange('product_id')
    def product_id_change(self):
        res = super().product_id_change()
        for contract in self:
            contract.order_id.partner_id.contract_ids.filtered(
                lambda c: c.product_id == self.product_id and datetime.date.today() >= c.date_from and datetime.date.today() <= c.date_to)
