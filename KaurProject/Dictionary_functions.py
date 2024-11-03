
# /********************************
#  -- Dictionary functions part (1)
# **********************************/

student={"name":"John","class":"6th","roll_no":23}
#1. get
# print(student.get("name")) #helps in fecting the value of a key.
# #output: John
#
# #2. items
# a=student.items() # to get both keys and items in the form of a tuple.
# print(a)
# #output: dict_items([('name', 'John'), ('class', '6th'), ('roll_no', 23)])
#
# #3. keys
# a=student.keys() # to get keys only.
# print(a)
# #output: dict_keys(['name', 'class', 'roll_no'])
#
# #4. values
# a=student.values() # to get values only.
# print(a)
# #output: dict_values(['John', '6th', 23])
#
# #5. copy , this function copies the dictionary another variable/dictionary.
# student={"name":"John","class":"6th","roll_no":23}
# print("Original : ",student)
# b=student.copy() # to get values only.
# print("Copied : ",b)

# output:
# Original :  {'name': 'John', 'class': '6th', 'roll_no': 23}
# Copied :  {'name': 'John', 'class': '6th', 'roll_no': 23}


# /********************************
#  -- Dictionary functions part (2)
# **********************************/

#student={"name" : "John", "class":"6th","roll_no":23}

# 1. setdefault

#The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key(or append in the end of the string), with the specified value, see example #below.

#syntax
#dictionary.setdefault(keyname, value)

# x=student.setdefault("name","preet") # it will keep the original value John , that was assigned in the dictionary.
# print(x)
# x1=student.setdefault("lastname","Singh")
# print(x1)
# print(student)

# 2. update , it updates the dictionary , by inserting specified items to dictionary. he update() method inserts the specified items to the dictionary.

student={"name" : "John", "class":"6th","roll_no":23}
print(student)
x=student.update({"age":23})
print(x)
print(student)

#Syntax:
#1. car.update({"color": "White"})
#2. dictionary.update(iterable)

#for list remove(): removes specified item, If there are more than one item with the specified value, the remove() method removes the first occurrence
#for list The pop() method removes the specified index. eg: pop(1)
# # 3. pop : The pop() method removes the specified item from the dictionary.
x=student.pop("age")
print(x)
print(student)


# # 4. popitem : Remove the last item from the dictionary:
#
print(student)
x=student.popitem()
print(x)
print(student)

#Output:
# {'name': 'John', 'class': '6th', 'roll_no': 23}
# ('roll_no', 23)
# {'name': 'John', 'class': '6th'}
#


# # 5. clear : Remove all elements from the car list:

print(student)
x=student.clear()
print(x)
print(student)

#output:
# {'name': 'John', 'class': '6th'}
# None
# {}




