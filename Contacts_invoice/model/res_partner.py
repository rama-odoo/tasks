from odoo import fields,models,api


class Partner(models.Model):
    _inherit = "res.partner"

    is_default = fields.Boolean(string='Is Default')



class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        rec = super(SaleOrder, self).onchange_partner_id()
        for partner in self.partner_id.child_ids:
            if partner.type == 'invoice' and partner.is_default:
                self.partner_invoice_id = partner
            elif partner.type == 'delivery' and partner.is_default:
                self.partner_shipping_id = partner

        return rec
