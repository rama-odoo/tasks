# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    discount_2 = fields.Float(string="2nd Disc.%")


    @api.depends('price_subtotal', 'discount_2', 'price_unit')
    def _compute_amount(self):
        res = super()._compute_amount()
        for line in self:
            line.price_subtotal = line.price_subtotal - ((line.price_subtotal * line.discount_2) / 100.0)
        return res
