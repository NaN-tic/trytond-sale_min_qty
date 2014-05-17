#This file is part sale_min_qty module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['SaleLine']
__metaclass__ = PoolMeta


class SaleLine:
    __name__ = 'sale.line'

    @classmethod
    def __setup__(cls):
        super(SaleLine, cls).__setup__()
        cls._error_messages.update({
                'min_qty_product': 'Quantity product line "%s" is less than '
                    'quantity available for sale in product. '
                    '(Minimum quantity is: %s).',
                })

    def on_change_quantity(self):
        User = Pool().get('res.user')
        user = User(Transaction().user)

        res = super(SaleLine, self).on_change_quantity()

        # TODO: replace user.shop to sale.shop
        if not user.shop:
            return res

        if (user.shop.min_qty
                and self.product and self.product.template.sale_min_qty
                and self.quantity
                and not self.product.template.sale_min_qty <= self.quantity):
            self.raise_user_error('min_qty_product',
                (self.product.rec_name, self.product.sale_min_qty))

        return res
