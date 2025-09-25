num1 = float(input("enter first number: "))
operator = input("enter operator (+,-,*,/): ")
num2 = float(input("enter last number: "))

if operator=='+':
    result = num1 + num2
elif operator=='-':
    result = num1 - num2
elif operator=='*':
    result = num1 * num2
elif operator=='/':
    if num2!=0:
        result = num1 / num2
    else:
        result = "invalid"
else:
    print("error")

print("Result: ",result)

