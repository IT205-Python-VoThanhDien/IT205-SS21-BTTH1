print(" VÍ MOMO GIẢ LẬP ".center(50,"="))
print("1. Nạp tiền vào ví")
print("2. Chuyển tiền")
print("3. Xem số dư hiện tại")
print("4. Thoát chương trình")
print("="*50)

user_choice = input("Nhập lựa chọn của bạn: ")
match user_choice:
    case '1':
        pass
    case '4':
        exit()