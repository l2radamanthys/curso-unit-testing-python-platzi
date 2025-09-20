from src.bank_account import BankAccount
import unittest


class BankAccountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount(0)

    def test_initialize_account(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100)
        self.assertIn("no puedes depositar montos negativos", str(context.exception))

    def test_withdraw(self):
        self.account.deposit(500)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 400)

    def test_witdraw_negative_amount(self):
        self.account.deposit(400)
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100)
        self.assertIn("no puedes depositar montos negativos", str(context.exception))

    def test_withdraw_amount_gt_balance(self):
        self.account.deposit(400)
        with self.assertRaises(Exception) as context:
            self.account.withdraw(500)
        self.assertIn("saldo insuficiente", str(context.exception))

    def test_transfer_to_anoter_account(self):
        self.account.deposit(600)
        other_account = BankAccount(0)
        transfer_result = self.account.transfer(other_account, 500)
        self.assertTrue(transfer_result)
        self.assertEqual(self.account.get_balance(), 100)
        self.assertEqual(other_account.get_balance(), 500)
