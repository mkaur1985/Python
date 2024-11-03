
# 1. Slicing of a string: to cut down the string within a starting and ending point.
a="Harry Potter and the Goblet of Fire"
print(a)
print(a[0:5]) # print harry
print(a[6:12]) #print potter

print(a[:5]) # No need to specify the begining address as it begins with 0 as a default value.
print(a[-4:]) #reading from right side or from the end of the string.

# 2. slicing of a numeric string.
b="0123456789"
print(b[::2]) # here we are not defining the starting or the end value but we want to define the gap of 2 here
print(b[:6:2]) # starting point not given(default 0), but end is given with a gap of 2 numbers.
print(b[:6:3])

# 3. Reverse order :
print(b[::-1]) # to print in reverse order. Output: 9876543210
print(b[6::-1]) # reverse order again but from 6 to 0 , use -1 for reverse order.