# Python Notes:

WS Cube Tech : 

https://www.youtube.com/watch?v=3n_Gb0aBR6Q

**************************************************************************************************************************************************************************************
JOB Roles with Python:

1-python backend engineer
2-Data engineers
3-RPA developer (Robotic Process Automation
4-Devops engineer
5-Data Scientist
6-Data Analyst
7-Machine learning engineers

/*****************************
   What is Python ?
****************************/

Answer: Python is a programming language that is widely used in web applications, software development, data science, and machine learning (ML).
	Python is used as a “scripting language” for web applications, meaning it can automate specific series of tasks and improve efficiency. 
	Python is an interpreted, object-oriented, high-level programming language with dynamic semantics developed by Guido van Rossum. It was originally released in 1991.


what is interpreter and compiler.
What is the scope of python.

/*********************
Advantages of Python:
**********************/
Open source and free to use
Easy to learn
Portability
Dynamically typed
High-level programming language
Productivity
Extensive libraries
Data science
Huge standard library


/****************************************
What are Python pros and cons?
****************************************/
Pros of Python. Beginner friendly. Well-supported. Flexible. Multiple libraries. Embeddable. Highly scalable. Prototyping-friendly.
Cons of Python. Slower than compiled languages. Less secure. Not ideal work environment. Bad memory consumption and garbage collection. Dynamically typed. Poor multithreading.


/*****************************************************************************************************
PYTHON: Installation and PYCHARM (use as IDE integrated development environment for Python)
*****************************************************************************************************/

1.Install Python
goto--> python.org  , after the installation has been done. IDLE SHELL 3.12.7 version opens.
a). Go to file --> New an untitled page opens. 
b). IDLE SHELL 3.12.7   ----> here we can type print() to print a string and hit enter , output will be displayed as below.


2.Install PYCHARM (https://www.youtube.com/watch?v=6a2cSXgooDo)  : we installed the free version.  (https://www.jetbrains.com/pycharm)

PYCHARM COMMUNITY EDITION : FREE VERSION

3.Connect PYTHON and PYCHARM Interpreter.   python 3.12 .exe /or .exe windows -->   is the interpreter.

Go to file--> New Project-->
a) Give Project Name : KaurProject
b) Location : Update project location
c) New Env : VirtualENV
d) Interpreter: python 3.12 .exe /or .exe windows
e)Uncheck : creat main.py sample script ----------------------> click Create.

*********************************************************************************************************************************************************/
Lets go to PYCHARM to create our projects and our program files.

ProjectName: KaurProject ---> right click --> New file--> name : Demo

Command:   print("hello world")
Output :   hello world
Save as : Demo  or save All

Right click --> run Demo , or go to run on menu bar and execute it.

/************************************************************************
FIRST PROGRAM :   Here we are using multiple print()
************************************************************************/

print ("hello world")
print("this is my first program")
print("I hope you all will like it")


/****************************************************************************************************************************************************************
A) to write multiple line in different rows using 1 print() --> 2 Methods used.
					i) Triple quotations  (could be triple single or triple double quotations)
					ii) \n backslash
****************************************************************************************************************************************************************/

Example 1.
print (""" Hello guys
 Hope you will like my first program
 see you soon""")

Example 2.
print (''' Hello guys
 Hope you will like my first program
 see you soon''')

Example3.
print (' Hello guys it\'s me')  ---> for apostrophe use a back slash , otherwise it gives an error.

Example 4.
print ("Hello world! \nThis is Preeto learning python. \nHope I succeed.")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/****************************
--COMMENTS in PyCharm
*****************************/

