# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResCompany(models.Model):

    _inherit = 'res.company'

    partner_id = fields.Many2one('res.partner', string='Partner')
