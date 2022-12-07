# -*- coding: utf-8 -*-

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    pan_no = fields.Char(string='PAN No.')
    iec_code = fields.Char(string='IEC CODE')
