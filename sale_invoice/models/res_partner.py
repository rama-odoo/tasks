# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    product_uom_detail_ids = fields.One2many('product.uom.detail', 'partner_id',
                                             string='Product Uom')
