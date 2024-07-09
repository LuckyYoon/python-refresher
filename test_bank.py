import unittest
from bank import account


class testBank(unittest.TestCase):
    def setUp(self):
        self.Account = account(100, "1", "LuckyYoon")

    def testInit(self):
        self.assertEqual(self.Account.info(), (100, "1", "LuckyYoon"))

    def testWithdraw(self):
        self.assertEqual(self.Account.withdraw(50), 50)
        self.assertEqual(self.Account.withdraw(200), None)

    def testDeposit(self):
        self.assertEqual(self.Account.deposit(100), 200)
        self.assertEqual(self.Account.deposit(-100), None)

    def testCheckBalance(self):
        self.assertEqual(self.Account.checkBalance(), 100)
        self.Account.deposit(100)
        self.assertEqual(self.Account.checkBalance(), 200)
        self.Account.withdraw(100)
        self.assertEqual(self.Account.checkBalance(), 100)
