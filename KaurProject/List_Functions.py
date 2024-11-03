

# /*************************************
#   List Functions
# **************************************/
# 1. to find the length of a list

a=["Thor","Hulk","Ironman","Captain America"]
print(len(a))

# 2. to count an occurrence of a particular element
#
# a=["Thor","Hulk","Ironman","Captain America","Hulk"]
# print(a.count("Hulk"))

# 3. to add to the list
# append() is used to add a value to the end/last of the list.

# a.append("Bheem")
# print(a)
#output: ['Thor', 'Hulk', 'Ironman', 'Captain America', 'Hulk', 'Bheem']

# 4. to add to a specific location
# insert method is used to insert a value at a particular position. We first specify the index number and then the actual new value.
#
# a.insert(1,"vision")
# print(a)

# 5. to remove from a list
a.remove("Hulk")  # to remove a value from list we use remove() , if there is multiple occurance of the vlaue then remove() removes the very first occurrence from the list
print(a)

# 6. to remove from a certain location.
# when we don't know the value but we know only location eg index 1

print(a.pop(1)) # removes value from index 1
print(a)

# *******************************************************************************************************************

# /*****************************
#  List Functions - Part2
# *******************************/

a=["Thor","Hulk","Ironman","Captain America"]

# to create a copy of a list
b=a.copy()
print(b)

# to access an element(or access an index)
print(a.index("Ironman"))

# to extend the list
c=["vision","spiderman"]
a.extend(c)
print(a)

# to reverse the list
print(a)
a.reverse()
print(a)

# to sort the list (it will sort in ascending order of alphabets or numbers)
a.sort()
print(a)

d=[3,56,7,8,2,4,6,8,0,1]
d.sort()
print(d)

# to clear all the data from the list. (it will empty the list)
a.clear()
print(a)
#output:  []

