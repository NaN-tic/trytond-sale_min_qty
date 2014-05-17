#This file is part sale_min_qty module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .product import *
from .shop import *
from .sale import *


def register():
    Pool.register(
        Template,
        SaleShop,
        SaleLine,
        module='sale_min_qty', type_='model')
