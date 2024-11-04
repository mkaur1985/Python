
# /*************************************
#   Problem solving
# **************************************/
#
# 1. Write a python program to sort a dictionary by value.
# a={"a":12,"b":23,"c":6,"d":91,"e":45}
# a=sorted(a.values())
# print("dictionary sorted by values", a)
# # output: [6, 12, 23, 45, 91]
#
# # sort by keys
# a={"a":12,"b":23,"c":6,"d":91,"e":45}
# a=sorted(a.keys())
# print("dictionary sorted by keys",a)
#output: ['a', 'b', 'c', 'd', 'e']


# 2. Write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.
a={}
for i in range(1,16):
    a[i]=i**2  # exponent / calulated square or raise to the power of 2.
print(a)
# output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


# 3. Write a program to multiply all the items in a dictionary.
a={"a":1,"b":2,"c":3,"d":4,"e":5}
product=1
for i in a:
  product=a[i]*product
print(product)
#output: 120


# 4. Write a python program to sort a dictionary by key.

# # sort by keys
a={"a":12,"b":23,"c":6,"d":91,"e":45}
a=sorted(a.keys())
print("dictionary sorted by keys",a)
#output: ['a', 'b', 'c', 'd', 'e']



