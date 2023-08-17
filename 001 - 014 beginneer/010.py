# Let's try to grind more today!
# Let's try to complete the Beginners today

########################################################### FUNCTION WITH OUTPUT (RETURN)

# def format_name(firstname, lastname):
#     '''Hello Duniya'''
#     return firstname.capitalize() + " " + lastname.capitalize()

# yash = format_name("yAsh", "KOLAMBEKAR")
# print(yash)

########################################################### LEAP YEAR CHECKER

# def is_leap_year(year):
#     if (year % 4 == 0) and (year % 100 != 0):
#         return True
#     elif (year % 100 == 0) and (year % 400 == 0):
#         return True
#     else:
#         return False
    
# year = int(input("Enter a year: "))
# print(is_leap_year(year))


########################################################### CALCULATOR PROJECT

# import os

# def add(n1, n2):
#     """Adds the given numbers n1 and n2"""
#     return (float(n1) + float(n2))

# def sub(n1, n2):
#     """Subtracts n2 from n1"""
#     return (float(n1) - float(n2))

# def mul(n1, n2):
#     """Multiplies the inputs n1 and n2"""
#     return (float(n1) * float(n2))

# def div(n1, n2):
#     """Divides n1 by n2"""
#     return (float(n1) / float(n2))

# def calculator_start(n1_inp):
#     os.system("cls")
#     if(n1_inp != "none"):
#         n1 = n1_inp
#     else:
#         n1 = input("Enter your first number: ")

#     print("Please select from the below operations\n+\n-\n*\n/\n")
#     operation = input("Enter your operation: ")

#     n2 = input("Enter your second number: ")
#     result = ""

#     if operation == "+":
#         result = add(n1, n2)
#     elif operation == "-":
#         result = sub(n1, n2)
#     elif operation == "*":
#         result = mul(n1, n2)
#     elif operation == "/":
#         result = div(n1, n2)
    
#     print(f"Successfull: {str(n1)} {operation} {str(n2)} = {str(result)}")
    
#     choice = input("Press y to continue performing operations on the result or n to start new: ")

#     if choice == "y":
#         calculator_start(result)
#     else:
#         calculator_start("none")

# calculator_start("none")


########################################################### SIMPLE EVAL FUNCTIONS

# def eval_fun():
#     print(eval(input("Enter an operation: ")))
#     eval_fun()

# eval_fun()