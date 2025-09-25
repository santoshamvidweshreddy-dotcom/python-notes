num = int(input("enter your number: "))
counter = 0
for i in range(1,num+1):
    if(num%i==0):
        counter+=1

if(counter==2):
    print("the given number is a prime number")
else:
    print("the given number is not a prime number")