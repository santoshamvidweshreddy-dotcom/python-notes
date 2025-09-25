# ##ARRAYS:


# #Create integer Array:
# import array
# num = array.array('i',[1,2,3,4,5])
# print(num)

# #create float Array:
# import array
# num = array.array('f',[1.1,2.2,3.3,4.4,5.5])
# print(num)

# #1.Accessing elements(indexing):
# import array
# num = array.array('i',[10,20,30,40])
# print(num[0])
# print(num[1 or -3])
# print(num[2 or  -2])
# print(num[-1 or 3])

# #2.slicing array:
# import array
# num = array.array('i',[10,20,30,40,50])
# print(num[1:4])
# print(num[::-1])

# #3.Adding elements:

# import array
# num = array.array('i',[1,2,3])
# num.append(4)
# print(num)

# #insert at specific index -> .insert(index,value):
# import array
# num = array.array('i',[10,20,30,40])
# num.insert(1,10)
# print(num)

# #4.Remove elements:
# import array
# num = array.array('i',[10,20,30,40])
# num.remove(10)
# print(num)

# #remove element by index:
# import array
# num = array.array('i',[10,20,30,40])
# del num[0]
# print(num)

# #Basic Operations on Array:
# import array
# num = array.array('i',[1,2,3,4,5,6,7])
# print(len(num))
# print(sum(num))
# print(max(num))
# print(min(num))