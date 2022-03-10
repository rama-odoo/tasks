# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models,api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    discount_2 = fields.Float(string="2nd Disc.%")


    @api.depends('price_subtotal','discount_2','price_unit','product_uom_qty','discount','tax_id')
    def _compute_amount(self):
        res = super()._compute_amount()
        for line in self:
            line.price_subtotal = line.price_subtotal - ((line.price_subtotal * line.discount_2) / 100.0)
        return res

    def _prepare_invoice_line(self, **optional_values):

        values = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        values['discount_2'] = self.discount_2
        # print("\nvalue******************",values)

        return values