from src.bank_account import BankAccount
from src.exceptions import InsufficientFundsError, WithdrawlTimeRestrictionError, WithdrawDateRestrictionError
import unittest
import os
from unittest.mock import MagicMock, patch


class BankAccountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount(balance=0, log_file="transactions.log")

    def tearDown(self) -> None:
        if self.account.log_file and os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def test_initialize_account(self):
        self.assertEqual(self.account.get_balance(), 0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100)
        self.assertIn("no puedes depositar montos negativos", str(context.exception))

    @patch("src.bank_account.dt.datetime")
    def test_withdraw(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.weekday.return_value = 1
        mock_now.hour = 10
        mock_datetime.now.return_value = mock_now

        self.account.deposit(500)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 400)

    @patch("src.bank_account.dt.datetime")
    def test_witdraw_negative_amount(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.weekday.return_value = 1
        mock_now.hour = 10
        mock_datetime.now.return_value = mock_now

        self.account.deposit(400)
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-100)
        self.assertIn("no puedes retirar montos negativos", str(context.exception))

    @patch("src.bank_account.dt.datetime")
    def test_withdraw_amount_gt_balance(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.weekday.return_value = 1
        mock_now.hour = 10
        mock_datetime.now.return_value = mock_now

        self.account.deposit(400)
        with self.assertRaises(InsufficientFundsError) as context:
            self.account.withdraw(500)
        self.assertIn("saldo insuficiente", str(context.exception))
        self.assertEqual(self.account.get_log()[-1], "Saldo insuficiente, no puedes retirar 500, tu balance disponble es 400\n")

    @patch("src.bank_account.dt.datetime")
    def test_transfer_to_anoter_account(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.weekday.return_value = 1
        mock_now.hour = 10
        mock_datetime.now.return_value = mock_now

        self.account.deposit(600)
        other_account = BankAccount(0)
        transfer_result = self.account.transfer(other_account, 500)
        self.assertTrue(transfer_result)
        self.assertEqual(self.account.get_balance(), 100)
        self.assertEqual(other_account.get_balance(), 500)

    def test_transaction_log_exist(self):
        self.account.deposit(400)
        self.assertTrue(os.path.exists(self.account.log_file))
        self.assertIsNotNone(self.account.get_log())

    def test_transactions_log_size(self):
        self.assertEqual(self.account.get_log(), ["Cuenta creada.\n"])
        self.account.deposit(400)
        self.assertEqual(self.account.get_log(), ["Cuenta creada.\n", 'Deposit: 400, new balance 400\n'])

    @patch("src.bank_account.dt.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.weekday.return_value = 1
        mock_now.hour = 10
        mock_datetime.now.return_value = mock_now

        self.account.deposit(400)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 300)

    @patch("src.bank_account.dt.datetime")
    def test_withdraw_disallow_before_bussines_hours(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.weekday.return_value = 1
        mock_now.hour = 6
        mock_datetime.now.return_value = mock_now

        self.account.deposit(400)
        with self.assertRaises(WithdrawlTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.dt.datetime")
    def test_withdraw_disallow_after_bussines_hours(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.weekday.return_value = 1
        mock_now.hour = 19
        mock_datetime.now.return_value = mock_now

        self.account.deposit(400)
        with self.assertRaises(WithdrawlTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.dt.datetime")
    def test_withdraw_on_monday(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.weekday.return_value = 1 # weekday() retorna 6
        mock_now.hour = 10

        # Hacer que datetime.now() retorne nuestro mock
        mock_datetime.now.return_value = mock_now

        self.account.deposit(400)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 300)

    @patch("src.bank_account.dt.datetime")
    def test_withdraw_on_sunday(self, mock_datetime):
        mock_now = MagicMock()
        mock_now.weekday.return_value = 6  # weekday() retorna 6
        mock_now.hour = 10

        # Hacer que datetime.now() retorne nuestro mock
        mock_datetime.now.return_value = mock_now

        self.account.deposit(400)
        with self.assertRaises(WithdrawDateRestrictionError):
            self.account.withdraw(100)

    def test_deposit_with_multiple_amounts(self):
        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 3000, "expected": 4000},
            {"amount": 4500, "expected": 5500},
        ]
        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="log.log")
                new_balance = self.account.deposit(case.get("amount"))
                self.assertEqual(new_balance, case.get("expected"))

    def test_bank_account_without_log(self):
        acount = BankAccount(balance=100)
        acount.deposit(100)
        self.assertEqual(acount.get_log(), None)
