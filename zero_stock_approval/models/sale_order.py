from odoo import fields, _, models, api
import datetime



class SaleOrder(models.Model):

    _inherit = 'sale.order'

    approval = fields.Boolean(string=" Zero Stock Approval",store=True)

    # approval  fields logic
    def _approval(self):
         if self.env.uid == self.parent_id.user_id.id:
            self.approval = True

