weight = float(input("enter your weight: "))
if weight<=49:
    result = "under weight"
elif weight<80>50:
    result = "normal weight"
elif weight>=80:
    result = "over weight"
else:
    result = "invalid"

print(result)