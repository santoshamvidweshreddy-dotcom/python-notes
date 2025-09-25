marks = int(input("enter your marks(0-100): "))            
if marks<35:
    print("fail")
elif marks<60:
    print("pass")
elif marks<85:
    print("first class")
elif marks<=100:
    print("distiction")
else:
    print("invalid")
