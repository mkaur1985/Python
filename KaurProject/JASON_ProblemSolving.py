
# /**************************************
# Convert Python data into Jason format
#                  and
# Convert Jason data into Python format
# ***************************************/

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