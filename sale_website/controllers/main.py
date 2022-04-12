# from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo import http


class WebsiteSale(http.Controller):

    @http.route('/shop/cart/reorder', type='http', auth="public", website=True)
    def reorder_cart(self, **kwargs):

        old_order = http.request.env['sale.order'].browse(
            int(kwargs.get('order_id')))
        new_order = http.request.website.sale_get_order(force_create=True)
        new_order.order_line.unlink()

        for line in old_order.order_line:
            new_order._cart_update(
                product_id=line.product_id.id, add_qty=line.product_uom_qty)

        return http.request.redirect('/shop/cart')
