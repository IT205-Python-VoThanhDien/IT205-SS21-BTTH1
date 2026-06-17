import unittest
from main import (
    Wallet, 
    TransactionLogger, 
    InvalidAmountError, 
    InsufficientBalanceError
)


class TestWallet(unittest.TestCase):
    """Unit test cases for Wallet core functionalities."""

    def setUp(self):
        """Initialize Logger and Wallet instances before each test."""
        self.logger = TransactionLogger()
        self.wallet = Wallet(self.logger)

    def test_deposit_success(self):
        """Test if depositing a valid amount correctly updates the balance."""
        self.wallet.deposit(500000)
        self.assertEqual(self.wallet.balance, 500000)

    def test_transfer_insufficient_balance(self):
        """Test if transferring more than balance raises proper exception."""
        self.wallet.deposit(300000)
        with self.assertRaises(InsufficientBalanceError):
            self.wallet.transfer("0987654321", 500000)

    def test_invalid_amount(self):
        """Test if depositing a negative amount raises proper exception."""
        with self.assertRaises(InvalidAmountError):
            self.wallet.deposit(-100000)


if __name__ == '__main__':
    unittest.main()