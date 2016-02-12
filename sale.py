# This file is part sale_min_qty module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import fields
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
                'max_qty_product': 'Quantity product line "%s" is more than '
                    'quantity available for sale in product. '
                    '(Maximum quantity is: %s).',
                })

    @fields.depends('sale')
    def on_change_quantity(self):
        User = Pool().get('res.user')

        super(SaleLine, self).on_change_quantity()

        if Transaction().context.get('check_qty', True):
            shop = None
            if self.sale and hasattr(self.sale, 'shop'):
                shop = self.sale.shop
            else:
                user = User(Transaction().user)
                if user.shop:
                    shop = user.shop

            if shop:
                if (shop.min_qty
                        and self.product and self.product.template.sale_min_qty
                        and self.quantity
                        and not self.product.template.sale_min_qty <= self.quantity):
                    self.raise_user_error('min_qty_product',
                        (self.product.rec_name, self.product.sale_min_qty))
                if (shop.max_qty
                        and self.product and self.product.template.sale_max_qty
                        and self.quantity
                        and not self.product.template.sale_max_qty > self.quantity-1):
                    self.raise_user_error('max_qty_product',
                        (self.product.rec_name, self.product.sale_max_qty))
