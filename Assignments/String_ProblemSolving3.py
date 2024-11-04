

# /**************************************
#  Problem solving 3
# ***************************************/

# 1. Take an input from a user as a string then,reverse it.
# a=input("Enter a string: ")
# print(a[::-1])

# 2. write a program to check if a string contains only digits.

a="12345678"
b="abc123"
c="abc"
print(a.isalnum()) # number and alphabet
print(b.isalnum())
print(c.isalpha()) # only alphabet
print(a.isdigit())

# 3. Write a program to check if a string is palindrome.
# a=input("Enter a string : ")
# b=a[::-1]
# print(a)
# print(b)
# if(a==b):
#     print(a,"is a palindrome")
# else:
#     print(a,"is not a palindrome")

# 4. write a program to find number of vowels in a string.
#
# a=input("Enter a string to check vowels : ")
# vowels=0
# for i in a:
#     if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" ):
#         vowels=vowels+1
# print("the number of vowels are : ", vowels)


# 5. write a program to check if every word in a string begins with a capital letter.

#a=input("Enter a string to check the title : ")
# b=a.title()
# print(a)
# print(b)
# if(a==b):
#     print(a," - Each word in the string begins with capital letter")
# else:
#     print(a," - Each word in string doesn't begin with capital letter")

#Easy Method
a=input("Enter a string to check the title : ")
print(a.istitle()) #this function return true or false.