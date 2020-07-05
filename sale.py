# This file is part sale_min_qty module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import fields
from trytond.transaction import Transaction
from trytond.i18n import gettext
from trytond.exceptions import UserError

__all__ = ['SaleLine']


class SaleLine(metaclass=PoolMeta):
    __name__ = 'sale.line'

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
                    raise UserError(gettext('sale_min_qty.msg_min_qty_product',
                        product=self.product.rec_name,
                        qty=self.product.sale_min_qty))
                if (shop.max_qty
                        and self.product and self.product.template.sale_max_qty
                        and self.quantity
                        and not self.product.template.sale_max_qty > self.quantity-1):
                    raise UserError(gettext('sale_min_qty.msg_max_qty_product',
                        product=self.product.rec_name,
                        qty=self.product.sale_max_qty))
