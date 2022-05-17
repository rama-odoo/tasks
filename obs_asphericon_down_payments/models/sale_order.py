from odoo import models,fields,api,_

class SaleOrder(models.Model):
    _inherit = "sale.order"

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    deduction_rate = fields.Float('Deduction Rate')
