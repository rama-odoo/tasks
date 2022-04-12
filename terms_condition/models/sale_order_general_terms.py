from odoo import models, fields


class SaleOrderGeneralTerms (models.Model):
    _name = "sale.order.general.terms"
    _description = "General Terms"

    name = fields.Char(string="General Terms")
    note = fields.Html(string="Description on the General notes")
    code = fields.Integer(string="code")
    description = fields.Text('Description')
