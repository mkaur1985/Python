
#List : is mutable ,means it can be updated once created , use of[]
#Tuples : non-mutable , means it cannot be updated(add or remove etc) once created , use of () but again () are optional


# Example of Tuples
a="apple","mango","banana",1,45,67,89.0
b=("apple","mango","banana")
print(type(a))
print(type(b))

#a.append("abc") # this will throw error , as tuples cannot be updated.
#output:
# <class 'tuple'>


# when a tuple has only 1 value then how to create a tuple ?

a="apple"
print(type(a))  #output string

a="apple",
print(type(a))  #output tuple


# /***********************************
# --Slicing and Iteration in tuples
# ************************************/

a=("OnePlus","Vivo","Redmi","Samsung","Nokia")
# print(a[1:3]) # if we want to print Vivo and Redmi we have to give index as 3 , because we always add 1 to the n value ( 0 to n+1)  otherwise it will not give the correct result.
# print(a[:3])
# print(a[2:])
# print(a[::2]) # we want here gap of 2 for complete tuple.
# print(a[1::2])
# print(a[::-1]) # reverse copplete tuple.
# print(a[2::-1]) # from Redimi to reverse order so we used -1

# *****************************
# -- Iteration
# ******************************
# 1. For loop
a=("OnePlus","Vivo","Redmi","Samsung","Nokia")
for i in a:
    print(i)

# 2. along with range and length in for loop
for i in range(len(a)):
    print(a[i])  # we want value of index here , if we use only i that will give us index.

#3. along with while loop.
i=0
while (i<len(a)):
    print(a[i])
    i=i+1









