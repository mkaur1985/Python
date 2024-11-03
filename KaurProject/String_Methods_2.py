# use Ctrl+/ to comment out the parahgraph at once.

a="hello"
b="Hello123"
c="123456"
d="HELLO"
e=" "
f="Hello 123"
g="1.234"

# 11. isalnum : returns True if all characters in the string are alphanumeric.(alphabets and numbers only)
# print(a,"is alphanumeric ? :",a.isalnum())  #TRUE
# print(b,"is alphanumeric ? :",b.isalnum())  #TRUE
# print(c,"is alphanumeric ? :",c.isalnum())  #TRUE
# print(f,"is alphanumeric ? :",f.isalnum())  #this string has a space in it : FALSE (f="Hello 123") space is a string/special character
# print(g,"is alphanumeric ? :",g.isalnum())  # FALSE : This has decimal numbers in it.

# 12. isalpha : returns True if all characters in the string are alphabet.

# print(a,"is alpha ? :",a.isalpha())  #TRUE
# print(b,"is alpha ? :",b.isalpha())  #FALSE
# print(c,"is alpha ? :",c.isalpha())  #FALSE
# print(f,"is alpha ? :",f.isalpha())  #FALSE
# print(g,"is alpha ? :",g.isalpha())  #FALSE
# print(d,"is alpha ? :",d.isalpha())  #TRUE
# print(e,"is alpha ? :",e.isalpha())  #FALSE

# 13. isdecimal :  returns True if all characters in the string are decimals
a="hello"
b="Hello123"
c="123456"  #isdecimal returns True here
d="HELLO"
e=" "
f="Hello 123"
g="1.234"   #returns false here

# print(a,"is decimal ? :",a.isdecimal())  #FLASE
# print(b,"is decimal ? :",b.isdecimal())  #FALSE
# print(c,"is decimal ? :",c.isdecimal())  #TRUE The isdecimal() method returns True if all the characters are decimals (0-9).
# print(f,"is decimal ? :",f.isdecimal())  #FALSE
# print(g,"is decimal ? :",g.isdecimal())  #FALSE
# print(d,"is decimal ? :",d.isdecimal())  #FALSE
# print(e,"is decimal ? :",e.isdecimal())  #FALSE

# 14. isdigit : returns True if all characters in the string are digits.

# print(a,"is digit ? :",a.isdigit())  #FALSE
# print(b,"is digit ? :",b.isdigit())  #FALSE
# print(c,"is digit ? :",c.isdigit())  #TRUE , c="123456"
# print(f,"is digit ? :",f.isdigit())  #FALSE
# print(g,"is digit ? :",g.isdigit())  #FALSE
# print(d,"is digit ? :",d.isdigit())  #FALSE
# print(e,"is digit ? :",e.isdigit())  #FALSE

# 15. isnumeric : returns True if all characters in the string are numeric.

# print(a,"is numeric ? :",a.isnumeric())  #FALSE
# print(b,"is numeric ? :",b.isnumeric())  #FALSE
# print(c,"is numeric ? :",c.isnumeric())  #TRUE , c="123456"
# print(f,"is numeric ? :",f.isnumeric())  #FALSE
# print(g,"is numeric ? :",g.isnumeric())  #FALSE
# print(d,"is numeric ? :",d.isnumeric())  #FALSE
# print(e,"is numeric ? :",e.isnumeric())  #FALSE

# 16. islower : returns True if all characters in the string are in lowercase.

a="hello"  #True
b="Hello123"
c="123456"
d="HELLO"
e=" "
f="Hello 123"
g="1.234"

# print(a,"is lower ? :",a.islower())  #True
# print(b,"is lower ? :",b.islower())  #FALSE
# print(c,"is lower ? :",c.islower())  #FALSE
# print(f,"is lower ? :",f.islower())  #FALSE
# print(g,"is lower ? :",g.islower())  #FALSE
# print(d,"is lower ? :",d.islower())  #FALSE
# print(e,"is lower ? :",e.islower())  #FALSE


# 17. isupper : returns True if all characters in the string are uppercase.
#
# print(a,"is upper ? :",a.isupper())  #FALSE
# print(b,"is upper ? :",b.isupper())  #FALSE
# print(c,"is upper ? :",c.isupper())  #FALSE
# print(f,"is upper ? :",f.isupper())  #FALSE
# print(g,"is upper ? :",g.isupper())  #FALSE
# print(d,"is upper ? :",d.isupper())  #TRUE
# print(e,"is upper ? :",e.isupper())  #FALSE

# 18. isspace : returns True if all characters in string are whitespaces.
a="hello"  #True
b="Hello123"
c="123456"
d="HELLO"
e=" "
f="Hello 123"
g="1.234"
#
# print(a,"is space ? :",a.isspace())  #FALSE
# print(b,"is space ? :",b.isspace())  #FALSE
# print(c,"is space ? :",c.isspace())  #FALSE
# print(f,"is space ? :",f.isspace())  #FALSE
# print(g,"is space ? :",g.isspace())  #FALSE
# print(d,"is space ? :",d.isspace())  #FALSE
# print(e,"is space ? :",e.isspace())  #TRUE

# 19. istitle : returns True if all words in a text start with a upper case letter.(Symbols and numbers are ignored)

#The istitle() method returns True (if all words in a text start with a upper case letter),
# AND the rest of the word are lower case letters, otherwise False. Symbols and numbers are ignored.

print(a,"is title ? :",a.istitle())  #FALSE
print(b,"is title ? :",b.istitle())  #True
print(c,"is title ? :",c.istitle())  #FALSE
print(f,"is title ? :",f.istitle())  #True
print(g,"is title ? :",g.istitle())  #FALSE
print(d,"is title ? :",d.istitle())  #FALSE
print(e,"is title ? :",e.istitle())  #TRUE
