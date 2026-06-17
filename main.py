import logging
import sys


class InvalidAmountError(Exception):
    """Exception raised for invalid transaction amounts (<= 0)."""
    pass


class InsufficientBalanceError(Exception):
    """Exception raised when transfer amount exceeds current balance."""
    pass


class TransactionLogger:
    """Class to handle all logging configurations and operations."""
    
    def __init__(self):
        logging.basicConfig(
            filename='momo_transactions.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger()

    def info(self, message):
        """Log an info level message."""
        self.logger.info(message)

    def warning(self, message):
        """Log a warning level message."""
        self.logger.warning(message)

    def error(self, message):
        """Log an error level message."""
        self.logger.error(message)


class Wallet:
    """Class representing the MoMo Wallet system."""
    
    def __init__(self, logger):
        self.balance = 0
        self.logger = logger

    def deposit(self, amount):
        """Handle money deposit into the wallet."""
        if amount <= 0:
            self.logger.error(
                f"InvalidAmountError: Attempted to process {amount} VND."
            )
            raise InvalidAmountError("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
        
        self.balance += amount
        self.logger.info(
            f"Deposit successful: +{amount} VND. "
            f"Current Balance: {self.balance}"
        )

    def transfer(self, phone, amount):
        """Handle money transfer to another phone number."""
        if amount <= 0:
            self.logger.error(
                f"InvalidAmountError: Attempted to process {amount} VND."
            )
            raise InvalidAmountError("Lỗi: Số tiền giao dịch phải lớn hơn 0.")
            
        if amount > self.balance:
            self.logger.error(
                f"InsufficientBalanceError: Attempted to transfer "
                f"{amount} VND with balance {self.balance} VND."
            )
            raise InsufficientBalanceError(
                "Giao dịch thất bại: Số dư của bạn không đủ."
            )

        if amount >= 10000000:
            self.logger.warning(
                f"High value transaction detected: {amount} VND to {phone}"
            )

        self.balance -= amount
        self.logger.info(
            f"Transfer successful: -{amount} VND to {phone}. "
            f"Current Balance: {self.balance}"
        )

    def get_balance(self):
        """Retrieve the current wallet balance."""
        self.logger.info(f"Balance checked. Current Balance: {self.balance}")
        return self.balance


def display_menu():
    """Display the main interaction menu for the user."""
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("=======================================")


def main():
    """Main execution flow of the application."""
    logger = TransactionLogger()
    wallet = Wallet(logger)

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            print("\n--- NẠP TIỀN VÀO VÍ ---")
            try:
                amount = int(input("Nhập số tiền cần nạp: "))
                wallet.deposit(amount)
                print(f"\nNạp tiền thành công: +{amount:,} VND")
                print(f"Số dư hiện tại: {wallet.balance:,} VND")
            except ValueError:
                logger.error("ValueError: Invalid numeric input for deposit.")
                print("\nLỗi: Vui lòng nhập số tiền hợp lệ.")
            except InvalidAmountError as e:
                print(f"\n{e}")

        elif choice == '2':
            print("\n--- CHUYỂN TIỀN ---")
            phone = input("Nhập số điện thoại người nhận: ")
            try:
                amount = int(input("Nhập số tiền cần chuyển: "))
                wallet.transfer(phone, amount)
                print(f"\nChuyển tiền thành công tới số điện thoại {phone}.")
                print(f"Số tiền đã chuyển: {amount:,} VND")
                print(f"Số dư còn lại: {wallet.balance:,} VND")
            except ValueError:
                logger.error("ValueError: Invalid numeric input for transfer.")
                print("\nLỗi: Vui lòng nhập số tiền hợp lệ.")
            except (InvalidAmountError, InsufficientBalanceError) as e:
                print(f"\n{e}")

        elif choice == '3':
            print("\n--- SỐ DƯ VÍ MOMO ---")
            balance = wallet.get_balance()
            print(f"Số dư hiện tại: {balance:,} VND")

        elif choice == '4':
            print("\nCảm ơn bạn đã sử dụng dịch vụ")
            logger.info("System shutdown")
            sys.exit(0)


if __name__ == "__main__":
    main()