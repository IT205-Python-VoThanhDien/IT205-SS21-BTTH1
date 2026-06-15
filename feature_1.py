import logging

logging.basicConfig(
    filename="momo_transactions.log",
    filemode="a",
    level=logging.DEBUG,
    format="[%(asctime)]"
)

account_balance = 0

recharge_money = int(input("Nhập số tiền cần nạp: "))

account_balance += recharge_money

print(account_balance)