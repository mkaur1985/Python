
# 1. Write a program to find a sum of all the even numbers up to 50.

# 1. first logic

"""
sum=0
for i in range(2,50,2):
    sum=sum+i
print(sum)

# 2. second Logic
sum=0
for i in range(2,50):
    if i % 2 == 0:
        sum=sum+i
print(sum)

# 2. Write a program to write first 20 numbers and their squared numbers.

for i in range (1,21):
    square=i**2 #exponent/square root
    print(i,square)
"""

# 3. Write a program to find sum of first 10 odd numbers using while loop.
i=1
sum=0
while i <= 20:
    if i % 2 != 0:
     sum=sum+i
    i=i+1
    print("the sum of first 10 odd digits is :  ",sum)

# 4. Write a program to check if a number is divisible by 8 and 12 up to 100 numbers.

for i in range(1,101):
    if(i%8==0) and (i%12==0):
        print(i,"is divisible by 8 and 12")


# 5. Write a program to create a billing system at supermarket.

    while True:
        name=input("enter customer's name: ")
        total=0

        while True:
                quantity=float(input("enter the quantity of product bought: "))
                amount= float(input("enter the amount of the product "))
                total+=quantity*amount
                repeat=input("Do you want to calculate the total for another product yes/no: ")
                if repeat == "no":
                    break
        print("-"*40)
        print("Name: ",name)
        print("Amount to be paid: ", total)
        print("-" * 40)
        print("*************************Happy Shopping***********************************")

        repeat1=input("Do you want to go to next customer ? (yes/no) :  ")
        if repeat1 == "no" or repeat1 == "No":
            break






