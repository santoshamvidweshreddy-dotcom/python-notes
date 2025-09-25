# ##Higher Order Function:

# #a)map():
# def square(x):
#     return x*x
# number = [1,2,3,4,5]
# squared = list(map(square,number))
# print(squared)

# #b)filter():
# def is_even(x):
#     return x%2==0
# number = [1,2,3,4,5,6]
# even_numbers = list(filter(is_even,number))
# print(even_numbers)

# #c)reduce():
# from functools import reduce
# def add(x,y):
#     return x+y
# numbers = [1,2,3,4,5]
# sum_numbers = reduce(add,numbers)
# print(sum_numbers)


#numpy array


# ##NUMPY ARRAY:
# import numpy as np 
# #1D:
# arr1 = np.array([1,2,3,4,5])
# print(arr1)
# #2D:
# arr2 = np.array([1,2,3])
# print(arr2)


# ##adding 2 arrays:
# #using python array:

# import array
# a = array.array('i',[1,2,3])
# b = array.array('i',[4,5,6])
# result = array.array('i',[a[i]+b[i] for i in range(len(a))])
# print(result)

# #using numpy array:
# import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# result = a+b
# print(result)
