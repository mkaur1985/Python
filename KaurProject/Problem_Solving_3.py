
#Pattern 1
"""
for i in range(1,6):
    print("""""")
    for j in range(1,6):
        print(j,end=" ")


# Pattern 2
        for i in range(1, 6):
            print("""""")
            for j in range(1, i+1):
                print(j, end=" ")
                """

# Pattern 3
for i in range(1, 6):   #rows
    print("""""")
    for j in range(i, i+i ): #columns
      print(i, end=" ")   #updated value here from J to i.

# Pattern 4

for i in range(1,6):   #rows
    print("""""")
    for j in range(6, i,-1 ): #columns
        print(i, end=" ")

# Pattern 5 Christmas tree

for i in range(1,6):   #rows
    #print(""" """)
    for j in range(6, i,-1 ): #columns
        #print(" ", end=" ")
        print(""" """)
        for k in range(i):
            print("*", end=" ")

# Pattern 6
for i in range(1,6):   #rows
    print("""""")
    for j in range(i, 0,-1 ): #columns
        print(j, end=" ")


#Pattern 7
for i in range(1,6):
    print("""""")
    for j in range(i,i+i):
        print("*",end=" ")

for k in range(1, 6):
    print("""""")
    for z in range(6, k, -1):
        print("*", end=" ")


list=[False,True,"2",3,4]
b=0  in list
print(b)

