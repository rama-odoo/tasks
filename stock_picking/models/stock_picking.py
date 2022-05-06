from pickle import TRUE
from odoo import fields, models, _


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    show_additional_name = fields.Boolean(string="Additional Name")


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    lot_secound_name = fields.Char('Lot /Secound Name')

    def _assign_production_lot(self, lot):
        res = super(StockMoveLine, self)._assign_production_lot(lot)

        lot.lot_secound_name = self.lot_secound_name
        return res


class StockMove(models.Model):
    _inherit = "stock.move"

    def action_show_details(self):
        res = super(StockMove, self).action_show_details()

        if self.picking_type_id.show_additional_name:
            res['context']['lot'] = True
        else:
            False,

        return res


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    lot_secound_name = fields.Char("Second lot Name")
