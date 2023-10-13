"""
Dr. Sobhan Esmaeili | Postdoctoral Researcher in Computer and Telecommunication Networks
Statistical Pattern Recognition | Session 01
"""
# Checking a Version Number
# python --version
# -------------------------

# Clearing the Terminal Output
# cls
# -------------------------

# Using the Python Shell
# copyright
# credits
# -------------------------

# Writing Your First Line of Python
# print("Hello World")
# print("▬" * 23) # Alt + 22
# print("\t", "1", "\n\t", "2", "\n\t", "3")
# print("\t" * 5, "1", "\n" * 4, "\t", "2", "\n\t", "3")
# -------------------------

# Exiting the Python Shell
# exit()
# -------------------------

# Line Numbers Introduced
# 27| ←
# 1| # this is the first line in the cell
# 5| # this is the fifth line in the cell
# -------------------------

# Writing Comments
# this is a comment
# print("Hello") # this is also a comment
"""
This is a multi-Line comment
"""
# -------------------------

# Data Types
# Data Types    Sample Value       Description
#  Integer           5            Whole numbers
#   Float           5.7          Decimal numbers
#  Boolean         True       True or False values
#  string         "hello"   Characters within quotes
# -------------------------

# The Print Statement
# Integer
# print(2)
# Floats
# print(10.953)
# Booleans
# print(True)
# Strings
# print(" ")
# print("Sobhan Esmaeili")
# -------------------------

# Type Checking
# type(int)
# -------------------------

# Variables
# variable_01 = 1
# print(variable_01)
# variable_02, variable_03 = "A", "5"
# print(variable_02, variable_03)

# Handling Naming Errors
# variable_01 = 1
# print(Variable_01)

# Integer and Float Variables
# num_01 = 2
# num_02 = 2.5
# print(num_01, num_02)

# Boolean Variables
# switch = True
# print(switch)

# String Variables
# name = 'Sobhan Esmaeili'
# student_number = "20202"
# print(name, student_number)

# Using Multiple Variables
# num_01 = 1
# num_02 = 1
# result = num_01 + num_02
# print(result)
# print(num_01 + num_02)


# Using Operators on Numerical Variables
# Adding, Deleting, Multiplying, Dividing From a Variable
# result = 1
# num_01 = 2
# result += 1  # Same as Saying result = result + 1
# print(result)
# result *= num_01  # Same as Saying result = result * num1
# print(result)

# Overwriting Previously Created Variables
# Defining a Variable and Overwriting It's Value
# name = 'Sobhan'
# print(name)
# name = 'Sepehr'
# print(name)

# Whitespace
# name = "Sobhan Esmaeili"

# String Concatenation
# Using the addition operator without variables
# name = "Sobhan" + " " + "Esmaeili"
# name = 'Sobhan' + ' ' + 'Esmaeili'
# print(name)

# using the addition operator with variables
# first_name = "Sobhan"
# last_name = "Esmaeili"
# full_name = first_name + " " + last_name
# print(full_name)

# Formatting Strings (3.8)
# Injecting Variables Using the Format Method
# name = "Sobhan"
# print("Hello {0}".format(name))
# print('Hello {0}, you are {1} years old!'.format(name, 38))

# Formatting Strings (3.6)
# Injecting Variables Using the Format Method
# name = "Sobhan"
# print("Hello {}".format(name))
# print('Hello {}, you are {} years old!'.format(name, 38))

# using the new f strings (3.6)
# name = "Sobhan"
# print(f"Hello {name}")

# String Index
# Using Indexes to Print Each Element
# word = "Sobhan Esmaeili"
# print(word[0])
# print(word[1])
# print(word[-1])

# String Slicing
# word = "Sobhan Esmaeili"
# print(word[0:3:1])

# String Manipulation
# using the title method to capitalize a string
# name = "sobhan esmaeili"
# print(name.title())

# Replacing an Exclamation Point With a Period
# words = "Hello Sobhan!"
# print(words.replace("!", "."))

# Finding the Starting Index of our Searched Term
# words = "Sobhan Esmaeili"
# print(words.find("Esmaeili"))

# removing white space with strip
# name = " Sobhan "
# print(len(name))
# print(name.strip())
# print(len(name.strip()))

# name = " Sobhan "
# print(name.lstrip())
# print(name.rstrip())

# Converting a String Into a List of Words
# words = "0 1 2 3 4 5 6 7 8 9"
# print(words.split(" "))

# Accepting User Input
# accepting and outputting user input
# print(input("What is your name? "))

# saving what the user inputs
# answer = input("What is your name? ")
# print("Hello {0}!".format(answer.title()))

# Checking the Type
# how to check the data type of a variable
# num_01 = 5
# print(type(num_01))

# Converting Data Types
# num_01 = "10"
# num_01 = int(num_01)  # re-declaring num to store an integer
# print(type(num_01))  # checking type to make sure conversion worked
# num_01 = 10
# num_01 = str(num_01)
# print(type(num_01))
# num_01 = 2.5
# num_01 = int(num_01)
# print(type(num_01))
# print(num_01)
# num_01 = True
# num_01 = int(num_01)
# print(type(num_01))
# print(num_01)
# num_01 = 0
# num_01 = bool(num_01)
# print(type(num_01))
# print(num_01)
# num_01 = 2
# num_01 = float(num_01)
# print(type(num_01))
# print(num_01)


# Converting User Input
# working with user input to perform calculations
# answer = input("Type a number to add: ")
# print(type(answer))  # default type is string, must convert
# result = 100 + int(answer)
# print("100 + {0} = {1}".format(answer, result))

# Handling Errors
# try:
#     answer = float(input("Type a number to add: "))
#     print("100 + {0} = {1}".format(answer, 100 + answer))
# except:
#     print("You did not put in a valid number!")
# # without try/except print statement would not get hit if error occurs
# print("The program did not break!")

# If Statements
# using an if statement to only run code if the condition is met
# x, y = 5, 10
# if x < y:
#     print("x is less than y")

# Comparison Operators
# == equality if x == y: if x is equal to y
# != Inequality if x != y: if x does not equal y
# > Greater than if x > y: if x is greater than y
# < less than if x < y: if x is less than y
# >= Greater or equal if x >= y: if x is greater or equal to y
# <= less or equal if x <= y: if x is less or equal to y

# checking user input
# answer = int(input("What is 5 + 5? "))
# if answer == 10:
#     print("You got it right!")

# Logical Operator "and"
# using the keyword 'and' in an 'if statement'
# x, y, z = 5, 10, 5
# if x < y and x == z:
#     print("Both statements were true")

# Logical Operator "or"
# using the keyword 'or' in an 'if statement'
# x, y, z = 5, 10, 5
# if x < y or x != z:
#     print("One or both statements were true")





##########################################################################################
# Home Work
# netsh wlan show all (CMD Command)
# import subprocess
# meta_data = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"])
# print(meta_data)

# 1)Number of Visible Networks
# 2)Network Type
# 3)Authentication
# 4)Encryption
# 5)SSID
# 6)Signal
# 7)Radio Type
# 8)Channel
# 9)Basic Rate (Mbps)
# 10)Other Rate (Mbps)
# 11)MAC Address
##########################################################################################
# Contact Info:
# Email: S.Esmaeili@umail.umz.ac.ir
# Cellphone: +989122123203
##########################################################################################