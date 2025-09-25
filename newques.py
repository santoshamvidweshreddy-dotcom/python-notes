# # sum of 1st 5 natural numbers
# num =1
# for i in range(2,6):
#     num += i #num=num+i(num always updates)
# print("sum =",num)




# #multiplication table
# num = int(input("enter a number : "))
# for i in range(1,11):
#     print(f"{num}*{i}={num*i}")




# #CHECK IF AN ELEMENT EXISTS:

# #list :
# fruit = input("Enter a fruit: ")
# fruits = ['apple', 'banana', 'grapes']

# if fruit in fruits:
#     print("Present")
# else:
#     print("Absent")

# #tuple:
# fruit = input("Enter a fruit: ")
# fruits = ('apple', 'banana', 'grapes')

# if fruit in fruits:
#     print("Present")
# else:
#     print("Absent")





    

# #print number in reverse(5 to 1)
# for i in range(5,0,-1):
# #start at 5,stop before 0,decrement by 1
#     print(i)




# #print squares of number form 1 to 5
# for i in range(1,6):
#     print(f"{i}*{i}={i*i}")



# #print first five even number 
# for i  in range(0,100):
#     if i%2==0:
#         if i==10:
#             print("first even number")      
#             break
#         print(i)


# #use list for above question
# list=[1,3,5,2,7,9]
# for num in list:
#     if num%2==0:
#         print("first even number found",num)
#         break
# else:
#     print("not found any even number")


# #user input simulation\
# while True:
#     name = input("enter 'vidwesh' to stop code:") 
#     if name == 'vidwesh':
#         print("logined")
#         break
#     else:
#         print("try again")



##continuequestion by using tuple: 
# tuple=(-1,-2,1,2,3,4)
# for i in tuple:
#     if i<0:
#         print("skipping negative numbers")
#         continue
#     print(i)


# tuple=(-1,6,1,2,3,4)
# for i in tuple:
#     if i%3==0:
#         print("skipping negative numbers")
#         continue
#     print(i)

# #1)
# import array
# num = array.array('i',[1,2,3,4,5])
# print(num[0])
# print(num[-1])

# #2)
# import array
# num = array.array('i',[1,2,3,4,5])
# print(num[2:5])

# #3)
# import array
# num = array.array('i',[1,2,3,4,5])
# print(num[-3:-1])


# #4)
# import array
# num = array.array('i',[1,2,3,4,5])
# print(num[::2])

# #5)
# import array
# num = array.array('i',[5,10,15,20,25,30])
# print(num[:4])
# count=0
# for i in num[:4]:
#     count += i
# print(count)
    

# #6)
# import array
# num = array.array('i',[1,2,3,4,5])
# print(num[::-1])


# #1)
# a = int(input("enter number:"))
# b = int(input("enter number:"))
# def function(a,b):
#     print("mul is:",a*b)
# function(a,b)

# #2)
# num= int(input("enter a number: "))
# def func(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# func(num)


# #3)
# a = int(input("enter number:"))
# def func(num):
#     result = 1
#     for i in range(1,num+1):
#         result*=i
#     print(result)
# func(a)

# #4)
# a = int(input("enter number:"))
# b = int(input("enter number:"))
# c = int(input("enter number:"))
# def func(a,b,c):
#     if (a>b>c or a>c>b):
#         print("a")
#     elif (b>a>c or b>c>a):
#         print("b")
#     else:
#         print("c")
# func(a,b,c)


# #5)
# name = input("enter your name:")
# def func(name):
#     print(name[::-1])
# func(name)


# #6)
# name = input("enter your name:")
# def func(name):
#     vowels= "aeiouAEIOU"
#     count = 0
#     for char in name:
#         if char in vowels:
#             count+=1
#     print(count)
# func(name)


# #1)
# a = float(input("enter a number: "))
# b = float(input("enter a number: "))
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)

# #2)
# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# a+=b
# b=a-b
# a-=b

# print(a)
# print(b)



# #3)
# a = float(input("enter a number: "))
# b = float(input("enter a number: "))
# if a==b:
#     print("two variables are equal")
# else:
#     print("two variables are not equal")




# #7)
# num = int(input("enter a number: "))
# list = [1,2,3,4,5]
# if num in list:
#     print("present")
# else:
#     print("not present")

# #6)
# marks = int(input("enter marks:"))
# if (marks>=35 and marks<=100):
#     print("pass")
# elif marks<35:
#     print("fail")
# else:
#     print("not valid")

# #5)
# import array
# arr1 = array.array('i',[1,2,3])
# arr2 = array.array('i',[4,5,6])
# result1 = array.array('f',[(arr1[i]+arr2[i])/2 for i in range(len(arr1))])
# result2 = array.array('i',[arr1[i]+arr2[i] for i in range(len(arr1))])
# print(result1)
# print(result2)

# #4)
# def sum(a):
#     return a+a
# number = [1,2,3,4,5]
# sum = list(map(sum,number))
# print(sum)
