#!/usr/bin/env python
# This file is part sale_min_qty module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class SaleMinQtyTestCase(unittest.TestCase):
    'Test Sale Minimum Quantity module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_min_qty')

    def test0005views(self):
        'Test views'
        test_view('sale_min_qty')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleMinQtyTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
