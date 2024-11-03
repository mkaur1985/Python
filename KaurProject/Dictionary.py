# 1. print the dictionary
employee_data={"Name":"John","age":24,"gender":"male"}
print(employee_data)

# Output:
# {'Name': 'John', 'age': 24, 'gender': 'male'}

# 2. Print the value of a particular key.
print(employee_data["age"]) # if we want to print only the age , so we put a key object here.
# output: 24

# /********************************
#  Iterations in dictionaries:
# *********************************/

# 1. Iterations can be between keys and values ,or between only key or in between only values.

student={"name":"John","class":"6th","roll_no":23}

#printing all the key names one by one
for i in student:
    print(i) #this will give us the key's.

#output:
# name
# class
# roll_no

# 2. printing all the value names one by one
for i in student:
    print(student[i])

#output:
# John
# 6th
# 23

# 3. using value function:
for i in student.values() :
    print(i)

#Output:
#John
#6th
#23

for i in student :
    x=student.values()
    print(x)

# output:
# dict_values(['John', '6th', 23])
# dict_values(['John', '6th', 23])
# dict_values(['John', '6th', 23])

# 4. to get both keys and values at the same time.

for x,y in student.items():
    print(x,":",y )

#Output:
# name : John
# class : 6th
# roll_no : 23

# /***************************************
# -- Nested Dictionaries
# ****************************************/

# A dictionary within a dictionary is called a nested (dictionary).
#There will be major key and then it will have its owen minor keys and values.

employee= {1:{"name":"John","age":20,"gender" :"male" } ,
	       2:{"name":"Lisa","age":24, "gender":"M"} ,
           3:{"name":"Paula","age":25, "gender":"female"} }
print(employee)
print(employee[2])   #provides complete dictionary for key 2
print(employee[2]["age"]) # provides only age value for dictionary 2

#output:
# {1: {'name': 'John', 'age': 20, 'gender': 'male'}, 2: {'name': 'Lisa', 'age': 24, 'gender': 'M'}, 3: {'name': 'Paula', 'age': 25, 'gender': 'female'}}
# {'name': 'Lisa', 'age': 24, 'gender': 'M'}
# 24















