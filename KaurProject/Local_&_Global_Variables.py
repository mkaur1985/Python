

#/************************************
# --Local and Global Variables.
# **************************************/

#Variable: is a container or a placeholder that can be used for storing a value.
#Local variables: are restricted to only one block of code and cannot be changed throughout the program.
#Global variables : are not restricted to one block of code and they can be changed throughout the program.
#Global variable can be defined inside or outside  a function. once declare as global it can updated/accessed throughout the program.

# Syntax for global variable:

#     global variable name
#    eg : global x

# Example:
x=24 # local variable  # this is a local variable as well
print("first variable x is   :" ,x)
def hello():
    global x # x is now a global variable
    x=25 # local variable
    return x
print("Local variable has value: ",hello())
print("Global variable: ",x)