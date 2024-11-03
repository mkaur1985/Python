"""
Identity operators are used to compare items to see if they are the same object with the same memory address.

i) IS
ii) IS NOT

two variables : having same data type
storing similar value
storing value into same Id etc.
"""

a=1234
b="1234"
print(a is b)  # returns false because we compared number with string

a=1234
b=1234
print(a is b) # returns true because we compared number with number
print(a is not b) # returns false because we said datatype of a and b is not same(value and data type both are same).