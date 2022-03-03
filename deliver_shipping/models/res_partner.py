# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    days_deliver = fields.Integer(string="Days to Deliver")
   