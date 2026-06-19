import logging
import sys


logging.basicConfig(
    filename='momo_transactions.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)


wallet = {
    "balance": 0
}


def deposit(amount):
    """Xử lý nạp tiền vào ví"""
    if amount <= 0:
     
        raise Exception(f"InvalidAmountError: Attempted to process {amount} VND.")
    
    wallet["balance"] += amount
    logging.info(f"Deposit successful: +{amount} VND. Current Balance: {wallet['balance']}")
    
    print("\n--- NẠP TIỀN VÀO VÍ ---")
    print(f"Nạp tiền thành công: +{amount:,} VND".replace(',', '.'))
    print(f"Số dư hiện tại: {wallet['balance']:,} VND".replace(',', '.'))

def transfer(phone, amount):
    """Xử lý chuyển tiền"""
    if amount <= 0:
        raise Exception(f"InvalidAmountError: Attempted to process {amount} VND.")
    
    if amount > wallet["balance"]:
        raise Exception(f"InsufficientBalanceError: Attempted to transfer {amount} VND with balance {wallet['balance']} VND.")
    
    wallet["balance"] -= amount
    
    if amount >= 10000000:
        logging.warning(f"High value transaction detected: {amount} VND to {phone}")
        
    logging.info(f"Transfer successful: -{amount} VND to {phone}. Current Balance: {wallet['balance']}")
    
    print("\n--- CHUYỂN TIỀN ---")
    print(f"Chuyển tiền thành công tới số điện thoại {phone}.")
    print(f"Số tiền đã chuyển: {amount:,} VND".replace(',', '.'))
    print(f"Số dư còn lại: {wallet['balance']:,} VND".replace(',', '.'))

def check_balance():
    """Hiển thị số dư hiện tại"""
    logging.info(f"Balance checked. Current Balance: {wallet['balance']}")
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {wallet['balance']:,} VND".replace(',', '.'))

def display_menu():
    """Hiển thị Menu và xử lý luồng chạy chính"""
    while True:
        print("\n========== VÍ MOMO GIẢ LẬP ==========")
        print("1. Nạp tiền vào ví")
        print("2. Chuyển tiền")
        print("3. Xem số dư hiện tại")
        print("4. Thoát chương trình")
        print("=======================================")
        
        choice = input("Chọn chức năng (1-4): ")
        
        try:
            if choice == '1':
                amount = int(input("Nhập số tiền cần nạp: "))
                deposit(amount)
                
            elif choice == '2':
                phone = input("Nhập số điện thoại người nhận: ")
                if len(phone) != 10 or not phone.isdigit():
                    print("Lỗi: Số điện thoại phải bao gồm đúng 10 chữ số.")
                    continue
                    
                amount = int(input("Nhập số tiền cần chuyển: "))
                transfer(phone, amount)
                
            elif choice == '3':
                check_balance()
                
            elif choice == '4':
                print("Cảm ơn bạn đã sử dụng dịch vụ!")
                logging.info("System shutdown")
                sys.exit()
            else:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại (1-4).")
                
        except ValueError:
            print("\nLỗi: Vui lòng nhập số tiền hợp lệ.")
            logging.error("ValueError: Invalid numeric input for transaction.")
            
        except Exception as e:
          
            error_message = str(e)
            
            if "InvalidAmountError" in error_message:
                print("\nLỗi: Số tiền giao dịch phải lớn hơn 0.")
                logging.error(error_message)
                
            elif "InsufficientBalanceError" in error_message:
                print("\nGiao dịch thất bại: Số dư của bạn không đủ.")
                logging.error(error_message)
                
            else:
               
                print("\nĐã xảy ra lỗi hệ thống.")
                logging.error(f"UnknownError: {error_message}")


if __name__ == "__main__":
    display_menu()