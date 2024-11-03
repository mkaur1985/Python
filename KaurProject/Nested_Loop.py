
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
#1
#1   2
#1   2   3
#1   2   3   4
#1   2   3   4   5
