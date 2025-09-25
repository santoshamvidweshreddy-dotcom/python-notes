balance = int(input("please enter your account balance: "))
withdraw= int (input("please withdraw your amount: "))
if withdraw>balance:
    print("insuffient amount")
elif withdraw%100!=0:
    print("enter the amount in multiple of 100")
else:
    print("transaction successful = ", balance-withdraw)
