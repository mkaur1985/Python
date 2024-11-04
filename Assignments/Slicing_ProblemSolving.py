# /********************************************
# -- Problem Solving
# **********************************************/

a = " why fit in , when you are Born to Stand Out!"

# 1. write a program to find the length of the following string.
print("Length of the string is: ",len(a))

# 2. write a program to check how many times alphabet O is occurring.

print("String o is occurring : ",a.count("o") ,"times")
print("String O is occurring : ",a.count("O") ,"times")

# 3. write a program to convert whole string into upper and lowercase.
print(a.upper())
print(a.lower())

# 4. Write a program to convert whole string into title.
print(a.title())  #first letter of each word gets converted into capital

# 5. Write a program to find the index number of "fit in" .
print(a.find("fit in",0,11))
print(a.index("fit in",0,11))
print(a[5:11])  # using (slicing/cut down) find the "fit in" from a string.

