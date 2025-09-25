num1 = float(input("enter first number: "))
operator = input("enter(+,-,*,/): ")
num2 = float(input("enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator =='-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 !=0:
        result = num1 / num2
    else:
        result = "invalid"
else:
    result = "invalid operator"

print("result:",result)