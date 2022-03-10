from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # discount_2 = fields.Float(string="2nd Disc.%", related="move_id.discount_2")
    discount_2 = fields.Float(string="2nd Disc.%")
   

    def _get_price_total_and_subtotal(self,price_unit=None, quantity=None, discount=None, currency=None, product=None, partner=None, taxes=None, move_type=None):
        # self.ensure_one()
      res = super()._get_price_total_and_subtotal(price_unit=price_unit,quantity=quantity,discount=discount,currency=currency,product=product,partner=partner,taxes=taxes,move_type=move_type)
      print("***res *** : ",res.get('price_subtotal'))
      print("2 discount,",self.discount_2)
      price_subtotal = res.get('price_subtotal') - ((res.get('price_subtotal')*self.discount_2)/100)
      res['price_subtotal'] = price_subtotal
      print("***res****",res)
      return res