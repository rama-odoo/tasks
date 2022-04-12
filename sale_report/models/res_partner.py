# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import  models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if name:

            name = name.split(' / ')[-1]
            args = ['|', ('name', operator, name),
                    ('mobile', operator, name), ]

        return self._search(args, limit=limit, access_rights_uid=name_get_uid)
