for i in range(7):
    print(i)
    print("done")

count=0
while count<=10:
    print(count)
    count+=1 #count = count+1  

marks = 1
while marks!=0:
    marks = int(input("enter marks:"))
    if marks>90:
        print("Grade A")
    elif marks>80:
        print("Grade B")
    elif marks>50:
        print("Grade C")
    else:
        print("pack your bags")