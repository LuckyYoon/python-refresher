import unittest
from bank import account

class testBank(unittest.TestCase):
    def testInit(self):
        Account = account(100, "1", "LuckyYoon")
        self.assertEqual(Account.info(), (100, "1", "LuckyYoon"))

    def testWithdraw(self):
        Account = account(100, "1", "LuckyYoon")
        self.assertEqual(Account.withdraw(50), 50)
        self.assertEqual(Account.withdraw(200), None)
    
    def testDeposit(self):
        Account = account(100, "1", "LuckyYoon")
        self.assertEqual(Account.deposit(100), 200)
        self.assertEqual(Account.deposit(-100), None)

    def testCheckBalance(self):
        Account = account(100, "1", "LuckyYoon")
        self.assertEqual(Account.checkBalance(), 100)
        Account.deposit(100)
        self.assertEqual(Account.checkBalance(), 200)
        Account.withdraw(100)
        self.assertEqual(Account.checkBalance(), 100)