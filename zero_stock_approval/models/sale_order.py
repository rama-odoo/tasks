# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, _, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval = fields.Boolean(string=" Zero Stock Approval", store=True)
