
# ***************************** For Loop **************************************************** #

# for statement without range function.
fruits =["apple","bannana","mango","orange"]
for x in fruits:
    print(x)

# for statement with range function.
for i in range(1,6):
    print("Hello world !!!")

# we have used starting from 1, ending at 6 and gap of 2 numbers. It will print odd number.
    for i in range(1, 6,2):
        print(i)

# Table multiplication

print("*******************Multiplication Table for 7 ***************")
n=7
for i in range(1,11):
    print(n,"*",i,"=", n*i)

# pass statement is used with empty loops to avoid errors.

for i in [0,1,2,3]:
     pass