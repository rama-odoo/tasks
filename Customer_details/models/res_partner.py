# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models


class Partner(models.Model):

    _inherit = "res.partner"

    def name_get(self):
        record = []
        for rec in self:
            record.append((rec.id, '%s - %s' % (rec.name, rec.zip)))
        return record
