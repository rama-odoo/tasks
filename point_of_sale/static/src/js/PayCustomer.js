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

            async _onClickPay(event) {
                const currentClient = this.currentOrder.get_client();
                if (currentClient) {
                    console.log("data is valide......", currentClient.zip);
                    if (currentClient.zip) {
                        return this.showScreen('PaymentScreen');
                    }
                    else {
                        const { confirmed, payload } = await this.showPopup('TextInputPopup', {
                            title: this.env._t('Zip is Not Add'),
                            body: this.env._t('Please, Enter youer Zip Number !.'),
                        });
                        console.log(confirmed)
                        if (confirmed) {
                            await this.rpc({
                                model: 'res.partner',
                                method: 'write',
                                args: [[currentClient.id], { zip: payload }],
                            });
                        }
                    }
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
