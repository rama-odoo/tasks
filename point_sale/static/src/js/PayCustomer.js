odoo.define('point_sale.ProductScreen', function (require) {
    'use strict';
    console.log("test successful");

    const ProductScreen = require('point_of_sale.ProductScreen');
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require('web.custom_hooks');

    const PointSaleProductScreen = (ProductScreen) =>
        class extends ProductScreen {

            constructor() {
                super(...arguments);

                useListener('click-pay', this._onClickPay);
            }

            _onClickPay() {
                const currentClient = this.currentOrder.get_client();
                if (currentClient && this.currentOrder.get_client_name()) {
                    return  this.showScreen('PaymentScreen');
                }
                else {
                    this.showPopup('ErrorPopup', {
                        title: this.env._t("Customer Add"),
                        body: this.env._t(
                            "Customer is not Add plese Add customer."
                        ),
                    });
                }
            }
        }
    Registries.Component.extend(ProductScreen, PointSaleProductScreen);
    return ProductScreen;
});
