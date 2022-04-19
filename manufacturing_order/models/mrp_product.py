from odoo import models


class MrpProduction(models.Model):

    _inherit = "mrp.production"

    def serial_lot(self):
        data = {}
        for product_id in self.filtered(lambda mo: mo.state == 'confirmed').mapped('product_id').ids:

            for production in self.filtered(lambda xo: xo.product_id.id == product_id and not xo.lot_producing_id):
                if product_id in data.keys():
                    data[product_id] = data[product_id].append(production)
                else:
                    data[product_id] = [production]
