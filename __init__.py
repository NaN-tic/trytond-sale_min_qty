# This file is part sale_min_qty module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import product
from . import shop
from . import sale


def register():
    Pool.register(
        product.Template,
        shop.SaleShop,
        sale.SaleLine,
        module='sale_min_qty', type_='model')
