

# /**********************************
#  -- Functions Problem Solving
# ***********************************/
# 1. write a function to find maximum of three numbers in python.
def maximum_num(val1,val2,val3):
    if val1>val2 and val1>val3:
        return(print(val1 ,"is the maximum of all"))
    elif val2>val3 and  val2>val1:
     return(print(val2,"is the maximum of all"))
    else:
            return(print(val3,"is the maximum value"))

maximum_num(5,7,91)
#output: 91

# 2. Write a python function to create and print a list where the values are square of numbers between 1 and 30.
def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())
#output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]

# 3.write a python function that takes a number as a parameter and check if the number is prime or not.
def prime_func(n):
    if(n==1):
        print(n , " : is not a prime number")
    for i in range (2,n):
            if(n%i==0 ):
             print(n," : is not a prime number")
             break # to come out of the loop , otherwise it keeps on printing same sence for each iteration.
            else:
              print(n, " : is  a prime number")
            break
    return n
prime_func(7)


# 4. Write a python function to sum all the numbers in a list.
def add(numbers): # complete list has been assigned to varibale number=[12,4,5,6,7,8,9] during function call.
    print(numbers)
    total=0
    for i in numbers:
        print(i)
        total=total+i
    return(total)

print("sum of all the list numbers: ", add([12,4,5,6,7,8,9]) )

# ********************************************************************
# NOTES:
# a=[10,12,13,14]  this is a list
# for i in a  # this means i will have values from list a
# for i in range(len(a)) # this means i will have index from list a as we have used a length variable.
# for i in range(1,5) # this means i will have index value as we have given a range between 1 and 5.
# *****************************************************************************************************************

#solution 2nd example using recursion
def add(numbers):
    if len(numbers)==1:
        return(numbers[0])
    else:
       return((numbers[0]) +add(numbers[1:]) ) # we have used here a recursive method to add the numbers in a list.

print(add([12,4,5,6,7,8]))


# 5. write a python program to solve the Fibonacci sequence using recursion.
# Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.

def fs(num):
    if num==1:
        return(0)
    elif num==2:
        return(1)
    else:
        return (fs(num-1)+fs(num-2))

print(fs(7))

# 0 1 1 2 3 5 8  # 7 places in fibonacci series.