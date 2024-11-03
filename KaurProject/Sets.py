
#1. there is no indexing and no element is ordered. So everytime we run this script it will give us different output.
a={"Ironman","Hulk","Thor","Captain America"}
print(a)
#output: {'Hulk', 'Ironman', 'Thor', 'Captain America'}
# Ran second time: {'Thor', 'Hulk', 'Captain America', 'Ironman'}

#2. Let's check the type of variable a:
print(type(a))
#output: <class 'set'>

#3. Loop
for i in a:
    print(i)  # there are no indexing hence it will print the value.


# /******************************
#  -- Set Methods/functions - 1
# ********************************/

#add
#pop
#remove
#discard
#copy

a={"Ironman","Hulk","Thor","Captain America"}

# add
a.add("Spiderman")  # it adds at any random number , because there is no indexing.
print(a)

#output: {'Ironman', 'Captain America', 'Spiderman', 'Thor', 'Hulk'}
# Ran second time: {'Spiderman', 'Ironman', 'Hulk', 'Thor', 'Captain America'}

# pop : it will remove a random value from the set eash time we run the query.
# a.pop()
# print(a)

#Output:
#Before pop (): {'Captain America', 'Hulk', 'Thor', 'Spiderman', 'Ironman'}
#After pop() : {'Hulk', 'Thor', 'Spiderman', 'Ironman'}

# remove
a={"Ironman","Hulk","Thor","Captain America"}
a.remove("Thor") # to remove a specific value.
print(a)
#output: {'Captain America', 'Ironman', 'Hulk'}

# discard : is simialr to remove, it removes a particular value from the set.
a.discard("Hulk")
print(a)

# copy : to copy a set into another set.
a={"Ironman","Hulk","Thor","Captain America"}
print("The original set",a)
b=a.copy()
print("After copying the set",b)

# /********************************
# -- set functions - Part 2
# **********************************/

#isdisjoint
#issubset
#issuperset
#update
#clear

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor"}

#Return True if no items in set B is present in set A

# 1.isdisjoint  : this method works on two or more sets. It checks for the elements of set b , if they belong to set a or not. If they don't belong it returns True else False
print(a.isdisjoint(b))
#output is : True , because elements of set B doesn't belong to set a
print(a.isdisjoint(c))
#output is : False, because elements of set B belong to set a

# 2.issubset
#Return True if all items set X are present in set Y:
#x = {"a", "b", "c"}
#y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y) #True

#Return True if all items in set c are present in set a:
#The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
print(c.issubset(a) ) , #means c is a child of a
#Output: True
print(c.issubset(b))
#output: False

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor"}

# 3.issuperset
#Return True if all items set y are present in set x:
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = y.issuperset(x) #True
#Return True if all items set A are present in set C:
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False.

print(a.issuperset(c)) # means A is a parent of C
#output: True

# 4.update
#Insert the items from set y into set x:
#If an item is present in both sets, only one appearance of this item will be present in the updated set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) # here we want to update set x with the values of set y
print(x)
#output: {'apple', 'cherry', 'banana', 'microsoft', 'google'} # any duplicate value will display only once because a set has unique elements only.

#or Use |= as a shortcut instead of update():
x |= y
print(x)

# 5.clear # removes all items from a set.
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#output: set() , means the set is empty.


# /*****************************
# Set functions - Part 3
# *******************************/

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor","Spiderman"}

# Union : RETURNS ALL VALUES.
# Difference : UNCOMMON VALUES FROM SET A ((creates new set))
# Difference Update : (updates existing set)
# Intersection : ONLY COMMON VALUES FROM A and B (creates new set)
# Intersection Update : (updates existing set)
# Symmetric Difference : UNCOMMON VALUES from A and B (creates new set)
# Summetric Difference update: (updates existing set)

# 1. Union : (all values from A and B + common values from both sets)
#Return a set that contains all items from both sets, duplicates are excluded:
#You can specify as many sets you want, separated by commas. It does not have to be a set, it can be any iterable object.
# If an item is present in more than one set, the result will contain only one appearance of this item.

# Example: RETURNS ALL VALUES.
# A={1,2,3}
# b={3,4,5}
# C={1,2,3,4,5}  is the output ,all elements from A and B + common elements - duplicate values appears only once.


#Syntax: set.union(set1, set2...)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
#output: {'cherry', 'banana', 'apple', 'google', 'microsoft'}


a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor","Spiderman"}

print(a.union(c))
#output: {'Ironman', 'Spiderman', 'Captain America', 'Hulk', 'Thor'}


# 2. Difference : Return a set that contains the items that only exist in set A, and not in set B (it will also exclude the common elements.):
#It returns a new set.
# Example: ONLY UNCOMMON VALUES FROM SET A
# A={1,2,3}
# b={3,4,5}
# C={1,2}  is the output

x=a.difference(c)
print(x) # created a new set x
#output: {'Ironman', 'Captain America'} # returns items from only set A


# 3. Difference Update : The difference_update() method removes the items that exist in both sets.
# it will not return new set ,rather it updates the existing set.
a.difference_update(c)
print(a)
output: {'Ironman', 'Captain America'}

#------------------------------------------
a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor","Spiderman"}
#-----------------------------------------------

# 4. Intersection : returns only the common elements in both sets.
# it returns a new set
# Example:  ONLY COMMON VALUES
# A={1,2,3}
# b={3,4,5}
# C={3} 3, is the output
#
# x=(a.intersection(c))
# print(x)
#output: {'Thor', 'Hulk'}

# 5. Intersection Update :  it updates the same set and returns the common values of all sets.
# a.intersection_update(c)
# print(a)
#output: {'Thor', 'Hulk'}

# 6. Symmetric Difference: returns uncommon elements of set A and set B , it completely ignores the common values from both the sets.
#returns a new set
# Example: ONLY UNCOMMON VALUES /IGNORE COMMON
# A={1,2,3}
# b={3,4,5}
# C={1,2,4,5} # this will ignore common values from both the sets.

x=a.symmetric_difference(c)
print(x)
#output: {'Captain America', 'Spiderman', 'Ironman'}

# 7. symmetric Difference update: returns uncommon elements of set A and set B , ignores common elements from both sets.
# updates existing set.
print(a.symmetric_difference(c))
#output : {'Ironman', 'Spiderman', 'Captain America'}














