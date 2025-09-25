a=int(input("enter the first side of triangle: "))
b=int(input("enter the second side of triangle: "))
c=int(input("enter the third side of triangle: "))

if a==b==c:
    result = "equilateral"
elif(a==b!=c or a==c!=b or b==c!=a):
    result ="isoscales"
else:
    result = "scaler"

print(result)