for num in range(1,100):
    if num%13==0:
        print(f"found it! the first number divisible by 13 is {num}:")
        break

for i in range(1,11):
    if i==5:
        continue
    print(i)