# /***************************
#  STRINGS Functions PART 3
# *****************************/
#
# # 1. endswith() : Returns true if string ends with a specified value.
# a="Harry Potter"
# print(a.endswith("r"))  #string here ends with "r" so it will return True.
# print(a.endswith("t",6,9)) # we can also define the start and end position of the string
#
# # 2. startswith() : Returns True if the string starts with a specified value.
# a="Harry Potter"
# print(a.startswith("H"))  #return true because the string here starts with letter H
# print(a.startswith("P",6,9))
# print(a.startswith("a"))  #returns false
#
# # 3. swapcase() - swaps or converts (The lower case into capital) and (capital case into lower case)
# a="Harry Potter"
# print(a.swapcase())  # Output: hARRY pOTTER
#
# # 4. strip() - Returns a trimmed version of a string. (by default strings are removed)
#
# a="      Harry Potter      "                   #output: Harry Potter
# b="*****Harry Potter   ............********"   #output: Harry Potter
# print(a.strip()) # bydefault it removes the string
# print(b.strip("*,.,"))
#
# #5.split()	Splits the string at the specified separator, and returns a list
#
# a="#OOFD#BRB#OMW#TB"
# print(a.split("#"))  #output : comes in the form of a list    ['', 'OOFD', 'BRB', 'OMW', 'TB']
# b="hello. My name is John. I am 21 years old"
# print(b.split(".")) #output : comes in the form of a list  ['hello', ' My name is John', ' I am 21 years old']

# 6. ljust() - Return left justified version of the string.

# SYNTAX:
# string.ljust(length, character)

# Parameter	Description
# length		Required. The length of the returned string
# character	Optional. A character to fill the missing space (to the right of the string). Default is " " (space).

#Lenght of string is 12 ,total lenght given in ljust(20) 20, so rest of the 8 characters are filled with *.
#this process starts from left to justift the string as left justified..

a="Harry Potter"
x=a.ljust(20,"*")  # we added here 20 spaces , we used * character instead of spaces.
print(a.ljust(20,"*"))
print(x," This is my favorite movies")
# output:
#Harry Potter********
# Harry Potter********  This is my favorite movies


# 7. rjust() - Returns the right justified version of the string.
a="Harry Potter"
x=a.rjust(20,"*")  # we added here 20 spaces , we used * character instead of spaces.
print(x," This is my favorite movies")
# Output:
# ********Harry Potter  This is my favorite movies

#Lenght of string is 12 ,total lenght given in ljust(20) 20, so rest of the 8 characters are filled with *.
#this process starts from right to justift the string as right justified.

#8. Replace: A string is replaced with a specified value.
a="My name is John"
print(a)
print(a.replace("John","Lisa"))  # we want to replace John with Lisa

#output:
#My name is Lisa

#9. rindex(): Searches the string for a specified value and returns the last position of where it was found
#Basically returns the index of the word/string.
a ="Harry Potter and Gods of the earth"
print(a.rindex("Gods"))   #returns 17
print(a.rindex("Harry"))  #returns 0

#10. rfind() :  Searches the string for a specified value and returns the last position of where it was found
#rfind() and rindex() are same.
a ="Harry Potter and Gods of the earth"
print(a.rfind("Gods"))   #returns 17
print(a.rfind("Harry"))  #returns 0

b="shipi shipi shapa shapa"
print(b.rfind("pi",3,12)) #output is 0 and 9 position
