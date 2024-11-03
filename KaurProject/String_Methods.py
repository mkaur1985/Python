
# String
a = "Harry Potter and The Goblet of fire"
print(a)

# 2. define the length of the string.
a = "Harry Potter and The Goblet of fire"
print(len(a))

# 3. To count the number of times a character is appearing in a string (Capital O and small o will be counted separately)
print(a.count("H"))

#4. to convert each letter into uppercase
print(a.upper())

#5. to convert each letter into lowercase
print(a.lower())

#6. to convert each letter into lowercase
print(a.casefold())

#7. to find index of any character.
print(a.index("o"))
print(a.index("o",15,24))   # we find to particual index so we give the start location and end location)

#8. to find index of any character.
print(a.find("o"))
print(a.find("o",15,34))   # we find to particual index so we give the start location and end location)

#9. To convert the first letter of string to a capital Letter.
print(a.capitalize())

#10. To write format/values in  a string.
name="John"
age="23"
b="My name is: {}  My age is {}"
print(b.format(name,age))

#11. It fills the characters and centralizes a string.
print(name.center(20))
print(name.center(20,"*")) # total 20 spaces , 4 spaces are occupied by John , rest 8 spaces on both sides represented by a star sign but that is optional.




