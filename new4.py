# ##FUNCTIONS:

# def function():
#     print("Hello world!")
# function()

# #Passing Parameters and Arguments:

# def my_function(name):
#     print("Hello", name)
# my_function("world")

# #Function Arguments Types:
# #a)position Arguments

# def add(a,b):
#     print("sum is: ",a+b)
# add(5,10)

# #Keyword Arguments
# def introduce(name,age):
#     print(f"my name is {name} , my age is {age}")
# introduce(name="vidwesh",age=18)

# #b)Default Arguments:

# def my_function(name="guest"):
#     print("Hello",name)
# my_function()
# my_function("ram")

##SCOPE OF VARIABLES:
x = 100
def func():
    y = 50
    print("inside function,x=",x)
    print("inside function,y=",y)
func()
print("outside function,x=",x)
print(y)#error