To give explanation of the code.
i) Single Line Comments: just use  ----  >   # hash
ii) Multiple Line Comments: use triple quotes  --- >  """  


Example 1.  # in this program I will add two number  --> hit enter --> PyCharm ignores this completely and --> nothing will be displayed in run window

Example 2. Triple Quotes. (quotes could be single or double)

"""
in this program I will add two number
Hello world
I am testing multiple line comments
"""


'''
in this program I will add two number
Hello world
I am testing multiple line comments
''' 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/****************************
--VARIABLES in PyCharm
*****************************/

Variables are placeholder that can store a value.  or a container that can hold data inside it like a value.
Variable could be a letter or a word and we simply assign a value to it. 
Simple variable can be created who's value can increase or decrease. Next we can have a constant variable (value for such variable doesn't change).

Input

a="hello world"
print(a)

Output: hello world

Rules for variables:
i) python is a case sensitive language so varibale names are case sensitive.
ii) There should be no space in variable name , _ underscore can be used in variable name
iii) variable name should not begin with a number or special character.  

a="hello world"
print(A )  --> this will throw error for the variable that's different than we used.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/****************************
--Datatypes and User-Inputs	
*****************************/

Types of data a variable can store.
-----------------------------------

Data types: 
(a)Text type: string (str)
(b) Numeric Types : int, float , complex ,Evalute(eval) --> used for mathematical terms (works with print() as well to print strings) , helps in finding  answer for an expression.
(C) Sequence : list, tuple, range
(d) Mapping Type: Dictionaries(dict)
(e) set type: set , frozenset
(f) Boolean type: bool
(g) Binary Types: bytes ,bytearray,memoryview


User - Input:
------------------
Like entering credentials on the website login page.

name=input("What is your name: ")   --> taking value at the execution time and assigning to variable name. No data type specified here so its string by default.
print(name)   ---> to print the value on the output screen we use print()

output: 
Entered name by user

What is your name: John
John

(i)INTEGER:
Age=int(input("What is your age? ") )

(ii)float: 
salary=float(input("What is your salary? ") )

iii) exp1=eval(input("enter an expression here"))
     print(exp1)

output :  2+3 , we receive result as --> 5


/----------------------------Output-----------------------------------------	
	What is your name: Preeto
	Preeto
	What is your age? 39
	39
	What is your Salary? 89000
	89000.0
	enter an expression here2+3
	5 
or

enter an expression here print("hello world")
hello world
None

--------------------------------------------------------------------------------/

/****************************
--Typecasting and subtypes	
*****************************/

Typecasting : conversion from one data type to another data type is called type casting.

i) Implicit Type conversion: where python itself converts one data type to another.
ii) Explicit Type conversion: where the user converts one data type to another type. 

type : In python can tell us the data type of a variable.

/*****************
  Example:
*****************/

name="Maharishi Arvindo"
print(type(name))
output:  <class 'str'>

age=23
print(type(age))
output: <class 'int'>

sal=23.00
print(type(sal))
output: <class 'float'>


Implicit Type:
a=123
b=1.23
c=a+b
print(c)
print(type(c))   ---> output will show a float data type  --> <class 'float'>


/*****************
Explicit Types:
*******************/

a="123"
a=int(a) ----- > #this is called explicit conversion of string into int
a=float(a)
b=1.23
c=a+b
print(c)
print(type(c))
 or

print("after conversion type is " , type(c)) --> add a string and separate using a comma.

----------------------------------------------------------------Questions Implementation--------------------------------------------------------------------


""" Questions and answers """
# Q1. print name , age and address in different lines.
name="Abacus"
age=23
address="654 lake street"
print(name)
print(age)
print(address)


# Q2. swap (interchange) two variables. --> Method 1. can be using temporary variable(put x=20 and y=10)

x=10
y=20
print("original value of x is: ", x)
print("original value of y is: ",y)
temp=x
x=y
y=temp
print("swapped value of x is: ", x)
print("swapped value of y is: ", y)

# Method 2.
a=30
b=40
print("original value of a is: ", a)
print("original value of b is: ",b)
a,b=b,a  # simply write using a comma
print("swapped value of a is: ", a)
print("swapped value of b is: ", b)

# Q3. write a program to convert float into  integer

z=24.56
print("Original value is",(z))
print("original data type is: ",type(z))
z=int(z)
print("After the type conversion the value is:",(z))
print("Converted data type is: ", type(z))

# Q.4 Write a program to take data from a student, ID card then print in different lines. (use input())

print("*** Student Identity card ***")
name =input("enter name of student: ")
age =int(input("enter age of student: "))
grade=input("enter grade of student: ")
email=input("enter email of student: ")
ph_no=input("enter phone number of student: ")
print("*** Student Identity card ***")
print(name)
print(age)
print(grade)
print(email)
print(ph_no)

# Q.5 write a program to take a user input as an integer value then convert it to float.

ab=int(input("Enter a number: "))
print("Checking the data type ",type(ab))
ab=float(ab)
print("Checking the data type after conversion ",type(ab))

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/****************************
 Operators and Operands.
****************************/

i) Operators : Indicates what operation is to be performed. (+ - * / =)
ii) Operands : On what the action is performed.

Eg : x + y  = 0

x, y and 0 are operands. + and = is an operator.


/**************************************
 7 Types of operators in Python
**************************************/ 
1. Arithmetic Operators.
2. Comparison Operators.
3. Logical Operators.
4. Assignment Operators.
5. Identity Operators.
6. Membership Operators.
7. Bitwise Operators.


/**************************************
 1. Arithmetic Operators
**************************************/
1. Addition  +
2. Division /  :  if we divide 8/3 , the quotient value = 2.66 (that is on the top of divide symbol)
3. Subtraction -
4. Multiplication  *
5. Modulus %  : Provides the remainder of/during division. 8%3 = 2   , it will give a numeric value before the decimal. 
6. Floor Division  //   :  if we divide 8/3 , the quotient value = 2  , it gives the value before the decimal.
7. Exponentiation  **  (for numbers in powers) 2 raise to power  (2**10)


--------------------------------------------------------------------------------------------------------------------------
# 1.Modulus %  , it will give remainder value but a value before the decimal.

print(8%3)

# 2. division

print(8/3)

# 3.floor division  , it gives the quotient value before decimal

print(8//3)

# 4. Exponentiation , 2 raise to 10 , or 2 raise to power 10.

print(2**10)
----------------------------------------------------------------------------------------------------------------------------

/**************************************
 2. Comparison Operators
**************************************/
i)   Less than  <
ii)  Less than equal to <=
iii) Greater than  >
iV)  Greater than equal to >=
v)   Not equal to !=
Vi) equal to ==

-----------------------------------------------------------------------

# Greater than symbol , returns true or false value
print(3>2)

# Greater than equal to symbol
print(4>=4)

# Less than
print( 2<3)
# Less than equal to symbol
print(2<=3)

# equal to ==
print(3==3)

# Not equal to
print (3!=3)  # false
print(3!=4)  # True
--------------------------------------------------------------------------------

/**************************************
 3. Logical Operators
**************************************/

i) And : True if both operands are true eg. (x and y)

ii) OR : True if either of operand is true eg. (x or y)

iii) NOT : True if operand is false (complements the operand) eg (not x)


----------------------------------------------------------------------------------------------------------
# And operator

print(3>2 and 3<4)

# OR Operator
print( 3>2 or 3>4 or 5>4)

#Not Operator , it reverse the value of expression.( It converts true into false and false into True)
print(not(6>5) or (3<2 ))

----------------------------------------------------------------------------------------------------------

/**************************************
 4. Assignment Operators
**************************************/

Assignment operators are used in python to assign values to variables.

i) =  		example : x=6
ii) +=		x+=6 ( x=x+6)
iii) -=		x-=6 (x=x-6)
iV) *=		x*=6 (x=x*6)

/**************************************
 5. Identity Operators
**************************************/

Identity operators are used to compare items to see if they are the same object with the same memory address and if the objects are of same type or not.


Memory Allocation: When the program is compiled or executed, the system allocates memory to hold the variable. The amount of memory allocated depends on the variable's data type. For example, an integer variable may typically require 4 bytes of memory.



i) IS
ii) IS NOT

two variables :
having same data type 
storing similar value 
storing value into same Id etc.

a=1234
b="1234"
print(a is b)  # returns false because we compared number with string

a=1234
b=1234
print(a is b) # returns true because we compared number with number
print(a is not b) # returns false because we said datatype of a and b is not same(value and data type both are same).

/*******************************
6. Bitwise Operators
********************************/

These operators are used to compare the binary numbers. There are 2 binary numbers 1 and 0.   Binary means 2. To convert a number into binary we bin() in python.

print(bin(10))

1 means ON or True
0 means OFF or False

i) And (&)
ii) OR (|)
iii) XOR (^) Operator
iV) << zero fill left shift
v) >> Zero fill right shift

And Operator:
0&0=0
0&1=0
1&0=0
1&1=1

OR Operator:
0|0=0
0|1=1
1|0=1
1|1=1

XOR Operator:
0^0=0
0^1=1
1^0=1
1^1=0

(A)Zero fill left shift : adds digits to the left of a number by removing digits from the right. 

eg : 10<<2 , it will add 2 zeros to the left and also removes last 2 digits from right.

10=1010

output: 0010

(b)Zero fill Right shift :adds digits to the right of a number by removing digits from the left. 

eg: 10>>2

10=1010
output: 1000



----------------------------------------------------------------------------
a = 10
b = 8
print(a & b) # displays 8 because when we convert 10 and 8 into binary and perform "and" operation on it give answer as 8 in binary.

print("Binary conversion of 10 is: ", bin(10))
print("Binary conversion of 8 is: ", bin(8))
print("Binary conversion of performing and on 10&8  is: ", bin(a & b))

--------------------------------------------------------------------------
/*******************************
7. Membership Operators
********************************/

Are used to check the presence of a sequence in an object.

Type:
1. In
2. not in

--------------------------------------------------------------------------------
a="hello world"

print("p" in a) # returns false because p is not a part of the string stored in variable a

print("e" in a) # returns true because e is a pet of the string stored in variable a

print("p" not in a)  # returns True because p is not a part of the string stored in variable a

---------------------------------------------------------------------------------

/****************************************************************************************************************************************************************************************/

-------------------------------------

Conditional Statements:
-------------------------------------

Conditional statement allows system to execute a certain condition only if it is true. Indentation is important while writing the if statements because there is no use of parentheses in 
if statements , so we differentiate the statements blocks within if condition with indentation(tab). The indentation is performed automatically in Python(PyCharm community edition interface).

Types of conditional statements:
1. If the statement
2. if-else statement
3. if-elif-else statement
4. Nested if statement
5. Short hand if statement. 
6.  Short hand if else statement. 


(i) If statement: most fundamental decision-making statement.

If statement in python has subsequent syntax:

if expression 
statement

/*********
 SYNTAX:
*********/
if(condition) :
     Print() 

-----------------------------------------------------
Example:
marks=97

if marks>=90:
    print("You are eligible to enroll in science")

print("thank you")
---------------------------------------------------------

(ii) If-Else Statement :

if-else statement is used when you want to give two statements to computer.
If one condition is false , program executes another condition.

/***********
Syntax:
***********/
if condition:
	#will execute this block if condition is true.
else:
	#will execute this block if condition is false.
	
-------------------------------------------------------------
Example:
#2. If-else statement

marks=80
if marks>=90:
    print("You are eligible")
else:
    print("You are not eligible")
----------------------------------------------------------------


iii) If-elif-else Statement: elif (is a combination of else if)

If condition is evaluated first- if it is false , then the control will move on to the next condition check that is elif condition.If the elif condition is also false then the control moves to the else part.
Multiple elif conditions can be applied.

/***************
SYNTAX:
****************/
if condition:
	Body of if
elif condition:
	body of elif
else:
        body of else


-----------------------
Example:
-----------------------
#3. if-elif-else statement
marks=60

if marks>90:
    print("You can go to a trip")
elif (marks >=80 and marks <=90):
    print("you can go to Vrindavan")
elif (marks >=70 and marks <=80):
    print("You can go to Varsana")
elif(marks>=60 and marks<=70):
    print("You can go to a temple")
else:
    print("God is within you...do naam Jap !")



--------------------------------------------------------

iV) Nested if statement :      [Also called if within if]

Nested if statement is one in which an if statement is nested inside another if statement. control moves in the inner condition if the outer if condition is true.

/********************
Syntax:
********************/ 
If(condition 1):
   #Execute if condition 1 is true
	If(condition 2):
   	#Execute if condition 2 is true
	if(condition 3):
  	 #Execute if condition 3 is true
	condition3 ends here
	condition2 ends here
	condition 1 ends here
else:
#execute else part. 


-----------------
Example:
----------------- 

#4. Nested if statement:

marks=87
if(marks>85):
    print("You are going on a trip")
    if(marks > 86):
        print("You can buy beautiful clothes")
        if(marks > 90):
            ("You are going on another trip")
        else:
            ("It's enough fun this time !! Lets head home !!")
---------------------------------------------------------------------------------

/**********************************
  5. Short Hand if statement
**********************************/ 

Short hand if statement is used when only one statement needs to be executed inside the if block. This statement can be mentioned in the same line which holds if statement. Python is an interpreted language which executes each line one by one. By writing the if condition and statement in same line saves time.

Syntax:
if condition : statement

--------------------------------------------------------------
Example:

marks=87
if(marks >= 85): print("You are eligible for buying a dictionary")
------------------------------------------------------------------

/**********************************
 6. Short Hand if else statement
**********************************/ 

It is used to mention if-else statements in one line. There is only one statement
to execute in both if and else blocks. we do not use colons in syntax for this if statement.

SYNTAX:
[body of if ] if (condition) else [body of if else statement]

--------------
Example
----------------
marks=90
print("you are going on a trip") if (marks>=85) else print("You have won the championship")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/**********************************************
	Problem solving: check in Pycharm
************************************************/

1. write a program to see if a number is positive.
2. write a program to check whether a number is odd or even
3. write a program to create area calculator.
4. Write a program to check whether the passed letter is a vowel or not.
5. Write a program to check if a number is a single digit number , 2-digit number and so on.., up to 5 digits.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/************************************************
-- Conditional Loops
*************************************************/

A loop means to repeat something in the exact same way.

1. For Loop
2. While Loop
3. While True
4. Nested loop (loop within loop)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
/**********************************************************************************************************************************************************************************
1. For Loop :
*********************/


For loop is a loop that repeats something in a given range.
The range has a starting point , ending point and a step/ gap in it.
+1 is added to the ending point while defining a range.



copied from google:
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). 
eg:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

Output: 
apple
banana
cherry



fruits = ["apple", "banana", "cherry"]
for x in fruits:
 print(x)
if x==banana:
break
Else:
print("the condition is false so control moved to the else part.")




Syntax:
for variable in range(any number/digit):

/********************
1. first
********************/
for x in range(6):
  print(x) 
output:
0
1
2
3
4
5

Note that range(6) is not the values of 0 to 6, but the values 0 to 5 because it begins with 0 and not 1.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6): 

/********************
2. second
********************/
for x in range(2, 6):
  print(x)
output: 
2
3
4
5

/********************
3. Third
********************/
for x in range(2, 30, 3): # there will be gap of 3 numbers
print(x) 
Output:
2
5
8
11
14
17
20
23
26
29

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/********************************************************
 --2. WHILE LOOP
*********************************************************/
While loop executes till the given condition is true.
In while loop , the increment is done inside the loop.

The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.


# Syntax
# while [condition]
# body of while
# Increment

------------------------------------
#  1. While loop statement.
------------------------------------
i=1
while(i<6):
    print(i)
    i=i+1

-------------------------------------------------------------------------
# 2. "break statement" to bring the control out of the loop statement.
----------------------------------------------------------------------

i = 1
while (i < 6):
    print(i)
    if(i==3):
        break   # control will come outside the loop.
    i = i + 1

--------------------------------------------------------------------------------------------------
#3. With the "continue statement" we can stop the current iteration, and continue with the next:
-----------------------------------------------------------------------------------------------
#i = 1
#while (i < 6):
#    print(i)
#    if(i==3):
#        continue   # to continue with next iteration.
#    i = i + 1     # if we put the increment statement her it will keep executing in loop (infinite loop)

# Infinite Loop : An infinite loop is a sequence of instructions in a computer program which loops endlessly, either due to the loop having no terminating condition, having one that can never be met, or one that causes the loop to start over.

-------------------------------------
# 4 .Continue with good syntax:
-------------------------------------
i = 0
while i < 6:   # do not use backets here , otherwise it will not run properly.
  i += 1
  if i == 3:
    continue
  print(i)

  #output:
  #Remember 3 will be missing here

  1
  2
  4
  5
  6


----------------------------------------------------------------------------------
#5 Else statement with While , to print a statement when a condition is false.
----------------------------------------------------------------------------------
i=1
while i < 6:
    print(i)
    i=i+1
else:
    print("the condition is false: ")



/***************************************
 --3. Nested Loops
*****************************************/

A loop within a loop is called a nested loop.
Nested loops are also used to solve pattern problems.

i) It can be done using a for loop
ii)It can be done using a while loop as well.



for i in range(1,4):    # this outer loop represents rows
    print("""
    """)
    for j in range(1,11):  # this inner loop represents columns.
        print(j, end ="")  # to print ouput in same line and not in different lines.
print()



# lets take an example of 5 rows and 5 columns for similar pattern.

for i in range(0,6):    # this outer loop represents rows
    print("""     # applied in outer loop to enter a line.
    """)
    for j in range(1,i+1):
        print(j, end = " ")   # end ="" is used to print inner loop output in same row.
print()


# Output:
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5



------------------------
--- Copied from w3school.
------------------------

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


Output:
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry


/**********************************
4. Pass statement: with for loop
************************************/
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement


/************************************************
5. While True  : T should be capital in True 
**************************************************/
It is an infinite loop.
To break a while true loop, break statement is used.

# while True: is an infinite loop, it cannot be stopped. To stop it we use break statement.


while True:
    num1=int(input("Enter a num1: "))
    num2 = int(input("Enter a num2: "))
    print("sum of both numbers is: ",num1+num2)
    repeat=input("do you want to stop the program yes/no: ")
    if repeat=="yes":
        break


/**********************************************************
--- Problem Solving :
**********************************************************/

1. Write a program to find a sum of all the even numbers up to 50.
2. Write a program to write first 20 numbers and their squared numbers.
3. Write a program to find sum of first 10 odd numbers using while loop.
4. Write a program to check if a number is divisible by 8 and 12 up to 100 numbers.
5. Write a program to create a billing system at supermarket.

Problem solving 2:
1. write a program to get Fibonacci series up to 10 numbers.
2. write a program to check if a number is prime or not.
3. write a program to find a palindrome of integers.
4. Write a program to create an area calculator.

Problem solving 3:
created different patterns like triangle , Christmas tree , etc


/**********************************************
--- String Manipulation
***********************************************/
Strings are combinations of numbers, alphabets/letters and  symbols enclosed inside quotations.

String Methods/functions:
1.lenght : returns the length of a string.
2. count : counts the number of times a word occurs in a string.
3. upper : converts the string into uppercase.
4. lower : converts the string into lower case.
5. casefold : Converts string into lower case
6. Capitalize : Converts the first character to upper case.
7. Index : Searches the string for a specified value and returns the position of where it was found ( returns the address )
8. find : Searches the string for a specified value and returns the position of where it was found ( returns the address )

9. format : Formats specified values in a string  (formats value of string)
10. center : Return a centered string.

/***************************
STRINGS PART 2
*****************************/

11. isalnum : returns True if all characters in the string are alphanumeric.
12. isalpha : returns True if all characters in the string are alphabet.
13. isdecimal :  returns True if all characters in the string are decimals
14. isdigit : returns True if all characters in the string are digits.
15. isnumeric : returns True if all characters in the string are numeric.
16. islower : returns True if all characters in the string are in lowercase.
17. isupper : returns True if all characters in the string are uppercase.
18. isspace : returns True if all characters in string are whitespaces.
19. istitle : returns True if all words in a text start with a upper case letter.(Symbols and numbers are ignored) AND the rest of the word are lower case letters, otherwise False. 

a="hello"
b="Hello123"
c="123456"
d="HELLO"
e=" "
f="Hello 123"
g="1.234"

SYNTAX:
print(a.isalnum())
print(a.isalpha())
print(a.isdecimal())
print(a.idigit())
print(a.isnumeric())
print(a.islower())
print(a.isupper())
print(a.isspace())
print(a.istitle())

/***************************
 STRINGS Functions PART 3
*****************************/

1. endswith() : Returns true if string ends with a specified value.
2. startswith() : Returns True if the string starts with a specified value.
3. swapcase() - swaps or converts (The lower case into capital) and (capital case into lower case)
4. strip() - Returns a trimmed version of a string.
5. Split() - splits/breaks the string by a character or by default string.
6. ljust() - Return left justified version of the string.
7. rjust() - Returns the right justified version of the string.

string.ljust(length, character)

Parameter	Description
length		Required. The length of the returned string
character	Optional. A character to fill the missing space (to the right of the string). Default is " " (space).


8. Replace: A string is replaced with a specified value.
9. rindex(): Searches the string for a specified value and returns the last position of where it was found

String characters: starts counting from 0 to n..

HARRY POTTER
01234567891011


/*********************************
-- SLICING IN STRINGS
***********************************/

It cut down the strings in small parts.

# 1. Slicing of a string: to cut down the string within a starting and ending point.
a="Harry Potter and the Goblet of Fire"
print(a)
print(a[0:5]) # print harry
print(a[6:12]) #print potter

print(a[:5]) # No need to specify the beginning address as it begins with 0 as a default value.
print(a[-4:]) #reading from right side or from the end of the string.

# 2. slicing of a numeric string.
b="0123456789"
print(b[::2]) # here we are not defining the starting or the end value but we want to define the gap of 2 here
print(b[:6:2]) # starting point not given(default 0), but end is given with a gap of 2 numbers.
print(b[:6:3])

# 3. Reverse order :
print(b[::-1]) # to print in reverse order. Output: 9876543210
print(b[6::-1]) # reverse order again but from 6 to 0 , use -1 for reverse order.


/********************************************
-- Problem Solving
**********************************************/

A = " why fit in , when you are Born to Stand Out!" 
1. write a program to find the length of the following string.
2. write a program to check how many time alphabet O is occurring.
3. write a program to convert whole string into upper and lowercase.
4. Write a program to convert whole string into title.
5. Write a program to find the index number of "fit in" . 


a = " why fit in , when you are Born to Stand Out!"

# 1. write a program to find the length of the following string.
print("Length of the string is: ",len(a))

# 2. write a program to check how many times alphabet O is occurring.

print("String o is occurring : ",a.count("o") ,"times")
print("String O is occurring : ",a.count("O") ,"times")

# 3. write a program to convert whole string into upper and lowercase.
print(a.upper())
print(a.lower())

# 4. Write a program to convert whole string into title.
print(a.title())  #first letter of each word gets converted into capital

# 5. Write a program to find the index number of "fit in" .
print(a.find("fit in",0,11))
print(a.index("fit in",0,11))
print(a[5:11])  # using (slicing/cut down) find the "fit in" from a string.

/**************************************
 Problem solving 2
***************************************/

A="OOTD.YOLO.ASAP.BRB.GTG.OTW"

1. Write a program to separate the following string into comma(,) separated values. (split())
2.Write a program to sort strings alphabetically in python. (sorted())
3.Write a program to remove a given character from a string. (replace())

Z="F.R.I.E.N.D.S"

4. Write a program to remove dot(.) from the following string. (replace())
5. Write a program to check the number of occurrence of a substring. (count())


/**************************************
 Problem solving 3
***************************************/
1. Take an input from a user as a string then,reverse it.
2. write a program to check if a string contains only digits.
3. Write a program to check if a string is palindrome.
4. write a program to find number of vowels in a string.
5. write a program to check if every word in a string begins with a capital letter.



# /**************************************
#  Problem solving 3
# ***************************************/

# 1. Take an input from a user as a string then,reverse it.
# a=input("Enter a string: ")
# print(a[::-1])

# 2. write a program to check if a string contains only digits.

a="12345678"
b="abc123"
c="abc"
print(a.isalnum()) # number and alphabet
print(b.isalnum())
print(c.isalpha()) # only alphabet
print(a.isdigit())

# 3. Write a program to check if a string is palindrome.
# a=input("Enter a string : ")
# b=a[::-1]
# print(a)
# print(b)
# if(a==b):
#     print(a,"is a palindrome")
# else:
#     print(a,"is not a palindrome")

# 4. write a program to find number of vowels in a string.
#
# a=input("Enter a string to check vowels : ")
# vowels=0
# for i in a:
#     if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" ):
#         vowels=vowels+1
# print("the number of vowels are : ", vowels)


# 5. write a program to check if every word in a string begins with a capital letter.

#a=input("Enter a string to check the title : ")
# b=a.title()
# print(a)
# print(b)
# if(a==b):
#     print(a," - Each word in the string begins with capital letter")
# else:
#     print(a," - Each word in string doesn't begin with capital letter")

----------------------
Easy Method
-----------------------
a=input("Enter a string to check the title : ")
print(a.istitle()) #this function return true or false.


/**********************************
 -- Introduction to lists
************************************/

Lists are the collection of ordered( follows indexing) and mutable data.
1. lists are written inside the squared brackets.
2. The value inside a list is separated by coma(,)
3. Mutable means once created , they can be changed.
4. Multiple datatypes can be written inside a list.

a=["apple","banana","mango","1","1.41"] Any number of datatypes can be written inside the list. 

Example:

fruits=["apple","banana","mango","12","23"]
print(fruits)
print(type(fruits)) # it gives us the data type of the list.
#output: ['apple', 'banana', 'mango']
#<class 'list'>

Note:
A variable can store only one value.
A list store multiple values of different type.


/**********************************
-- Slicing List :
************************************/

Positive Index: ranges between 0 to n
Negative Index: ranges between -1 to -n ( negative zero doesn't exists here) /it reads the list backwards.

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


/***************************************
 -- List Iteration:
****************************************/ 
1. Iteration using foor loop
2 .Iteration using for loop with Range and length function
3. Iteration using While loop
4. Using short hand for loop.


# ***************************************
#  -- List Iteration:
# ****************************************/

# 1. Iteration using for loop
a=["Hulk","Thor","Ironman","Captain America"]
# for i in a:
#     print(i)

# 2 .Iteration using for loop with Range and length function

# i means Index( address of values)
# a is a list that has values

# for i in range(len(a)):
#     print(i)  # this will only display 1 to 4  Index numbers
#     print(a[i]) # this displays value at each index.

# 3. Iteration using While loop
# i=0
# while i< len(a):  # here i should be smaller than length of the list
#     print(a[i])
#     i=i+1

# 4. Using short- hand for loop.
[print(i) for i in a]



/*************************************
  List Functions
**************************************/
# to find the length of a list
# to count an occurrence of a particular element
# to add to the list
# to add to a specific location
# to remove from a list
# to remove from a certain location.




# /*************************************
#   List Functions
# **************************************/
# 1. to find the length of a list

a=["Thor","Hulk","Ironman","Captain America"]
print(len(a))

# 2. to count an occurrence of a particular element
#
# a=["Thor","Hulk","Ironman","Captain America","Hulk"]
# print(a.count("Hulk"))

# 3. to add to the list
# append() is used to add a value to the end/last of the list.

# a.append("Bheem")
# print(a)
#output: ['Thor', 'Hulk', 'Ironman', 'Captain America', 'Hulk', 'Bheem']

# 4. to add to a specific location
# insert method is used to insert a value at a particular position. We first specify the index number and then the actual new value.
#
# a.insert(1,"vision")
# print(a)

# 5. to remove from a list
a.remove("Hulk")  # to remove a value from list we use remove() , if there is multiple occurance of the vlaue then remove() removes the very first occurrence from the list
print(a)

# 6. to remove from a certain location.
# when we don't know the value but we know only location eg index 1

print(a.pop(1)) # removes value from index 1
print(a)


/*****************************
 List Functions - Part2
*******************************/ 
a=["Thor","Hulk","Ironman","Captain America"]

# to create a copy of a list
# to access an element
# to entend the list
# to reverse the list
# to sort the list
# to clear all the data from the list.



a=["Thor","Hulk","Ironman","Captain America"]

# to create a copy of a list
b=a.copy()
print(b)

# to access an element(or access an index)
print(a.index("Ironman"))

# to extend the list
c=["vision","spiderman"]
a.extend(c)
print(a)

# to reverse the list
print(a)
a.reverse()
print(a)

# to sort the list (it will sort in ascending order of alphabets or numbers)
a.sort()
print(a)

d=[3,56,7,8,2,4,6,8,0,1]
d.sort()
print(d)

# to clear all the data from the list. (it will empty the list)
a.clear()
print(a)
d.clear()
print(d)
#output:  []
	  [] 
_________________________________________________________________________________

/**************************************
-- List Comprehension
****************************************/

To create a new list based on the values of an existing list.
We don't want to copy everything from exiting list , so we can't use copy().

so we can use for loop statement using if condition in it. But that method is a bit length method as example: (Without list comprehension you will have to write a for statement with a conditional test)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

---------------------------------------
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
-------------------------------------------

output: 
['apple', 'banana', 'mango']


/***********************************
Example using list comprehension
*************************************/
With list comprehension you can do all that with only one line of code:

l1=[30,40,50,60]
l2=[]
for i in l1
if(1>45);  put condition here 
l2.append(i)
print(l2,"\n",l1) #gives same out for both the lists


/**********************************
syntax:  list comprehensive
**********************************/

l1=[30,40,50,60]
l3=[i for i in l1]  # means obtain i using a for loop.
print(l3)

/****************************
# with if condition
******************************/
l1=[30,40,50,60,70,80,90]
newlist=[]
newlist=[i for i in l1 if i > 45 ]
print(newlist)


#output:
#[50, 60, 70, 80, 90]

other examples:
# newlist=[x for x in fruits if x == "apple"]
# newlist=[x for x in fruits if x != "apple"]
_________________________________________________________________________________

/***************************
Problem Solving:
***************************/

a=["Ross","Rachel","Monica","Joe","Chandler"]

1. write a program to swap first and forth element A[0],A[3]=A[3],A[0]
2. write a program to add a new value at second position (insert())
3. write a program to delete a value from 3rd position. (pop())
B=[13,77,12,10]
1.write a program to multiply all the numbers in the list, multi=multi*1
2. write a program to get the largest number from the list. (first sort() then use B[-1])
3. write a program to get the smallest number from the list. (first sort() then use B[0]) 

---------------------------------------------------------------------------------

/******************************
 -- Introduction to Tuples  
*********************************/ 

Mutable: data can be added / removed
Un-Mutable: data cannot be added / removed

Tuples are the collection of orderes and un-mutable data.
1) for tuples - brackets are not mandatory. By choice one use parantheses.
2) The value inside a Tuple is seperated by comma(,).
3) Once created ,tuples cannot be changes.
4) Multiple data types can be written inside a tuple.

data types eg: string, integer, float,boolean 

eg:
a="apple","mango","banana"
b=("apple","mango","banana")
print(type(a))
print(type(b))

---------------------------------------------------------------------------------

/***********************************
--Slicing and Iteration in tuples
************************************/


# /***********************************
# --Slicing and Iteration in tuples
# ************************************/

a=("OnePlus","Vivo","Redmi","Samsung","Nokia")

# print(a[1:3]) # if we want to print Vivo and Redmi we have to give index as 3 , because we always add 1 to the n value ( 0 to n+1)  otherwise it will not give the correct result.
# print(a[:3])
# print(a[2:])
# print(a[::2]) # we want here gap of 2 for complete tuple.
# print(a[1::2])
# print(a[::-1]) # reverse copplete tuple.
# print(a[2::-1]) # from Redimi to reverse order so we used -1

# *****************************
# -- Iteration
# ******************************
# 1. For loop
a=("OnePlus","Vivo","Redmi","Samsung","Nokia")
for i in a:
    print(i)

# 2. along with range and length in for loop
for i in range(len(a)):
    print(a[i])  # we want value of index here , if we use only i that will give us index.

#3. along with while loop.
i=0
while (i<len(a)):
    print(a[i])
    i=i+1


---------------------------------------------------------------------------------

/**************************************
 -- Converting tuples to list
****************************************/

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

 -------------------------------------------------------------------------

Q. What is JSON  : 

Answer: JSON stands for JavaScript Object Notation and is a lightweight format for storing and transporting data. JSON is often used when data is sent from a server to a web page. Python has the built-in module json , which allow us to work with JSON data.

In simple words: JSON (JavaScript Object Notation)
i) is a lightweight format for storing and transporting data.
2) JSON is often used when data is sent from a server to a web page.
3) Python has the built-in module json
------------------------------------------------------------------------------

/************************
 --DICTIONARY :
************************/
Dictionaries are used to store data values in key : value pairs.

1)A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
2)As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
3) Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
4) duplicates are not allowed: Dictionaries cannot have two items with the same key:


dict(): is used to create a dictionary. (also called  dict() Constructor)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 
# output: {'name': 'John', 'age': 36, 'country': 'Norway'}



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


Duplicates eg: 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


Accessing the dictionary data:
1. x = thisdict["model"]

2. x = thisdict.get("model") #get() method gives the same result.

3. x = thisdict.keys()  # key() return a list of all the keys in the dictionary #output: dict_keys(['brand', 'model', 'year'])

4. x = thisdict.values()  # values() method will return a list of all the values in the dictionary.   #output:  dict_values(['Ford', 'Mustang', 1964])

5.x = thisdict.items()  #Get a list of the key:value pairs
#output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


/**********************************
Python Collections (Arrays)
***********************************/

There are four collection data types in the Python programming language:

1.List is a collection which is ordered and changeable. Allows duplicate members.
2.Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3.Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4.Dictionary is a collection which is ordered** and changeable. No duplicate members.


JSON.DUMPS: json.dumps() converts Python objects to JSON strings.

JSON.LOADS: json.loads() converts JSON strings to Python objects,


/****************************************
	*****Problem Solving****

 Convert Python data into Jason format
                 and
 Convert Jason data into Python format
******************************************/ 

1. Convert the following dictionary into Jason format
 student_data ={"name": "David","age":13,"marks":87}

2.Access the value of age from the given data.
 student_data={"name": "David","age":13,"marks":87}

3. Pretty print following JSON data.
student_data={"name": "David","age":13,"marks":87}

4. Sort the following JSON keys and write them into a file.
student_data={"name": "David","age":13,"marks":87}


/****************************
Answers to Problem solving:
******************************/ 


# In simple words: JSON (JavaScript Object Notation)
# i) is a lightweight format for storing and transporting data.
# 2) JSON is often used when data is sent from a server to a web page.
# 3) Python has the built-in module json

# JSON.DUMPS: json.dumps() converts Python objects to JSON strings.

# JSON.LOADS: json.loads() converts JSON strings to Python objects,


#1. Convert the following dictionary into Jason format
import json
# student_data ={"name": "David","age":13,"marks":87}
# print(student_data)
# print(type(student_data))  #output: <class 'dict'>
# data=json.dumps(student_data) # converts python object into JSON string.
# print(data)         # output: {"name": "David", "age": 13, "marks": 87}
# print(type(data))   #output: <class 'str'>

#2.Access the value of age from the given data.
# Student_data='{"name": "David","age":13,"marks":87}'  # we have to convert the dictionary into string, int or string array before accessing its values. Hence we used single quotes for defining the dictionary.
# data=json.loads(Student_data) # used to convert json object into python string.
# print(data["age"])
# print(data["name"])


#3. Pretty print following JSON data.
# student_data={"name": "David","age":13,"marks":87}
# data=json.dumps(student_data,indent=4,separators=("," , "=") )
# print(data)

#Output: It has , and = sign used as a separator
# {
#     "name"="David",
#     "age"=13,
#     "marks"=87
# }


#4. Sort the following JSON keys and write them into a file.
student_data={"name": "David","age":13,"marks":87}
f=open("demo.json","w")
data=json.dumps(student_data,indent=4,sort_keys=True)
f.write(data)
print("the data has been added to the file")


#5. Access the nested key marks from the following nested data.

student_data="""{ "student":
                  {"grade":
                    {"name":"David","marks":87 }
                  }
                 
                }"""


data=json.loads(student_data ) # converted into python object
print(data["student"]["grade"]["marks"]) #print the nested data. , either the varibale should of same type then we can put multiple varibbales here , or use just one key variable to see the value.

#output:
#87

---------------------------------------------------------------------------------

/*************************************
 Introduction to Dictionaries:
***************************************/ 

Dictionary: It has a key and its value.it is useful in passing multiple values at the same time.

Dictionary allows user to write the data in the form of keys and values.
a) dictionaries are enclosed inside curly brackets. {}
b) Keys and values are separated by colon.
c)Every key value pair is separated by a comma (,).


/********************************
 Iterations in dictionaries: 
*********************************/

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


In dictionaries a[i] : means the complete pair that is the key and its value.
eg. "name" : "John" 
     "a" : 20



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


/********************************
 -- Dictionary functions part (1)
**********************************/ 

student={"name":"John","class":"6th","roll_no":23}
#1. get
print(student.get("name")) #helps in fecting the value of a key.
#output: John

#2. items
a=student.items() # to get both keys and items in the form of a tuple.
print(a)
#output: dict_items([('name', 'John'), ('class', '6th'), ('roll_no', 23)])

#3. keys
a=student.keys() # to get keys only.
print(a)
#output: dict_keys(['name', 'class', 'roll_no'])

#4. values
a=student.values() # to get values only.
print(a)
#output: dict_values(['John', '6th', 23])

#5. copy , this function copies the dictionary another variable/dictionary.
student={"name":"John","class":"6th","roll_no":23}
print("Original : ",student)
b=student.copy() # to get values only.
print("Copied : ",b)

# output:
# Original :  {'name': 'John', 'class': '6th', 'roll_no': 23}
# Copied :  {'name': 'John', 'class': '6th', 'roll_no': 23} 



/********************************
 -- Dictionary functions part (2)
**********************************/ 

student={"name" : "John", "class":"6th","roll_no":23}

# 1. setdefault

#The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key, with the specified value, see example #below.

#syntax
dictionary.setdefault(keyname, value)


#student={"name" : "John", "class":"6th","roll_no":23}

# 1. setdefault

#The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key(or append in the end of the string), with the specified value, see example #below.

#syntax
#dictionary.setdefault(keyname, value)

# x=student.setdefault("name","preet") # it will keep the original value John , that was assigned in the dictionary.
# print(x)
# x1=student.setdefault("lastname","Singh")
# print(x1)
# print(student)

# 2. update , it updates the dictionary , by inserting specified items to dictionary. he update() method inserts the specified items to the dictionary.

student={"name" : "John", "class":"6th","roll_no":23}
print(student)
x=student.update({"age":23})
print(x)
print(student)

#Syntax:
#1. car.update({"color": "White"})
#2. dictionary.update(iterable)

#for list remove(): removes specified item, If there are more than one item with the specified value, the remove() method removes the first occurrence
#for list The pop() method removes the specified index. eg: pop(1)
# # 3. pop : The pop() method removes the specified item from the dictionary.

x=student.pop("age")
print(x)
print(student)


# # 4. popitem : Remove the last item from the dictionary:
#
print(student)
x=student.popitem()
print(x)
print(student)

#Output:
# {'name': 'John', 'class': '6th', 'roll_no': 23}
# ('roll_no', 23)
# {'name': 'John', 'class': '6th'}
#


# # 5. clear : Remove all elements from the car list:

print(student)
x=student.clear()
print(x)
print(student)

#output:
# {'name': 'John', 'class': '6th'}
# None
# {}


/***************************************
-- Nested Dictionaries
****************************************/

# A dictionary within a dictionary is called a nested (dictionary).


dictionary_Name ={key1 :{"name":"John","age:20 } , 
	     Key2 :{"name":"Lisa", "gender":"M"} }
		

------------------
  Example:
------------------

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

---------------------------------------------------------------------------------

/*************************************
  Problem solving
**************************************/ 

1. Write a python program to sort a dictionary by value.
2. Write a python script to print a dictionary where the keys are numbers between 	1 and 15 and the values are square of keys.
3. Write a program to multiply all the items in a dictionary.
4. Write a python program to sort a dictionary by key.


In dictionaries a[i] : means the complete pair that is the key and its value.
eg. "name" : "John" 
     "a" : 20



# /*************************************
#   Problem solving
# **************************************/

# 1. Write a python program to sort a dictionary by value.
# a={"a":12,"b":23,"c":6,"d":91,"e":45}
# a=sorted(a.values())
# print("dictionary sorted by values", a)
# # output: [6, 12, 23, 45, 91]

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

--------------------------------------------------------------------------------





/*******************************
 Introduction to Sets
*********************************/ 

Sets are "unordered collection" of data. Every element inside the set is unique and mutable. Unordered means elements have no proper index assigned to it.

i) Sets are written inside the curly brackets.
ii) The value inside a set is separated by comma(,)
iii) Mutable means - once created ,they  can be changes.
iv) Elements in sets are unique and cannot be repeated. It comes only once in the set.



#1. there is no indexing and no element is ordered. So everytime we run this script it will give us different output.
a={"Ironman","Hulk","Thor","Captain America"}
print(a)
#output: {'Hulk', 'Ironman', 'Thor', 'Captain America'}
# Ran second time: {'Thor', 'Hulk', 'Captain America', 'Ironman'}

#2. Let's check the type of variable a:
print(type(a))
#output: <class 'set'>

#3. Loop
for i in a:
    print(i)  # there are no indexing hence it will print the value.





# /*************************************
#  -- Set Methods/functions - Part 1
# ***************************************/



#add : if we want to add an element in a set.
#pop : removes any random value from set because set has no index.
#remove: removes a specific value/element from set.
#discard : removes a specific value/element from set.
#copy : Copies a set into another set.




a={"Ironman","Hulk","Thor","Captain America"}

# add
a.add("Spiderman")  # it adds at any random number , because there is no indexing.
print(a)

#output: {'Ironman', 'Captain America', 'Spiderman', 'Thor', 'Hulk'}
# Ran second time: {'Spiderman', 'Ironman', 'Hulk', 'Thor', 'Captain America'}

# pop : it will remove a random value from the set eash time we run the query.
# a.pop()
# print(a)

#Output:
#Before pop (): {'Captain America', 'Hulk', 'Thor', 'Spiderman', 'Ironman'}
#After pop() : {'Hulk', 'Thor', 'Spiderman', 'Ironman'}

# remove
a={"Ironman","Hulk","Thor","Captain America"}
a.remove("Thor") # to remove a specific value.
print(a)
#output: {'Captain America', 'Ironman', 'Hulk'}

# discard : is simialr to remove, it removes a particular value from the set.
a.discard("Hulk")
print(a)

# copy : to copy a set into another set.
a={"Ironman","Hulk","Thor","Captain America"}
print("The original set",a)
b=a.copy()
print("After copying the set",b)




# /********************************
# -- set functions - Part 2
# **********************************/



#isdisjoint : Return True if no items in set B is present in set A (both sets are independent of each other).
#issubset : A complete set is a child of another set.
#issuperset : A complete set is a parent of another set.
#update : Insert the items from set y into set x ( like Merge ).
#clear : completely empty the set.





a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor"}

#Return True if no items in set B is present in set A

# 1.isdisjoint  : this method works on two or more sets. It checks for the elements of set b , if they belong to set a or not. If they don't belong it returns True else False
print(a.isdisjoint(b))
#output is : True , because elements of set B doesn't belong to set a
print(a.isdisjoint(c))
#output is : False, because elements of set B belong to set a

# 2.issubset
#Return True if all items set X are present in set Y:
#x = {"a", "b", "c"}
#y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y) #True

#Return True if all items in set c are present in set a:
#The issubset() method returns True if all items in the set exists in the specified set, otherwise it returns False.
print(c.issubset(a) ) , #means c is a child of a
#Output: True
print(c.issubset(b))
#output: False

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor"}

# 3.issuperset
#Return True if all items set y are present in set x:
# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = y.issuperset(x) #True
#Return True if all items set A are present in set C:
# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it returns False.

print(a.issuperset(c)) # means A is a parent of C
#output: True

# 4.update
#Insert the items from set y into set x:
#If an item is present in both sets, only one appearance of this item will be present in the updated set.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) # here we want to update set x with the values of set y
print(x)
#output: {'apple', 'cherry', 'banana', 'microsoft', 'google'} # any duplicate value will display only once because a set has unique elements only.

#or Use |= as a shortcut instead of update():
x |= y
print(x)

# 5.clear # removes all items from a set.
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

#output: set() , means the set is empty.






# /*****************************
# Set functions - Part 3
# *******************************/


# Union : RETURNS ALL VALUES.
# Difference : UNCOMMON VALUES FROM SET A ((creates new set))
# Difference Update : (updates existing set)
# Intersection : ONLY COMMON VALUES FROM A and B (creates new set)
# Intersection Update : (updates existing set)
# Symmetric Difference : UNCOMMON VALUES from A and B (creates new set)
# Summetric Difference update: (updates existing set)



a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor","Spiderman"}


# 1. Union : (all values from A and B + common values from both sets)
#Return a set that contains all items from both sets, duplicates are excluded:
#You can specify as many sets you want, separated by commas. It does not have to be a set, it can be any iterable object.
# If an item is present in more than one set, the result will contain only one appearance of this item.

# Example: RETURNS ALL VALUES.
# A={1,2,3}
# b={3,4,5}
# C={1,2,3,4,5}  is the output ,all elements from A and B + common elements - duplicate values appears only once.


#Syntax: set.union(set1, set2...)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
#output: {'cherry', 'banana', 'apple', 'google', 'microsoft'}


a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor","Spiderman"}

print(a.union(c))
#output: {'Ironman', 'Spiderman', 'Captain America', 'Hulk', 'Thor'}


# 2. Difference : Return a set that contains the items that only exist in set A, and not in set B (it will also exclude the common elements.):
#It returns a new set.
# Example: ONLY UNCOMMON VALUES FROM SET A
# A={1,2,3}
# b={3,4,5}
# C={1,2}  is the output

x=a.difference(c)
print(x) # created a new set x
#output: {'Ironman', 'Captain America'} # returns items from only set A


# 3. Difference Update : The difference_update() method removes the items that exist in both sets.
# it will not return new set ,rather it updates the existing set.
a.difference_update(c)
print(a)
output: {'Ironman', 'Captain America'}

#------------------------------------------
a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-Woman"}
c={"Hulk","Thor","Spiderman"}
#-----------------------------------------------

# 4. Intersection : returns only the common elements in both sets.
# it returns a new set
# Example:  ONLY COMMON VALUES
# A={1,2,3}
# b={3,4,5}
# C={3} 3, is the output
#
# x=(a.intersection(c))
# print(x)
#output: {'Thor', 'Hulk'}

# 5. Intersection Update :  it updates the same set and returns the common values of all sets.
# a.intersection_update(c)
# print(a)
#output: {'Thor', 'Hulk'}

# 6. Symmetric Difference: returns uncommon elements of set A and set B , it completely ignores the common values from both the sets.
#returns a new set
# Example: ONLY UNCOMMON VALUES /IGNORE COMMON
# A={1,2,3}
# b={3,4,5}
# C={1,2,4,5} # this will ignore common values from both the sets.

x=a.symmetric_difference(c)
print(x)
#output: {'Captain America', 'Spiderman', 'Ironman'}

# 7. symmetric Difference update: returns uncommon elements of set A and set B , ignores common elements from both sets.
# updates existing set.
print(a.symmetric_difference(c))
#output : {'Ironman', 'Spiderman', 'Captain America'}



/**************************************
  -- Functions - User created fntions
****************************************/

(i) A function is a block of code which only runs when it is called.

ii) You can pass data, known as parameters, into a function.

iii) A function can return data as a result.

iv) Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

v) Functions help break our program into smaller parts and helps it look more 
organised and manageable.

Two parts of function:
1) Define the function
2) Call the function.

#Example:
def my_function():
  print("Hello from a function")
 
my_function()  # calling a function



#Parameters: are the variables written inside the parentheses with the name of function.
#Arguments: are the values passed to the parameters while calling the function.

# example: 1
def addition(x,y): # x,y are paremeters.
    z=x+y
    print(z)
addition(5,6)  # 5,6 are arguments
#ouput: 11

# example : 2
def rect(length,width):
    print("area of rectangle is : ",length*width)
rect(10,23)  # function will do its work as many times we call it using multiple calling statements.
rect(12,14)



/************************************
Arbitrary Arguments, *args
**************************************/

If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly


 # 1. When we don't know how many arguments will be passed during function call then we put a * in front of parameter assign in the function definition.
 # 2. The calling statement will look like tuple of arguments.
 # 3. The value can be accessed as paremeter[index] in the body of the function.


Example:

def hello(*name): # use * in front of the parameter.
    print("Hello my name is : ", name[2] )  #access the values with index.
hello("John" ,"lisa","Mary","Sam")  # looks like a tuple of arguments.



# /*****************************************
# Return statement and Recursion in Python
# ******************************************/ 

Return : keyword in python is used to exit a function and return the value of the function.


#example 1:
def hello():
    return ("Hello world !!") # return keyword stores the value of the function and exits the function.

print(hello()) # if we don't use print here, nothing will be displayed in the output.

#Example 2:
def addition(a,b):
    return ("the addition of 2 numbers is: ",a+b)

print(addition(3,6))
#output: ('the addition of 2 numbers is: ', 9)

# ----------------------------------------------------------------------------
#   ---  Recursion(recursive) : which means a defined function can call itself.
# ------------------------------------------------------------------------------

# Recursion in most commonly used mathematical and programming concept
# In simple words, recursion means functions can call itself, giving us a benefit of looping through data in order to get a result.
# it's helpful when we work with series of numbers etc.
# function call is written within the function , with or without return statement.

# def hello():
#     print("Hello")
#     return hello() # this will make the function go in loop
# hello()  # function calling statement

#Output: Hello  , this will be printed multiple times.
# [Previous line repeated 996 more times] , python has 996 limit for recursive function, once it reached its limit the loop will stop.
# RecursionError: maximum recursion depth exceeded.

#--------------------------------------
# factorial of a number using recursion:
#--------------------------------------
#factorial of 3 : 3*2*1 =6
#factorial of 4 : 4*3*2*1 =24

def fact(n):
    print(n)
    if n==1:
        return 1
    else:

        return (n*fact(n-1))  # this statement will create the recursion(the function will call itself again and again)
print(fact(5)) # calling statement

#output: 120


#Another Example:
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)  # function is being called here itself unless the if condition is true.
    print(result)
  else:
    result = 0
  return result

tri_recursion(6)

#output:
# 1
# 3
# 6
# 10
# 15
# 21


/---------------------------
 -- Advantages
------------------------------/
1. They make the code look clean and organized.
2. By the use of recursive functions, a complex task can be broken down into small sub-parts.
3. Sequence generation becomes easier.

/---------------------------
 -- Dis-Advantages
------------------------------/
1. Recursive functions take up a lot of memory.
2. Sometimes the logic becomes hard to follow.
3. Difficult to debug the code using recursion.


/*************************************************
 Lambda function in python (temporary function)
***************************************************/

(i) It is used when an anonymous function is required for a short period of time.
(ii) It can take any number of arguments
(iii) But it can only have one expression.

Anonymous Function: Anonymous functions, also known as closures , allow the creation of functions which have no specified name.

---------
Syntax:
---------
lambda arguments : expression



#example 1:
a=lambda b: b*5  # lambda b:  lambda is a function + b is parameter :  #B*5 is an expression
print(a(4))
#output: 20

#example 2
x = lambda a, b : a * b
print(x(5, 6))
#output:30

# example 3
x=lambda b,c,d : b+c+d
print(x(2,3,4))
#output: 9

# example 4
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))  # here we are calling lambda function anonymously.
#output 33 


/************************************
--Local and Global Variables.
**************************************/ 

#Variable: is a container or a placeholder that can be used for storing a value.
#Local variables: are restricted to only one block of code and cannot be changed throughout the program.
#Global variables : are not restricted to one block of code and they can be changed throughout the program.
#Global variable can be defined inside or outside  a function. once declare as global it can updated/accessed throughout the program.

# Syntax for global variable:

#     global variable name
#    eg : global x

# Example:
x=24 # local variable  # this is a local variable as well
print("first variable x is   :" ,x)
def hello():
    global x # x is now a global variable
    x=25 # local variable
    return x
print("Local variable has value: ",hello())
print("Global variable: ",x) 


/**********************************
 -- Functions Problem Solving
***********************************/
1. write a function to find maximum of three numbers in python.
2. Write a python function to create and print a list where the values are square of numbers between 1 and 30.
3.write a python function that takes a number as a parameter and check if the number is prime or not.
4. Write a python function to sum all the numbers in a list.
5. write a python program to solve the Fibonacci sequence using recursion. 


# ***************************************************************************
# NOTES:
# a=[10,12,13,14]  this is a list
# for i in a  # this means i will have values from list a
# for i in range(len(a)) # this means i will have index from list a as we have used a length variable.
# for i in range(1,5) # this means i will have index value as we have given a range between 1 and 5.
#********************************************************************************



# /**********************************
#  -- Functions Problem Solving
# ***********************************/
# 1. write a function to find maximum of three numbers in python.
def maximum_num(val1,val2,val3):
    if val1>val2 and val1>val3:
        return(print(val1 ,"is the maximum of all"))
    elif val2>val3 and  val2>val1:
     return(print(val2,"is the maximum of all"))
    else:
            return(print(val3,"is the maximum value"))

maximum_num(5,7,91)
#output: 91

# 2. Write a python function to create and print a list where the values are square of numbers between 1 and 30.
def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())
#output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]

# 3.write a python function that takes a number as a parameter and check if the number is prime or not.
def prime_func(n):
    if(n==1):
        print(n , " : is not a prime number")
    for i in range (2,n):
            if(n%i==0 ):
             print(n," : is not a prime number")
             break # to come out of the loop , otherwise it keeps on printing same sence for each iteration.
            else:
              print(n, " : is  a prime number")
            break
    return n
prime_func(7)


# 4. Write a python function to sum all the numbers in a list.
def add(numbers): # complete list has been assigned to varibale number=[12,4,5,6,7,8,9] during function call.
    print(numbers)
    total=0
    for i in numbers:
        print(i)
        total=total+i
    return(total)

print("sum of all the list numbers: ", add([12,4,5,6,7,8,9]) )

# ********************************************************************
# NOTES:
# a=[10,12,13,14]  this is a list
# for i in a  # this means i will have values from list a
# for i in range(len(a)) # this means i will have index from list a as we have used a length variable.
# for i in range(1,5) # this means i will have index value as we have given a range between 1 and 5.
# *****************************************************************************************************************

#solution 2nd example using recursion
def add(numbers):
    if len(numbers)==1:
        return(numbers[0])
    else:
       return((numbers[0]) +add(numbers[1:]) ) # we have used here a recursive method to add the numbers in a list.

print(add([12,4,5,6,7,8]))


# 5. write a python program to solve the Fibonacci sequence using recursion.
# Fibonacci sequence is a sequence in which each number is the sum of the two preceding ones.

def fs(num):
    if num==1:
        return(0)
    elif num==2:
        return(1)
    else:
        return (fs(num-1)+fs(num-2))

print(fs(7))

# 0 1 1 2 3 5 8  # 7 places in fibonacci series.


------------------------------------------------------------------------------

**************************************
--- Modules
****************************************

Modules are the (.py) files, that contains set of functions you want to include in your program. Inbuilt modules are also available in python.
There are more than 200 modules available in python.
we save our module file using .py then we call it into our function.
we can also create use defined modules/


#********************************************
-- Inbuilt modules in Python - Important ones
#*********************************************

1. Datetime
2. Random
3. Math


/**********************
 -- Datetime Module
***********************/

#Import the datetime module and display the current date:

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



/*****************************
 -- Random Module
*******************************/ 

 it picks any random value

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


/*******************************
 -- Creation of Modules
********************************/ 
To create a module, all you need to do is create .py file in a similar path to your python file. Inside that file, you can add required functions you need your program to perform.

To call the module inside your program , all you need to do is use import keyword followed by the name of your .py file. 


------------------------------
-- Create 2 files.
 (i) Module_creation.py 
 (ii) demo01.py 
--------------------------------

1. Module_creation.py 
import demo  :  don't forget to import the module  here 

# here we are calling the module and printing the output.
a=demo.add(2,3)
print(a)


2.demo01.py  : use defined module.
Here we can add anything like function, lists, dictionaries and their functions. 

Example   : definition of a module here and returning the sum of x and y
def add(x,y)
return(x+y)


/*************************************
 -- Project Creation
****************************************/

https://www.kaggle.com/datasets/mojtaba142/hotel-booking

Hotel_Booking.csv

we have to find the reasons behind the cancellations.

1  Why the cancellation happening ?
2. Through whom cancellation happening ?
3. During what time period the cancellations are happening


/********************************
 Applying formulas in excel:
********************************/ 

1. we have opened a hotel_booking.csv file into excel from Power bi query editor.
2. when we are in power bi query and want to go to excel : go to-->menu bar--> close and load --> the file will open in excel.

3. Create a new column Name: room_status --> here we will apply formula.(example of if else.
if(reserved_room_type=assign_room_type,"Desired","un-Desired")

4.New column= Guest_type 
formula : if(and ) # and is for applying multiple conditions. 

eg: Conditions:
1. no of adults should be 2 and no of children should be 0, no of babies should be 0 then these are couples.
2. for singles : adults hould be 1 and babies and children should be 0.
3. Else Family : when we have 3-4 people , could be people with kids or more then 2 adults.

Column E is for adults
Column F is for children
Column G is for babies

Formula:
=if(and(E2=2,F2=0,G2=0)"Couples",if(and(E2=1,F2=0,G2=0),"Single","Family")) 



/********************************
 PIVOTING in excel:
********************************/ 
(A) Go to new sheet : Rename: Pivot
1. go to-->Insert-->Pivot table-->from table range--> select all columns and rows  of the file (or select diagonally by clicking arrow near header to select all).

Table Range=Table_hotel_bookings.
Existing workbook : select
Location: Pivot&A&1  
click : OK

------------------
Pivot sheet:
--------------------------
Pivot table sheet opens now.

-----------------------------
1. Create a pivot table:
-----------------------------
Pivot table fields:  select cloumns from right side check boxes.
and drop into boxes given on the right most of the sheet.
=Rows box (drop column guest_type here) eg: couple,family,single
=count box(drop column room_status here ) or use  column :Is_cancelled , rename: cancelled bookings.
=count box( drop column guest_type)  renamed: Total Guests 

solution: so here we found guest tepes, total guests and there cancelled bookings

---------
 Note:
---------
Pivot table analyse --> select grand total off --> grand total will disappear.

----------------------------------------------------------
2. Same pivot sheet , Create another pivot table.
----------------------------------------------------------
We can copy above table and paste below then make change in the below table.
(a) Select different columns here as desired.
=Rows(room_status) on the basis of desired or undesired room.
=count(room_status)
=count(is_cancelled) Renamed as : Cancelled bookings.

solution: so here we found that bookinng was cancelled on the  basis of desired or undesired room bookings.


-----------------------------
3. Lets create one more table.
-----------------------------
Again copy paste previous table in same sheet.

=Rows(arrival_date_month)
=count(arrival_date_month)
=count(is_cancelled) Renamed as : Cancelled bookings. 

solution: so here based on the month we found when did most people arrived and when did most bookings were cancelled.


----------------------------------------------------------
4. Another table to find ratio of hotel and resort
---------------------------------------------------------- 
(a)Copy paste the previous table in same sheet and make changes as required.

=Rows(hotel) eg: city hotel, Resort hotel
=count(hotel)

(b) for cancellations lets create another pivot table.
=Rows(hotel) eg: city hotel, Resort hotel
=count(is_cancelled) Renamed as : Cancelled bookings. 

solution : here we found :
	 1. type of hotel and their count.
         2. type of hotel and their Cancelled bookings. 


--------------------------------------------------
--5. Select Color themes for creating dashboard
--------------------------------------------------

Now we have sufficient data to create dashboard.

go to -->www.bing.com --> 
or www.colorkit.co

to select a theme template , as we want it to be colourful.
copy one color theme with 4-5 colors 
now go to excel -->pivot table sheet --> select a cell/click on empty box
now go to color Like A symbolon menu bar --> custom colors --> then paste the theme in the small box where theme name is given.

--------------------------------
Creating Dashboard
---------------------------------
go to new sheet :Rename Dashboard.

1. first select sheet and fill color : green
2. for table headers we use charts/textbox rather than selecting cells.

3. insert --> textbox -->drag it to make it big.
type Title : Hotel booking Cancellations
4. go to --> menu bar-- > shape format--> select same color -->fill-->green
5. shape format-->text fill--> light color (select the text first)
6. Home ---> Font size --> 24
7. Alignment--> center
8. sahpe outline--> no outline.

Now lets build charts.
1. go to pivot sheet.
2. select first table/ just click on a column of a table. --> then select chart
3. select bar chart.
Insert --Recomended charts --> insert chart --> select any chart here.

4. a chart appears on pivot sheet --> drag and drop to dashboard or cut paste to dashboard sheet. 
Hide all button --> select header button--> right click --> remove button.
Remove gridelines --> click on plus sign --> axes,legend
X,Y Axix title: can be renamed Manually. eg: x: Guest Type , Y: Bookings
chart background : can be changed as well : green 
Axis color: select light color.
Bar color : can be updated as well select bar and fill recent color--> orange , green.
Remove border of the chart: Format shape : no border (also appears on right side of the sheet)


Table 2 : we used pie chart.
format: change the chart color  : select original chart formart --> paste special on another chart.---> if chart type changes --> select chart and change it. 

table 3 L Pie chart , format copy paste : click + for axis names
Table 4 . Bar cahrt , Format copy paste : click on + to add data labels.

Then place all the charts in arranged manner.

--------------------------------------------
--Display aggrgate values on Dashboard
--------------------------------------------
1. on dashboard page: Insert---> textbox --> name it --> Total Bookings.
2. go to google --> hotel booking icons --> then choose one image and save it on your machine. (www.bing.com)
3. go to dashboard page --> click somewhere --> Insert --> illustrations-->pictures--> select your icon.
4. Menu bar--Picture format --> change its color type etc.
5.go to hotel_bookings sheet : Select column hotels --> it shows total count of hotels.
6. go to dashboard: insert text box --> type manually total count of hotels.
7.Copy paste all three things (picture, and 2 text box)
8. Update it for Total cancellations.
9. hotel_books heet-->is_cancelled --> select 1 , find the count : 44224

10.  Adding a Slicer: (Tiles)
go to Pivot -> inset-->slicer --> arrivale_date year
bring it on the dashboard by cut and paste. (it shows 2015,2016,2017)

Go to menu--> slicer--> change its type --> color etc.
format slicier element: font, style etc

--------------------------------
Dynamic view of the slicer.
----------------------------------

Right click on the sheet : select Remote Connections --> check box all the pivot tables on the sheet. This will help to show the dynamic changes based on the year selected in the slicer.

We can also add titles on the charts.



*****************************************
 -- Introduction to NUMPY:
******************************************
We use libraries for data analytics : 

other Libraries :  NumPy, SciPy, Visby, Pandas, Plotly, Matplotlib, Seaborn, Scikit-learn, Statsmodels, and Apache Superset.

What is Numpy ?
i) Numpy is the short form of Numerical Python.
ii) In 2005, Travis Oliphant created Numpy package.
iii) Numpy is a package that defines a multi-dimension array object and associates fast math functions that operates on arrays.

Numpy is used for : for scientific and mathematical operations.
such as :standard daviation, variance, mean ,mode,medium and many more.

iv) It also has functions for working in domain of linear algebra , fourier Transformation and matrices , transpose etc.
v) In simple words , it is the fundamental package for scientific computing in python.
 
Vi)The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements.

*******************
  Arrays:
*******************
1. An array is defined as a collection of items that are stored at the contigous memory locations.
2. It is a container which can hold a fixed number of items , and these items should be of the same type.
3. A combination of arrays saves a lot of time. The array reduce the overall size of the code.
4. Array is not comma separated. eg array[10 20 30] and are stored in the contiguous memory location. means it finds 3 empty spaces together. and won't stored in a scattered memory locations like lists, 
5.Because lists are comma separated so its values gets stored where ever it finds empty space.
6. Array can have only one type of data at one time.

Contiguous:next or together in sequence. /neighboring/sharing common border/touching. 

---------------
--NumPy
---------------
1. NumPy uses much less memory to store data.
2. NumPy makes it extremely easy to perform mathematical operations on it.
3.Used for the creation of n-dimensional arrays.
4. Finding elements in NumPy array is easy.

----------------------------------------------------------------------
1. install numpy: Go to cmd command prompt and type: pip install numpty
-----------------------------------------------------------------------
The numpy will automatically install on your machine.

2. Go to Jupyter website to write code in notebook:
https://jupyter.org/try-jupyter/lab/

3. Open - a notepad , save it as numpy.ipynb

------------------------------
Converting list into an array:
------------------------------

In Jupyter notepad: NumPy.ipynb

l1=[20,30,40]
l2=[50,60,70] 
print(l1+l2) # here it performs join operation rather than addition

#output: [20, 30, 40, 50, 60, 70]

---------------------------
Example 1: NumPy Arrays
---------------------------

import numpy as np
a=np.array([10,20,30]) # here we have converted a list into an array.
b=np.array([2,5,6,7])
print(a) 
print(b) 
print("addition result is: ",a+b) #addition

Output:
[10 20 30]
[2 5 6]
addition result is:  [12 25 36]

---------------------------
Example 2 : NumPy Arrays
----------------------------

import numpy as np
c=np.array([10,20,30])
d=np.array([2])
print(c)
print(d)
print("Multiplication result is: ",c*d) #multiplication
or
e=np.array(c*d) #this will work as well.
print(e)

Output:
[10 20 30]
[2]
Multiplication result is:  [20 40 60]

Example 3.
a=np.array([12,30,"40"]) #we here passed one variable as a string it will convert all other values to string as well.
print(a)

#output:
['12' '30' '40']

Example 4: 
b=np.array([12,30,60.55]) # We have passed float variable here
print(b) 

#output: all variables in output will have float values.
[12.   30.   60.55]



/***************************************************
-- Arrays V/S Lists or Advantages of arrays
****************************************************/
 
(i) A list cannot directly handle mathematical operations, while Array can.
(ii) An array consumes less memory than a list.
(iii) Using an array is faster than list.
(iv) A list can store different datatypes, while you can't do that in an array.
(v) we can create 2-D,3-D data arrays using NumPy arrays.
(vi) A list is easier to modify since a list store each element individually, it is easier to add and delete an element than an array does.
(vii) In lists one can have nested data with different size, while you cannot do
the same in array.

---------------
Nested list :   Two different lists can have different number/size of elements.
------------------
a=[[10,20],[30,40,50]] #nested list
print(a)
output: [[10, 20], [30, 40, 50]]


--------------
NumPy array: all nested lists in the array must be of same size (fixed size).
----------------

import numpy as np
a=np.array([10,20],[30,40,50]) # here we created nested lists/array with size 2 and 3 , and it will give us error. both lists can same either 2 elements or 3 elements.
print(a)

-------------------------
we will receive error:
-------------------------

TypeError  Traceback (most recent call last)
Cell In[19], line 2
      1 import numpy as np
----> 2 a=np.array([ [10,20],[30,40,50] ])
      3 print(a)

TypeError: Field elements must be 2- or 3-tuples, got '30'

-------------------
Better version: Numpy nested array , with same size of elements.
---------------------
import numpy as np
a=np.array([[10,20,30],[40,50,60]])
print(a)
#output:  [[10 20 30]
 	  [40 50 60]]

Timing: 10:44:19









 


































































































































