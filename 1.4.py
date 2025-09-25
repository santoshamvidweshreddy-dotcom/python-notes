for num in range(100,501):
    is_prime = True
    if num>1:
        for i in range(2,int(num**0.5)+1):
            if num%i ==0:
                is_prime = False
                break
            if is_prime:
                print(num,end=" ")
