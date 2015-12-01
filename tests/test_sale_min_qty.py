# This file is part of the sale_min_qty module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleMinQtyTestCase(ModuleTestCase):
    'Test Sale Min Qty module'
    module = 'sale_min_qty'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleMinQtyTestCase))
    return suite