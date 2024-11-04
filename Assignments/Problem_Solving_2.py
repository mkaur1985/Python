#Problem solving 2:
#1. write a program to get Fibonacci series up to 10 numbers(Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.).
#Eg . 0 1 1 2 3 5 8 13 21 etc
    # a b c


n=int(input("Enter a number: "))
if n==1:
    print(n)
else:
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2,11):
        c=a+b
        a=b
        b=c
        print(c)

#2. write a program to check if a number is prime or not(whole number geater than 1 , This means that a prime number is only divisible by 1 and itself.).
# eg: 1,3,11,37

num=int(input("Enter a number :  "))
if num <=1:
    print("it is not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("is not a prime number")
            break  # applying break here becz it will check the modulus from 2 up to n and print "it is not a prime number" n number of time the loop executed.
        else:
            print(num," - is not a prime number.")

# Output Example:
#2 % 3  - is not a prime number
#2 % 4  - is not a prime number
#2 % 5  - is not a prime number
#2 % 6  - is not a prime number
#2 % 7  - is not a prime number
#2 % 8  - is not a prime number
#2 % 9  - is not a prime number
#2 % 10  - is not a prime number

# Q3. write a program to find a palindrome of integers.(a number is a palindrome is to reverse the digits of the number and compare it with the original number.)
# Eg:  131=131 ,121=121 , 111=111 , reading in reverse order the number remains the same , hence it s palindrome number.
# 231=132 , after reading in reverse order the number chnaged hence it is not a palindrome.

num=int(input("Enter a number : "))
temp=num
reverse=0
while(num>0):
    digit=num%10  #here we obtain the  remainder value
    reverse= (reverse*10)+digit
    num=(num//10 ) # it will go in the number under our number is greater than 0
if(temp!=reverse):
    print(reverse,"number is not a palindrome")
else:
    print(reverse,"number is a palindrome")


#4. Write a program to create an area calculator.

print("*********Area Calculator************")
while True:
    print(""" Press 1 to calculate the area of square (side x side =side square)
    Press 2 to calculate the area of rectangle (length X width)
    Press 3 to calculate the area of circle (The area of a circle is pi times the radius squared (A = π r²).Pi meaninf in circle:This chart shows the angles and points formed by dividing the unit circle into twelve equal parts. Unit circle chart 12.)
    Press 4 to calculate the area of triangle ( Area of a triangle = 1/2 × base × height.)
    """)

    choice = int(input("Enter a number between 1-4 :  "))

    if(choice==1):
        while True:
            side=float(input("Enter length of one side of square: "))
            area=side*side  # side**2  we can use exponent as well
            print("Area of square is: ",area)
            repeat=input("do you want to try again for square  ? :")
            if(repeat=="no"):
                break

    elif(choice==2):
        while True:
            length=float(input("Enter length of rectangle: "))
            width=float(input("Enter width of rectangle: "))
            area=length*width
            print("Area of rectangle is: ",area)
            repeat = input("do you want to try again for rectangle  ? :")
            if (repeat == "no"):
                break

    elif(choice==3):
        while True:
            radius=float(input("Enter radius of circle: "))
            pi=3.12  # or we can use (22/7)
            area= pi * (radius**2) # radius square is represented by using exponent r**2
            print("Area of circle is: ", area)
            repeat = input("do you want to try again for circle  ? :")
            if (repeat == "no"):
                break

    elif(choice==4):
        while True:
         height=float(input("Enter height of traingle: "))
         base=float(input("Enter base of triangle: "))
         area=(base*height)*(1/2) # or use 0.5
         print("Area of triangle is: ", area)

         repeat = input("do you want to try again for triangle  ? :")
         if (repeat == "no"):
             break

    repeat1=input("Do you want to try another option ?: ")  #this condition is for outer while True statement.
    if repeat1=="no":
         break

