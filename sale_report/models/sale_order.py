# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    enquiry = fields.Integer(string="Enquiry Referens No:")
    mark = fields.Char(string="Special Remark if any")


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    sr_no = fields.Integer(string="Sr.No")
    model_num = fields.Char()