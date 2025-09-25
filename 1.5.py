total=0
for num in range(100,500):
    is_prime = True
    if num>1:       
        for i in range(2,num):
            if num%i ==0:
                is_prime = False
                break
            if is_prime:
                total+=num
print(total)