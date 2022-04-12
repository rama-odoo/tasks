# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api
from num2words import num2words


class SaleOrder(models.Model):
    _inherit = "sale.order"

    enquiry = fields.Integer(string="Enquiry Referens No:")
    mark = fields.Char(string="Special Remark if any")

    text_amount = fields.Char(string="Total In Words",
                              compute="amount_to_words")
    term_id = fields.Many2one(
        "sale.order.delivery.terms", string="Delivery Trems:")
    general_id = fields.Many2one(
        "sale.order.general.terms", string="General Trems:")

    @api.depends('amount_total')
    def amount_to_words(self):

        self.text_amount = num2words(self.amount_total)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    sr_no = fields.Integer(string="Sr.No")
    model_num = fields.Char()
