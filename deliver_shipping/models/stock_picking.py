from odoo import fields, _, models,api
import datetime

class StockPicking(models.Model):

   _inherit = 'stock.picking'

   appointment_date = fields.Datetime(string="Appointment Date")
  
   @api.onchange('appointment_date')
   def _onchange_date(self) :
        for record in self :
            if record.appointment_date and record.partner_id.day_to_delivrer > 0:
                record.scheduled_date = record.appointment_date - datetime.timedelta(days=record.partner_id.days_deliver)