fruits=["apple","banana","mango","12","23"]
print(fruits)
print(type(fruits))
#output: ['apple', 'banana', 'mango']
#<class 'list'>



# /**********************************
# -- Slicing List :
# ************************************/

# Positive Index: ranges between 0 to n
# Negative Index: ranges between -1 to -n ( negative zero doesn't exist here) /it reads the list backwards.
# When we want to display multiple values usinng list then the end range is followed as n+1

#    0         1          2             3
a=["Ironman","Thor","Captain America","Hulk"]
print(a[2])   # output: Captain America
print(a[:2]) # to print first two variables.(always use end value index =  n+1)
print(a[1:])
print(a[::2]) #to print the gap of 2

#    -4       -3          -2           -1
a=["Ironman","Thor","Captain America","Hulk"]
print(a[-3]) # output : Thor
print(a[-3:-1])
print(a[::-1])
print(a[-1:-4:-1]) #starting , -1 , end-4 ,and , reverse -1
#output: ['Hulk', 'Captain America', 'Thor']