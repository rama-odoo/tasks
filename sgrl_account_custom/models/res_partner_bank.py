# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    ifsc_code = fields.Char(string="IFSC CODE")
    ad_code = fields.Char(string="AD CODE")
