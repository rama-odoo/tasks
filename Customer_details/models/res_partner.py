# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models,api


class Partner(models.Model):

    _inherit = "res.partner"

    def name_get(self):
        record = []
        print("\n\n\n\n value is print**************")
        for rec in self:
            record.append((rec.id, '%s - %s' % (rec.name, rec.zip)))
        return record


    