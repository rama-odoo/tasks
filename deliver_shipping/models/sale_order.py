# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, _, models, api
import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'
   
    appointment_date = fields.Datetime(string="Appointment Date")
    commitment_date = fields.Datetime(readonly=False, compute='compute_commitment_date')

    @api.depends('appointment_date')
    def compute_commitment_date(self):
        for record in self:
            if record.appointment_date and record.partner_id.days_deliver > 0:
                record.commitment_date = record.appointment_date - datetime.timedelta(days=record.partner_id.days_deliver)

# action confirm button

    def action_confirm(self):
        print("\n confirm order in delivery")
        for record in self:
            record = super(SaleOrder , self).action_confirm()
        for data in self.picking_ids:
            data.appointment_date = self.appointment_date
        return record