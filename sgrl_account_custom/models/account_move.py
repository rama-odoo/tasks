# -*- coding: utf-8 -*-
from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"
    _description = "Account move"

    lr_number = fields.Char(string="LR Number:")
    lr_date = fields.Date(string="LR Date:")
    motor_vehicle_no = fields.Char(string="Motor Vehicle No.")
    dispatch_throug = fields.Char(string="Dispatch throug/Carrier name")
    destination = fields.Char(string="Final Destination")
    narration = fields.Text(string="Narration")
    country = fields.Many2one('res.country', string="Country")
    notify = fields.Many2one('res.partner', string="Notify 2")
    container_no = fields.Char(string="Ontainer No.")
    cont_seal_no = fields.Char(string="Cont Seal No.")
    rfid_seal_no = fields.Char(string="RFID Seal No.")
    freight = fields.Char(string="Freight")
    insurance = fields.Char(string="Insurance")
    export_under = fields.Selection([
        ('shree ganesh remedies ltd', 'Shree Ganesh Remedies Ltd'),
        ('under duty drawback', 'Under Duty Drawback'),
        ('under advance license', 'Under Advance License')])
    export_info = fields.Text(string="Export Info.")
    gross_wight = fields.Float(string="Gross Wt.")
    net_wight = fields.Float(string="Net Wt.")
    eway_bill = fields.Char(string="Eway Bill no.")
    is_export = fields.Boolean(string="Export")
    incoterm = fields.Text(string="Term and Delivery")
    export_declaration = fields.Char(string="Export Declaration")
    terms_of_delivery = fields.Text(string="Terms of Delivery")
    beneficiary = fields.Char(string="Beneficiary")
    loading_destination = fields.Char(string="Loading Destination/Port Name")
    delivery_destination = fields.Char(string="Delivery Destination/Port Name")
    pre_carriage_by = fields.Char(string="Pre- Carriage By")


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    packing_type = fields.Text(string="Packing Type")
    batch_marking = fields.Text(string="Batch No & Marking")
