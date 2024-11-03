

# ***********************************
# Example using list comprehension
# *************************************/


l1=[30,40,50,60]
l2=[]
for i in l1:
    if i > 45:   #  put condition here because we don't want to copy all values.
        l2.append(i)
print(l2,"\n",l1) #gives same out for both the lists

#output:
 # l2 [50, 60]
 #l1 [30, 40, 50, 60]

# With list comprehension you can do all that with only one line of code:

#*************************
#syntax: list comprehension
#*************************
l1=[30,40,50,60,70,80]
l3=[i for i in l1]  # means obtain i using a for loop.
print(l3)

# output:
# [30, 40, 50, 60, 70, 80]

# with if condition
l1=[30,40,50,60,70,80,90]
newlist=[]
newlist=[i for i in l1 if i > 45 ]
print(newlist)

#output:
#[50, 60, 70, 80, 90]

# newlist=[x for x in fruits if x == "apple"]
# newlist=[x for x in fruits if x != "apple"]

