
# three different Modules: all these modules have set of functions available in them.
# 1. Datetime
# 2. Random
# 3. Math

#Import the datetime module and display the current date
import datetime
x=datetime.datetime.now()
print(x)

y=datetime.datetime(1997,10,4)
print(y.strftime("%a")) #weekday short version
print(y.strftime("%A")) #weekday full version
print(y.strftime("%w")) #Weekday as a number 0-6, 0 is sunday
print(y.strftime("%d")) #Day of month 01-31
print(y.strftime("%b")) #Month name, short version
print(y.strftime("%B")) #Month name, full version
print(y.strftime("%m")) #Month as a number 01-12
print(y.strftime("%Y")) #Year, full version
print(y.strftime("%p")) #AM/PM
print(y.strftime("%y")) #Year, short version, without century (numeric 1997 : output : 97)
print(y.strftime("%Y")) #Year, full version

print(y.strftime("%H")) #Hours
print(y.strftime("%S")) #seconds
print(y.strftime("%M")) #Minutes
print(y.strftime("%Z")) #timezone



# /*****************************
#  -- Random Module
# *******************************/
# it picks any random value

import random
l=["Heads","Tails"]
x=random.randint(1,10)  # this function will pick a random integer value between  1 and 10. Each time a different value will be picked.
z=random.choice(l)
print(x)
print(z)


# /*****************************
#  -- Math Module
# *******************************/
# max,min, power , absolute, c, floor, square root etc

import math

x=max(13,67,45)
print("the maximum value is :",x)

x=min(13,67,45)
print("the minimum value is :",x)

# power , to calculate 2 raise to the power 4 , output is 16.
a=pow(2,4)
print(a)
#output : 16

# square root : we use exponent here.
b=math.sqrt(26)
print(b)

#absolute : to convert a negative value into a positive value.
c=abs(-12.345 )
print(c)
d=abs(-12.345*3 )
print(d)
# output : 12.345
#37.035000000000004

#ceil
k=math.ceil(2.4)
print(k) # output: 3,  it converts 2.4 to 3 , it gives next closest number.


#floor
k=math.floor(2.4)
print(k) # output:  2 , previous closet number