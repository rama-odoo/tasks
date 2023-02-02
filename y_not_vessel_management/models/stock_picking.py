# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    product_id = fields.Many2one('product.product', 'Product',store=True)
    currency_id = fields.Many2one('res.currency', "Currency", store=True)
    coupon_program_id = fields.Many2one('coupon.program', 'Discount Program', store=True)
    display_type = fields.Selection([
        ('line_section', 'Section'), ('line_note', 'Note')
    ], store=True, string='Display Type')
    project_id = fields.Many2one('project.project', 'Generated Project', store=True)
    task_id = fields.Many2one('project.task', 'Generated Task', store=True)
    invoice_status = fields.Selection([('upselling', 'Upselling Opportunity'), ('invoiced', 'Fully Invoiced'),
                                       ('to invoice', 'To Invoice'), ('no', 'Nothing to Invoice')], store=True,
                                      string='Invoice Status')
    is_service = fields.Boolean(string='Is a Service', store=True)
    is_delivery = fields.Boolean(string="Is a Delivery", store=True)
    is_reward_line = fields.Boolean(string="Is a program reward line", store=True)
    is_downpayment = fields.Boolean(string="Is a down payment", store=True)
    is_expense = fields.Boolean(string="Is expense", store=True)
    item_no = fields.Char(string="Item no",store=True)
    linked_line_id = fields.Many2one('sale.order.line', 'Linked Order Line', store=True)
    qty_delivered_method = fields.Selection([('manual','Manual'),('analytic','Analytic From Expenses'),('stock_move','Stock Moves'),('timesheet','Timesheets')],store=True,string='Method to update delivered qty')
    order_id = fields.Many2one('sale.order',string="Order Reference",store=True)
    order_type = fields.Selection([('Sales Contract','Sales Contract'),('Sales Order','Sales Order')],string="Order Type",store=True)
    po_no_customer_po = fields.Char(string="PO No (Customer PO)",store=True)
    product_packaging = fields.Many2one('product.packaging',string="Package",store=True)
    route_id = fields.Many2one('stock.location.route',string="Route",store=True)
    salesman_id = fields.Many2one('res.users',string="Salesperson",store=True)
    sequence = fields.Integer(string="Sequence",store=True)
    # x_studio_vessel = fields.Many2one('x_vessel',string="Vessel",store=True)
    ship_date = fields.Datetime(string='Ship Date',store=True)
    product_uom = fields.Many2one('uom.uom',string='Unit of Measure',store=True)
    quantity_done = fields.Float(related='move_lines.quantity_done',string="Done",store=True)
    product_uom_qty = fields.Float(related='move_lines.product_uom_qty',string="Quantity Demand",store=True)
