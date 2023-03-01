# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class sale_order(models.Model):
    _inherit='sale.order'

    customer_field=fields.Many2one('res.company',string='Customer Field')

class stock_picking(models.Model):
    _inherit='stock.picking'
    customer_field=fields.Many2one('res.company',string='Customer Field',compute="_vessel_management",store=True)

    @api.depends('backorder_id')
    def _vessel_management(self):
        for pick in self:
            if not pick.backorder_id:
                 pick.customer_field = pick.sale_id.customer_field
            else:
                pick.customer_field = False

