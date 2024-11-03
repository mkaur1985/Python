
# purpose of converion from tuple to list is:
# Once a tuple is created we cannot update it , but we can convert it into a list and can update the list as required.

a=("Oneplus","Nokia","Redmi")
print(type(a))  #output: <class 'tuple'>

a=list(a)  # converting tuple into a list here.
print("after conversion",type(a))
a.append("Vivo")
print(a)

#output:
#after conversion <class 'list'>
# ['Oneplus', 'Nokia', 'Redmi', 'Vivo']

a=tuple(a) # to convert it back into a tuple.
print(type(a))

#output:
# <class 'tuple'>


# ********************************
#  Functions in tuples
# **********************************

# 1. Count()
print(a.count("Redmi"))

# 2. Index()
print(a.index("Nokia"))

# 3. Lenth()
print(len(a))
