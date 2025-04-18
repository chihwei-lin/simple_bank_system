#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
 Script Name: account.py
 Author:      Calvin C W Lin <chihweilin@163.com>
 Version:     v1.0.0
 Description: bank account information
 Created:     2025-04-16
 Last Update: 2025-04-18
 Usage:       python account.py 
 Notes:       
===============================================================================
"""

import csv
import threading

lock = threading.Lock()

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        with lock:
            if amount > 0:
                self.balance += amount
                return True
            return False

    def withdraw(self, amount):
        with lock:
            if amount > 0 and self.balance >= amount:
                self.balance -= amount
                return True
            return False

    def transfer(self, target_account, amount):
        with lock:  
            if amount > 0 and self.balance >= amount:
                self.balance -= amount
                target_account.balance += amount
                return True
            return False

    # AccountUtils
    @staticmethod
    def save_to_csv(accounts, filename='accounts.csv'):
        with lock:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                for account in accounts:
                    writer.writerow([account.name, account.balance])

    @staticmethod
    def load_from_csv(filename='accounts.csv'):
        accounts = []
        try:
            with lock:
                with open(filename, mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        accounts.append(Account(row[0], float(row[1])))
        except FileNotFoundError:
            pass
        return accounts