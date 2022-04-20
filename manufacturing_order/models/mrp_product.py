from odoo import models


class MrpProduction(models.Model):

    _inherit = "mrp.production"

    def serial_lot(self):
        data = {}
        filtered_mo = self.filtered(
            lambda mo: mo.state == 'confirmed' and not mo.lot_producing_id)
        for product in filtered_mo:
            for product_id in product .mapped('product_id').ids:
                for production in filtered_mo.filtered(lambda xo: xo.product_id.id == product_id):
                    if product_id in data.keys():
                        data[product_id].append(production)
                    else:
                        data[product_id] = [production]
            for p in data.keys():
                a = 1
                ans = 0
                for vals in data[p]:
                    if a == 1:
                        vals.action_generate_serial()
                        ans = vals.lot_producing_id
                        a = a+1
                    else:
                        vals.lot_producing_id = ans