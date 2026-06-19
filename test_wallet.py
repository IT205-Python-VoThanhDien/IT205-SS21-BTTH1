import unittest
from momo_app import wallet, deposit, transfer

class TestMoMoFunctions(unittest.TestCase):
    
    def setUp(self):
        wallet["balance"] = 0

    def test_deposit_success(self):
        deposit(500000)
        self.assertEqual(wallet["balance"], 500000)

    def test_transfer_insufficient_balance(self):
        deposit(100000)
        
        # Bắt lỗi Exception chung, sau đó kiểm tra chuỗi bên trong có chứa chữ InsufficientBalanceError không
        with self.assertRaises(Exception) as context:
            transfer("0987654321", 200000)
        
        self.assertTrue("InsufficientBalanceError" in str(context.exception))

    def test_invalid_amount(self):
        with self.assertRaises(Exception) as context1:
            deposit(-50000)
        self.assertTrue("InvalidAmountError" in str(context1.exception))
            
        deposit(100000)
        
        with self.assertRaises(Exception) as context2:
            transfer("0987654321", -50000)
        self.assertTrue("InvalidAmountError" in str(context2.exception))

if __name__ == "__main__":
    unittest.main()