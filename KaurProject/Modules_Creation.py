
import demo01   # here we import the user defined module.

a=demo01.add(2,3) # calling the user defined module here.
print(a) # printing the value of the module.
#output: 5

# creating alias name of module.
import demo01 as d  #Created an alias here and we can use the alias name instead of full name of the module.
a=d.add(2,3) # calling the user defined module here.
print(a)
#output: 5

b=d.employee.items()
print(b)
b=d.employee["Name"]
print(b)
c=d.employee.get("age")
print(c)