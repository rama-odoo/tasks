# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,api,fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    date_time = fields.Date(string="Date")


    @api.onchange('product_id')
    def product_id_change(self):
        res = super().product_id_change()
        for record in self :
                if record.order_id.partner_id.contract_ids:
                    record.price_unit = record.date_time
                    print("\n\n\n value is print ",record)
                    record.product_id == record.price_unit
                    print("\n\n\n value is print ****************",res)
        return res
