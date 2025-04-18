#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
 Script Name: account.py
 Author:      Calvin C W Lin <chihweilin@163.com>
 Version:     v1.0.0
 Description: unit test case, testing normal and boundary cases
 Created:     2025-04-16
 Last Update: 2025-04-18
 Usage:       python test.py 
 Notes:       
===============================================================================
"""

import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def setUp(self):
        # initialize testing account
        self.acc1 = Account("Peter", 500)
        self.acc2 = Account("Bob", 300)

    def test_deposit(self):
        self.assertTrue(self.acc1.deposit(100))
        self.assertEqual(self.acc1.balance, 600)

        self.assertFalse(self.acc1.deposit(-50))  # deposit amount cannot be negative
        self.assertEqual(self.acc1.balance, 600)

    def test_withdraw(self):
        self.assertTrue(self.acc1.withdraw(100))
        self.assertEqual(self.acc1.balance, 400)

        self.assertFalse(self.acc1.withdraw(-50))  # withdraw amount cannot be negative
        self.assertEqual(self.acc1.balance, 400)

        self.assertFalse(self.acc1.withdraw(500))  # out of balance
        self.assertEqual(self.acc1.balance, 400)

    def test_transfer(self):
        self.assertTrue(self.acc1.transfer(self.acc2, 100))
        self.assertEqual(self.acc1.balance, 400)
        self.assertEqual(self.acc2.balance, 400)

        self.assertFalse(self.acc1.transfer(self.acc2, -50))  # transfer amount cannot be negative
        self.assertFalse(self.acc1.transfer(self.acc2, 500))  # out of balance
        self.assertEqual(self.acc1.balance, 400)
        self.assertEqual(self.acc2.balance, 400)

    def test_csv_save_and_load(self):
        accounts = [self.acc1, self.acc2]
        Account.save_to_csv(accounts, "test_accounts.csv")

        loaded_accounts = Account.load_from_csv("test_accounts.csv")
        self.assertEqual(len(loaded_accounts), 2)
        self.assertEqual(loaded_accounts[0].name, "Peter")
        self.assertEqual(loaded_accounts[0].balance, 500)
        self.assertEqual(loaded_accounts[1].name, "Bob")
        self.assertEqual(loaded_accounts[1].balance, 300)

if __name__ == "__main__":
    unittest.main()