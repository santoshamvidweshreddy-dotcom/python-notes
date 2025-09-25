units = int(input("enter no.of electricity units: "))
if units>1<=100:
    result = units*5
elif units>101<=200:
    result = units*7
elif units>200:
    result = units*10
else:
    result= "invalid"

print("Result =",result)
