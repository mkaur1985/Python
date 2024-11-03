"""
These operators are used to compare the binary numbers.
There are 2 binary numbers 1 and 0.   Binary means 2.
To convert a number into binary we bin() in python.
print(bin(10))

0&0=0
0&1=0
1&0=0
1&1=1

"""
# 1. Add operator on binary numbers.
print(bin(10))  # 1010 is the binary conversion of 10
print(bin(15))  # 1111 is the binary conversion of 15

a = 10
b = 8
print(a & b) # displays 8 because when we convert 10 and 8 into binary and perform "and" operation on it give answer as 8 in binary.

print("Binary conversion of 10 is: ", bin(10))
print("Binary conversion of 8 is: ", bin(8))
print("Binary conversion of performing and on 10&8  is: ", bin(a & b))

# 2. OR operator on binary number.
a = 10
b = 8
print(a | b) # displays 8 because when we convert 10 and 8 into binary and perform "and" operation on it give answer as 8 in binary.

print("Binary conversion of 10 is: ", bin(10))
print("Binary conversion of 8 is: ", bin(8))
print("Binary conversion of performing and on 10|8  is: ", bin(a | b))

# 3.Xor when it 1^1 or 0^0 : output is 0  , when it gets 1^0 or 0^1 : output is 1

a = 10
b = 8
print(a ^ b) # displays 8 because when we convert 10 and 8 into binary and perform "and" operation on it give answer as 8 in binary.

print("Binary conversion of 10 is: ", bin(10))
print("Binary conversion of 8 is: ", bin(8))
print("Binary conversion of performing and on 10|8  is: ", bin(a ^ b))  #0010 output

#4. zero fill right shift
# 20>>2
print("Binary conversion of 20 is: ", bin(20))
print("Binary conversion of 2 is: ", bin(2))
print(bin(20>>2))

#5. zero fill left shift
# 20<<2
print("Binary conversion of 20 is: ", bin(20))
print("Binary conversion of 2 is: ", bin(2))
print(bin(20<<2))














