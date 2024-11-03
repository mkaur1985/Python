

A=["Ross","Rachel","Monica","Joe","Chandler"]

# 1. write a program to swap first and forth element
print(A)
A[0],A[3]=A[3],A[0]
print(A)

# 2. write a program to add a new value at second position
A.insert(1,"Phoebe")
print(A)

# 3. write a program to delete a value from 3rd position.
#when we don't want to remove using name then use pop()
A.pop(2)
print(A)


#****************************************************************************

B=[13,7,12,10]

# 1.write a program to multiply all the numbers in the list

multi=1
for i in B:
    multi=multi*i
print(multi)

# 2. write a program to get the largest number from the list.

B.sort()
print(B)
print("the largest value in the list is",B[-1])
print("the smallest value in the list is",B[0])

# 3. write a program to get the smallest number from the list.

B.sort()
print(B)
print("the smallest value in the list is",B[0])
