
""" Questions and answers """
# Q1. print name , age and address in different lines.
name="Abacus"
age=23
address="654 lake street"
print(name)
print(age)
print(address)


# Q2. swap (interchange) two variables. --> Method 1. can be using temporary variable(put x=20 and y=10)

x=10
y=20
print("original value of x is: ", x)
print("original value of y is: ",y)
temp=x
x=y
y=temp
print("swapped value of x is: ", x)
print("swapped value of y is: ", y)

# Method 2.
a=30
b=40
print("original value of a is: ", a)
print("original value of b is: ",b)
a,b=b,a  # simply write using a comma
print("swapped value of a is: ", a)
print("swapped value of b is: ", b)

# Q3. write a program to convert float into  integer

z=24.56
print("Original value is",(z))
print("original data type is: ",type(z))
z=int(z)
print("After the type conversion the value is:",(z))
print("Converted data type is: ", type(z))

# Q.4 Write a program to take data from a student, ID card then print in different lines. (use input())

print("*** Student Identity card ***")
name =input("enter name of student: ")
age =int(input("enter age of student: "))
grade=input("enter grade of student: ")
email=input("enter email of student: ")
ph_no=input("enter phone number of student: ")
print("*** Student Identity card ***")
print(name)
print(age)
print(grade)
print(email)
print(ph_no)

# Q.5 write a program to take a user input as an integer value then convert it to float.

ab=int(input("Enter a number: "))
print("Checking the data type ",type(ab))
ab=float(ab)
print("Checking the data type after conversion ",type(ab))



