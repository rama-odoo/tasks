# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, _, models, api
import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    approval = fields.Boolean(string=" Zero Stock Approval",store=True)

    def _approval(self):
         if self.env.uid == self.parent_id.user_id.id:
            self.approval = True
