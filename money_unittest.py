#!/usr/bin/env python3

import unittest
from Money import Date


class TestMoneyMethods(unittest.TestCase):

    def test_adding_float_to_money(self):
        money: Date = Date(0)
        f: float = float(5.5)
        money += f
        self.assertEqual(money, 5.5)

    def test_accessing_money(self):
        money: Date = Date(5.5)
        a: float = float(0)
        a += money
        self.assertEqual(a, 5.5)

    def test_setting_currency_with_string_in_constructor(self):
        money: Date = Date("5.5 USD")
        self.assertEqual(money, 5.5)
        self.assertEqual(money.get_currency(), 'USD')

    def test_setting_currency_with_float_in_constructor(self):
        a: float = float(5.5)
        money: Date = Date(a)
        self.assertEqual(money, 5.5)

    def test_assignment(self):
        money: Date = Date()
        money = Date("10.5 USD")
        self.assertEqual(10.5, money)

    def test_setters_and_getters(self):
        money: Date = Date(10.5)
        self.assertEqual(money.get_value(), 10.5)
        money.set_value(1.1)
        self.assertEqual(money.get_value(), 1.1)
        money.set_currency('UwU')
        self.assertEqual(money.get_currency(), 'UwU')


if __name__ == "__main__":
    unittest.main()

