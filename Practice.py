# # First Python Program
# print("Hello World")
# print(5)
# print(17*3)

# # Comments, Escape Sequences & Print Statement
# """
# Hey Abdullah,This  
# is comment 
# Line pls donot uncomment
# """

# # Hey Abdullah,This  
# # is comment 
# # Line pls donot uncomment

# print("Hello Abdulla ,How is your day? \nand best wish for tomorrow...")

# print("Hello Abdulla ,\"How is your day?\" \nand best wish for tomorrow...")

# print("Hey",6,7)
# print("Hey",6,7, sep="~")
# print("Hey",6,7, end="009\n")
# print("Abdullah")


# # Variables and Data Types 
# a=10
# b=True
# c=6.88877
# d="Python Programing"

# print(a,b,c,d)

# a1=23
# a2=89
# print(f"The Result Of Two Number is {a1 + a2}")

# print("The type of a is" ,type(a))
# print("The type of b is" ,type(b))
# print("The type of c is" ,type(c))
# print("The type of d is" ,type(d))

# # list -- ordered collection of data and mutable  
# list1=[8,7.3,[4,"Hello"],["Morning",'Night']]
# print(list1)

# # tule--- ordered collection of data and Unmutable  
# tuple1=(8,7.3,[4,"Hello"],["Morning",'Night'])
# print(tuple1) 

# # Dictionary -- Key Vlue pair Unordered collection of data 
# dict1={
#     "Name":"Python",
#     "Age":23,
#     "Gender":"Male"
#     }
# print(dict1)


# # Operators
# # Arithmetic Operators
# a=78
# b=20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)

# # Relational Operators
# print(a>b)

# # Logical Operators
# print(a>b and a<b)

# # Bitwise Operators
# print(a&b)

# # Assignment Operators
# a4=10
# a4+=10
# print(a4)

# # Taking User Inpu
# x=input("Enter Your Name:")
# print("Good Morning",x)

# x1=input("Enter First Number")
# x2=input("Enter Second Number")
# print(int(x1) + int(x2));

# If Else Conditional Statements
# a=int(input("Enter Your Age:"))
# if(a > 18):
#     print("You are eligible for voting")

# else:
#     print("You are not eligible for voting")
# print("Your Age Is:",a)


# number=int(input("Enter A Number:"))
# if(number > 0):
#     print("Positive Number")

# elif(number == 0):

#     print("Number is equal")
# else:
#     print("Negative Number")

# num=int(input("Enter A number :"))

# if(num < 0):
#     print("Number Is Negative")
# elif(num > 0):
#     if(num <=10):
#         print("Number is between 1-10")
#     elif(num >=11 and num <=20):
#         print("Number is between 11-20")
#     else:
#         print("Number is between 21-100")
# else:
#     print("Number is Zero")


# Loops

name="Jonathan"
for i in name:
    print(i ,end=", ")
    if i=="a":
        print("This is beyond the Knowledge")

colors=["Red","Green","Blue","Purple"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(1,10,4):
    print(k+1)








