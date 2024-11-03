
# 1. Write a program to find max and min in a set.

a={12,56,34,8,90,1,57}
maximum = max(a)
minimum =min(a)
print("the maximum value in given set is: ",maximum)
print("the minimum value in given set is: ",minimum)

# Output:
# the maximum value in given set is:  90
# the minimum value in given set is:  1

# 2. Write a program to find common elements in three lists using sets.
#intersection()
a=[1,5,6,8,2]
b=[4,5,6,7]
c=[1,9,6,2,5]

#Python's bitwise AND operator is represented by the ampersand symbol (&). It compares the binary representation of two numbers and returns a new number, with each bit set to 1 only if they're the same in both operands. Otherwise, it returns 0.

# (i) Using bitwise and operator
print(set(a) & set(b) & set(c)) # we have used here and operator (bitwise and operator)
#output: common elements in set a,b,c are {5, 6}

# (ii) using intersection() : # first convert lists into set.
a=set(a)
b=set(b)
c=set(c)
x=a.intersection(b,c)
print(x)
#output: common elements in set a,b,c are {5, 6}

# 3. Write a program to find difference between two sets.
#difference() , will provide uncommon values from set A
a={1,5,6,8,2}
b={1,9,6,2,5}
x=a.difference(b)
print(x)  #output {8}

# 4. Write a python program to remove an item from a set if it is present in the set.
#remove() discard()
a={1,5,6,8,2}
a.remove(5)
print(a) #output: {1, 2, 6, 8}


# 5. Write a python program to check if a set is a subset of another set.
#issubset()
a={1,2,5}  #child
b={1,9,6,2,5} #parent
x=a.issubset(b)
print(x) #output: True , a is child of b

x=b.issuperset(a) # b is parent of a
print(x) #output: True