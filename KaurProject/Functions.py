
# /*************************
# -- Functions
# **************************/

def hello():
    print("Hello World function sample !! ")

hello() # calling the function here.

# 2. Example:
def addd():
    x=10
    y=30
    z=x+y
    print(z)

addd() #calling add()
# output: 40

# /*******************************
# --Parameters and Arguments
# *********************************/

#Parameters: are the variables written inside the parentheses with the name of function.
#Arguments: are the values passed to the parameters while calling the function.

# example: 1
def addition(x,y): # x,y are paremeters.
    z=x+y
    print(z)
addition(5,6)  # 5,6 are arguments
#ouput: 11

# example : 2
def rect(length,width):
    print("area of rectangle is : ",length*width)
rect(10,23)  # function will do its work as many times we call it using multiple calling statements.
rect(12,14)


#
# /************************************
# Arbitrary Arguments, *args
# **************************************/

 # 1. When we don't know how many arguments will be passed during function call then we put a * in front of parameter assign in the function definition.
 # 2. The calling statement will look like tuple of arguments.
 # 3. The value can be accessed as paremeter[index] in the body of the function.

def hello(*name): # use * in front of the parameter.
    print("Hello my name is : ", name[2] )  #access the values with index.
hello("John" ,"lisa","Mary","Sam")  # looks like a tuple of arguments.



# /************************************
# Return statement and Recursion in Python
# **************************************/

#example 1:
def hello():
    return ("Hello world !!") # return keyword stores the value of the function and exits the function.

print(hello()) # if we don't use print here, nothing will be displayed in the output.

#Example 2:
def addition(a,b):
    return ("the addition of 2 numbers is: ",a+b)

print(addition(3,6))
#output: ('the addition of 2 numbers is: ', 9)

# ----------------------------------------------------------------------------
#   ---  Recursion(recursive) : which means a defined function can call itself.
# ------------------------------------------------------------------------------

# Recursion in most commonly used mathematical and programming concept
# In simple words, recursion means functions can call itself, giving us a benefit of looping through data in order to get a result.
# it's helpful when we work with series of numbers etc.
# function call is written within the function , with or without return statement.

# def hello():
#     print("Hello")
#     return hello() # this will make the function go in loop
# hello()  # function calling statement

#Output: Hello  , this will be printed multiple times.
# [Previous line repeated 996 more times] , python has 996 limit for recursive function, once it reached its limit the loop will stop.
# RecursionError: maximum recursion depth exceeded.

#--------------------------------------
# factorial of a number using recursion:
#--------------------------------------
#factorial of 3 : 3*2*1 =6
#factorial of 4 : 4*3*2*1 =24

def fact(n):
    print(n)
    if n==1:
        return 1
    else:

        return (n*fact(n-1))  # this statement will create the recursion(the function will call itself again and again)
print(fact(5)) # calling statement

#output: 120


#Another Example:
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)  # function is being called here itself unless the if condition is true.
    print(result)
  else:
    result = 0
  return result

tri_recursion(6)

#output:
# 1
# 3
# 6
# 10
# 15
# 21


# /*************************************************
#  Lambda function in python (temporary function)
# ***************************************************/

#example 1:
a=lambda b: b*5  # lambda b:  lambda is a function + b is parameter :  #B*5 is an expression
print(a(4))
#output: 20

#example 2
x = lambda a, b : a * b
print(x(5, 6))
#output:30

# example 3
x=lambda b,c,d : b+c+d
print(x(2,3,4))
#output: 9

# example 4
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))  # here we are calling lambda function anonymously.
#output 33
