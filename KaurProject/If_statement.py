# 1. If statement
marks=97

if marks>=90:
    print("You are eligible to enroll in science")

print("thank you")




#2. If-else statement

marks=80
if marks>=90:
    print("You are eligible")
else:
    print("You are not eligible")
print("thank you")



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

# 5. Short hand if statement (write the if condition and the statement in the same line)

marks=87
if(marks >= 85): print("You are eligible for buying a dictionary")


# 6.  Short hand if else statement (write the if condition and the statement in the same line - no colon used in syntax)
marks=90
print("you are going on a trip") if (marks>=85) else print("You have won the championship")

