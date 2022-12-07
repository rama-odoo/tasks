# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    credit_dicount = fields.Float(string="Credit Dic%", readonly=False)


    @api.onchange('credit_dicount')
    def onchange_price_unit(self):
        for rec in self:
            if rec.move_id.move_type in ('out_refund'):
                price_unit = rec.price_unit * (1 - rec.credit_dicount / 100)
                rec['price_unit'] = price_unit
