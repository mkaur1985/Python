# Syntax
# while [condition]
# body of while
# Increment
from selectors import SelectSelector

#  1. While loop statement.
i=1
while i < 6:
    print(i)
    i=i+1


# 2. break statement to bring the control out of the loop statement.

i = 1
while i < 6:
    print(i)
    if i==3:
        break   # control will come outside the loop.
    i = i + 1


#3. With the continue statement we can stop the current iteration, and continue with the next:
#i = 1
#while (i < 6):
#    print(i)
#    if(i==3):
#        continue   # to continue with next iteration.
#    i = i + 1     # if we put the increment statement her it will keep executing in loop (infinite loop)

# Infinite Loop : An infinite loop is a sequence of instructions in a computer program which loops endlessly, either due to the loop having no terminating condition, having one that can never be met, or one that causes the loop to start over.


# 3 .Continue with good syntax:
i = 0
while i < 6:   # do not use backets here , otherwise it will not run properly.
  i += 1
  if i == 3:
    continue
  print(i)

#output:
#Remember 3 will be missing here

#  1
#  2
#  4
#  5
#  6


#4 Else statement with While , to print a statement when a condition is false.

i=1
while i < 6:
    print(i)
    i=i+1
else:
    print("the condition is false: ")


# While true statement:

while True:
    num1=int(input("Enter a num1: "))
    num2 = int(input("Enter a num2: "))
    print("sum of both numbers is: ",num1+num2)
    repeat=input("do you want to stop the program yes/no: ")
    if repeat=="yes":
        break







