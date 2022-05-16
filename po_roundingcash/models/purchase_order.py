import json
import math
from odoo import api,models,fields
from odoo.exceptions import UserError
from datetime import datetime

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    round_of_cash = fields.Many2one('account.cash.rounding',string='Cash Rounding Method')

    @api.onchange('order_line','round_of_cash')
    def _onchange_amount_all(self):
        for order in self:
            for virtualid in order.order_line:
                if virtualid.product_id.id == 36:
                    order.order_line -= virtualid
            if not order.order_line.taxes_id and order.order_line.product_id:
                if order.round_of_cash.strategy == "biggest_tax":
                    if order.round_of_cash.rounding_method =="UP":
                        if order.round_of_cash.rounding >= 1:
                            order.amount_total = math.ceil(order.amount_total)
                        else:
                            check = (order.amount_total * 100)%10
                            if check >= 5:
                                order.amount_total = round(order.amount_total, 1)
                            else:
                                order.amount_total = round(order.amount_total, 1) + 0.1
                    elif order.round_of_cash.rounding_method =="DOWN":
                        if order.round_of_cash.rounding >= 1:
                            order.amount_total = math.floor(order.amount_total)
                        else:
                            check = (order.amount_total * 100)%10
                            if check >= 5:
                                order.amount_total = round(order.amount_total, 1) - 0.1
                            else:
                                order.amount_total = round(order.amount_total, 1)
                    elif order.round_of_cash.rounding_method =="HALF-UP":
                        temp = math.floor(order.amount_total) + 0.50
                        if order.amount_total >= temp:
                            if order.round_of_cash.rounding >= 1:
                                order.amount_total = math.ceil(order.amount_total)
                            else:
                                order.amount_total = round(order.amount_total, 1)
                        elif order.amount_total < temp:
                            if order.round_of_cash.rounding >= 1:
                                order.amount_total = math.floor(order.amount_total)
                            else:
                                order.amount_total = round(order.amount_total, 1)
                elif order.round_of_cash.strategy == "add_invoice_line":
                    # extra_line = order.order_line(lambda line: line.product_id.id == 28)
                    # self.order_line -= extra_line
                    if order.round_of_cash.rounding_method =="UP":
                        temp1 = 0
                        if order.round_of_cash.rounding >= 1:
                            temp1 = math.ceil(order.amount_total) - order.amount_total
                        elif order.round_of_cash.rounding >= 0.1 and order.round_of_cash.rounding < 1 and order.price_unit > math.floor(order.price_unit):
                            temp1 = math.ceil(order.amount_total) - order.amount_total
                            check1 = (order.amount_total * 100)%10
                            check2 = (order.amount_total * 100)%100
                            temp1 += check2*(0.01) - check1*(0.1) + 0.1
                            # check = (order.amount_total * 100)%10
                            # if check >= 5:
                                # temp1 = round(order.amount_total, 1) - order.amount_total
                            # else:
                                # temp1 = round(order.amount_total, 1) - order.amount_total + 0.1
                            # if temp1 < 0:
                                # temp1 = temp1*(-1)
                        po_line_vals ={
                            'product_id': 36,
                            'order_id': order._origin.id,
                            'name': self.round_of_cash.name,
                            'product_qty': 1,
                            'price_unit': temp1,
                            'price_subtotal': temp1,
                            'display_type': False,
                            'product_uom': 1,
                            'date_planned': datetime.now(),
                        }
                        order.order_line = [(0,0,po_line_vals)]
                    elif order.round_of_cash.rounding_method =="DOWN":
                        temp1 = 0
                        if order.round_of_cash.rounding >= 1:
                            temp1 = math.floor(order.amount_total) - order.amount_total
                        elif order.round_of_cash.rounding >= 0.1 and order.round_of_cash.rounding < 1 and order.price_unit > math.floor(order.price_unit):
                            temp1 = math.ceil(order.amount_total) - order.amount_total
                            check1 = (order.amount_total * 100)%10
                            check2 = (order.amount_total * 100)%100
                            temp1 += check2*(0.01) - check1*(0.1) - 0.1
                            # check = (order.amount_total * 100)%10
                            # if check >= 5:
                                # temp1 = round(order.amount_total, 1) - order.amount_total - 0.1
                            # else:
                                # temp1 = order.amount_total - round(order.amount_total, 1)
                            # if temp1 > 0:
                                # temp1 = temp1*(-1)
                        po_line_vals ={
                            'product_id': 36,
                            'order_id': order._origin.id,
                            'name': self.round_of_cash.name,
                            'product_qty': 1,
                            'price_unit': temp1,
                            'price_subtotal': temp1,
                            'display_type': False,
                            'product_uom': 1,
                            'date_planned': datetime.now(),
                        }
                        order.order_line = [(0,0,po_line_vals)]
                    elif order.round_of_cash.rounding_method =="HALF-UP":
                        temp = math.floor(order.amount_total) + 0.50
                        if order.amount_total >= temp:
                            temp1 = 0
                            if order.round_of_cash.rounding >= 1:
                                temp1 = math.ceil(order.amount_total) - order.amount_total
                            elif order.round_of_cash.rounding >= 0.1 and order.round_of_cash.rounding < 1 and order.price_unit > math.floor(order.price_unit):
                                temp1 = math.ceil(order.amount_total) - order.amount_total
                                check1 = (order.amount_total * 100)%10
                                check2 = (order.amount_total * 100)%100
                                temp1 += check2*(0.01) - check1*(0.1) + 0.1
                            po_line_vals ={
                                'product_id': 36,
                                'order_id': order._origin.id,
                                'name': self.round_of_cash.name,
                                'product_qty': 1,
                                'price_unit': temp1,
                                'price_subtotal': temp1,
                                'display_type': False,
                                'product_uom': 1,
                                'date_planned': datetime.now(),
                            }
                            order.order_line = [(0,0,po_line_vals)]
                        elif order.amount_total < temp:
                            temp1 = 0
                            if order.round_of_cash.rounding >= 1:
                                temp1 = math.floor(order.amount_total) - order.amount_total
                            elif order.round_of_cash.rounding >= 0.1 and order.round_of_cash.rounding < 1 and order.price_unit > math.floor(order.price_unit):
                                temp1 = math.ceil(order.amount_total) - order.amount_total
                                check1 = (order.amount_total * 100)%10
                                check2 = (order.amount_total * 100)%100
                                temp1 += check2*(0.01) - check1*(0.1) - 0.1
                            po_line_vals ={
                                'product_id': 36,
                                'order_id': order._origin.id,
                                'name': self.round_of_cash.name,
                                'product_qty': 1,
                                'price_unit': temp1,
                                'price_subtotal': temp1,
                                'display_type': False,
                                'product_uom': 1,
                                'date_planned': datetime.now(),
                            }
                            order.order_line = [(0,0,po_line_vals)]
            elif order.order_line.taxes_id and order.order_line.product_id:
                if order.round_of_cash.strategy == "biggest_tax":
                    if order.round_of_cash.rounding_method =="UP": 
                        if order.round_of_cash.rounding >= 1:
                            temp2 = math.ceil(order.amount_total) - order.amount_total
                            order.amount_tax += temp2
                        else:
                            check = (order.amount_total * 100)%10
                            if check >= 5:
                                diff = round(order.amount_total, 1) - order.amount_total
                                order.amount_tax += diff
                            else:
                                diff = round(order.amount_total, 1) - order.amount_total + 0.1
                                order.amount_tax += diff
                    elif order.round_of_cash.rounding_method =="DOWN":
                        if order.round_of_cash.rounding >= 1:
                            temp2 = math.floor(order.amount_total) - order.amount_total
                            order.amount_tax += temp2
                        else:
                            check = (order.amount_total * 100)%10
                            if check >= 5:
                                diff = round(order.amount_total, 1) - order.amount_total - 0.1
                                order.amount_tax += diff
                            else:
                                diff = round(order.amount_total, 1) - order.amount_total
                                order.amount_tax += diff
                    elif order.round_of_cash.rounding_method =="HALF-UP":
                        temp = math.floor(order.amount_total) + 0.50
                        if order.amount_total >= temp:
                            temp2 = math.ceil(order.amount_total) - order.amount_total
                            order.amount_tax += temp2
                        elif order.amount_total < temp:
                            temp2 = math.floor(order.amount_total) - order.amount_total
                            order.amount_tax += temp2
                elif order.round_of_cash.strategy == "add_invoice_line":
                    if order.round_of_cash.rounding_method =="UP":
                        temp1 = 0
                        if order.round_of_cash.rounding >= 1:
                            temp1 = math.ceil(order.amount_total) - order.amount_total
                        elif order.round_of_cash.rounding >= 0.1 and order.round_of_cash.rounding < 1 and order.price_unit > math.floor(order.price_unit):
                            temp1 = math.ceil(order.amount_total) - order.amount_total
                            check1 = (order.amount_total * 100)%10
                            check2 = (order.amount_total * 100)%100
                            temp1 += check2*(0.01) - check1*(0.1) + 0.1
                            # if check >= 5:
                                # temp1 = round(order.amount_total, 1) - order.amount_total - 0.1
                            # else:
                                # temp1 = order.amount_total - round(order.amount_total, 1) + 0.1
                            # if temp1 < 0:
                                # temp1 = temp1*(-1)
                        po_line_vals ={
                            'product_id': 36,
                            'order_id': order._origin.id,
                            'name': self.round_of_cash.name,
                            'product_qty': 1,
                            'price_unit': temp1,
                            'price_subtotal': temp1,
                            'display_type': False,
                            'product_uom': 1,
                            'date_planned': datetime.now(),
                        }
                        order.order_line = [(0,0,po_line_vals)]
                        # self.env['purchase.order.line'].create(po_line_vals)
                    elif order.round_of_cash.rounding_method =="DOWN":
                        temp1 = 0
                        if order.round_of_cash.rounding >= 1:
                            temp1 = math.floor(order.amount_total) - order.amount_total
                        elif order.round_of_cash.rounding >= 0.1 and order.round_of_cash.rounding < 1 and order.price_unit > math.floor(order.price_unit):
                            temp1 = math.ceil(order.amount_total) - order.amount_total
                            check1 = (order.amount_total * 100)%10
                            check2 = (order.amount_total * 100)%100
                            temp1 += check2*(0.01) - check1*(0.1) - 0.1
                        po_line_vals ={
                            'product_id': 36,
                            'order_id': order._origin.id,
                            'name': self.round_of_cash.name,
                            'product_qty': 1,
                            'price_unit': temp1,
                            'price_subtotal': temp1,
                            'display_type': False,
                            'product_uom': 1,
                            'date_planned': datetime.now(),
                        }
                        order.order_line = [(0,0,po_line_vals)]
                    elif order.round_of_cash.rounding_method =="HALF-UP":
                        temp = math.floor(order.amount_total) + 0.50
                        if order.amount_total >= temp:
                            temp1 = 0
                            if order.round_of_cash.rounding >= 1:
                                temp1 = math.ceil(order.amount_total) - order.amount_total
                            elif order.round_of_cash.rounding >= 0.1 and order.round_of_cash.rounding < 1 and order.price_unit > math.floor(order.price_unit):
                                temp1 = math.ceil(order.amount_total) - order.amount_total
                                check1 = (order.amount_total * 100)%10
                                check2 = (order.amount_total * 100)%100
                                temp1 += check2*(0.01) - check1*(0.1) + 0.1
                            po_line_vals ={
                                'product_id': 36,
                                'order_id': order._origin.id,
                                'name': self.round_of_cash.name,
                                'product_qty': 1,
                                'price_unit': temp1,
                                'price_subtotal': temp1,
                                'display_type': False,
                                'product_uom': 1,
                                'date_planned': datetime.now(),
                            }
                            order.order_line = [(0,0,po_line_vals)]
                        elif order.amount_total < temp:
                            temp1 = 0
                            if order.round_of_cash.rounding >= 1:
                                temp1 = math.floor(order.amount_total) - order.amount_total
                            elif order.round_of_cash.rounding >= 0.1 and order.round_of_cash.rounding < 1 and order.price_unit > math.floor(order.price_unit):
                                temp1 = math.ceil(order.amount_total) - order.amount_total
                                check1 = (order.amount_total * 100)%10
                                check2 = (order.amount_total * 100)%100
                                temp1 += check2*(0.01) - check1*(0.1) - 0.1
                            po_line_vals ={
                                'product_id': 36,
                                'order_id': order._origin.id,
                                'name': self.round_of_cash.name,
                                'product_qty': 1,
                                'price_unit': temp1,
                                'price_subtotal': temp1,
                                'display_type': False,
                                'product_uom': 1,
                                'date_planned': datetime.now(),
                            }
                            order.order_line = [(0,0,po_line_vals)]
                order.update({
                    'amount_untaxed': order.amount_untaxed,
                    'amount_tax': order.amount_tax,
                    'amount_total': order.amount_untaxed + order.amount_tax,
                })