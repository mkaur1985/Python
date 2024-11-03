#1. write a program to see if a number is positive.
"""
num=int(input("Enter a number: "))
if(num>0):
    print("Number is positive")

#2. write a program to check whether a number is odd or even (even numbers are divisible by 0 )
num=int(input("Enter a number: "))
if(num % 2==0):
    print("you have entered an even number")
else:
    print(" you have entered  an odd number")

"""


# 3. write a program to create area calculator.

# print("*********Area Calculator************")
# print(""" Press 1 to calculate the area of square (side x side =side square)
# Press 2 to calculate the area of rectangle (length X width)
#Press 3 to calculate the area of circle (The area of a circle is pi times the radius squared (A = π r²).Pi meaninf in circle:This chart shows the angles and points formed by dividing the unit circle into twelve equal parts. Unit circle chart 12.)
# Press 4 to calculate the area of triangle ( Area of a triangle = 1/2 × base × height.)
# """)

'''
choice=int(input("Enter a number between 1-4 :  "))
if(choice==1):
    side=float(input("Enter length of one side of square: "))
    area=side*side  # side**2  we can use exponent as well
    print("Area of square is: ",area)

elif(choice==2):
    length=float(input("Enter length of rectangle: "))
    width=float(input("Enter width of rectangle: "))
    area=length*width
    print("Area of rectangle is: ",area)

elif(choice==3):
    radius=float(input("Enter radius of circle: "))
    pi=3.12  # or we can use (22/7)
    area= pi * (radius**2) # radius square is represented by using exponent r**2
    print("Area of circle is: ", area)

elif(choice==4):
    height=float(input("Enter height of traingle: "))
    base=float(input("Enter base of triangle: "))
    area=(base*height)*(1/2) # or use 0.5
    print("Area of triangle is: ", area)
else:
    print("Invalid input")

'''
"""
#4. Write a program to check whether the passed letter is a vowel or not.
letter=input("Enter a vowel:  ")
if letter in ("a,e,i,o,u") or letter in ("A,E,I,O,U"):  # can be written without commas ("aeiou")
    print("you have entered a vowel")
else:
    print("entered value is not a vowel")
"""

#5. Write a program to check if a number is a single digit number , 2-digit number and so on.., up to 5 digits.
#  digit value lies between belwo categories :
# single digit eg 5: 0 to 9
# double digit eg 12: 10 to 99
# triple digit eg 123 : 100 to 999
# four digits eg 1000 : 1000 to 9999
# five digit eg 10576: 10000 t0 99999

num=int(input("Enter a number: "))
if(num >=0 and num <=9):
  print("You have entered a 1 digit number")
elif(num >=10 and num <=99 ):
 print("You have entered a 2 digit number")
elif(num >=100 and num <=999):
  print("You have entered a 3 digit number")
elif(num >=1000 and num <=9999):
 print("You have entered a 4 digit number")
elif(num >=10000 and num <=99999):
 print("You have entered a 5 digit number")
else:
 print("digit count falls outside the given range")


"""  
var=input("Enter a number: ")
count1=len(var)
print("number entered is a ",count1," digit number")
"""
