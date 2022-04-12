from odoo import models, fields


class SaleOrderDeliveryTerms (models.Model):
    _name = "sale.order.delivery.terms"
    _description = "Delivery Terms"

    name = fields.Char(string="Delivery Terms")
    note = fields.Html(string="Description on the delivery notes")
    description = fields.Text('Description')
