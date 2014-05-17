#This file is part sale_min_qty module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Template']
__metaclass__ = PoolMeta


class Template:
    __name__ = 'product.template'
    sale_min_qty = fields.Integer('Sale Minimum Qty',
        help='Minimum quantity available to sale')
