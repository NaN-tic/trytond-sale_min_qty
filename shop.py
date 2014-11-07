# This file is part sale_min_qty module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['SaleShop']
__metaclass__ = PoolMeta


class SaleShop:
    __name__ = 'sale.shop'
    min_qty = fields.Boolean('Minimum Qty',
        help='Active validate minimum qty in this shop')
    max_qty = fields.Boolean('Maximum Qty',
        help='Active validate maximum qty in this shop')
