
# A="OOTD.YOLO.ASAP.BRB.GTG.OTW"

# 1.Write a program to separate the following string into comma(,) separated values.
a="OOTD.YOLO.ASAP.BRB.GTG.OTW"
print(a.split("."))

#output :  'OOTD', 'YOLO', 'ASAP', 'BRB', 'GTG', 'OTW']

# 2.Write a program to sort strings alphabetically in python.
# sort alphabetically
a=input("enter any string here: ")
b=sorted(a)
print(b)
#output: ['e', 'h', 'l', 'l', 'o']
# Capital letters are sorted separately


# 3.Write a program to remove a given character from a string.
z="F.R.I.E.N.D.S"
a="hello"
print(a.replace("e",""))
print(z.replace("E",""))

# 4. Write a program to remove dot(.) from the following string.
z="F.R.I.E.N.D.S"
print(z.replace(".",""))

# 5. Write a program to check the number of occurrence of a substring.
a= "she sells seashells on the sea shore"
print(a.count("sea"))


