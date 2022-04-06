# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models, _, api


class SaleOrder(models.Model):

    _inherit = "sale.order"

    selected_order_id = fields.Many2one('sale.order', string="Sale Order")


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def _onchange_product_id(self):
       
        product_ids = self.order_id.selected_order_id.order_line.mapped("product_id").ids

        print("\n\n\n value?////////////////??",product_ids,self.order_id.selected_order_id.id)
        return {
            'domain': {
                'product_id': [
                    ('id', 'in', product_ids)
                ]}
        }
