# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    deduction_rate = fields.Float('Deduction Rate',invisible=True)

    def _prepare_so_line(self, order, analytic_tag_ids, tax_ids, amount):
        res = super()._prepare_so_line(order, analytic_tag_ids, tax_ids, amount)
        res.update({"deduction_rate": self.amount, "is_downpayment": True})
        return res


