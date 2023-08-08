# Let's go Day 5, new beginnings


############################################# FOR LOOP

# states = ["Maharashtra", "Goa", "Gujurat", "Haryana", "Uttarakhand"]
# for item in states:
#     print(f"{item} great")
# print(states)


############################################# AVERAGE HEIGHT OF STUDENTS

# student_heights = [180, 124, 165, 173, 189, 169, 146]
# total_heights = 0

# for height in student_heights:
#     total_heights += height

# average_height = round(total_heights / len(student_heights))

# print(average_height)


############################################# HEIGHEST SCORE IN THE CLASS

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# highest_score = 0

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
    
# print(f"The highest score in the class is {highest_score}")


############################################# FOR LOOP WITH RANGE FUNCTION

# for number in range(0, 10, 2):
#     print(number)


############################################# ADDING FROM 1 to 100

# final_sum = 0

# for number in range(1, 101):
#     final_sum += number

# print(f"The sum of numbers from 1 to 100 is {final_sum}")


############################################## SUM OF EVEN NUMBERS FROM 1 TO 100
# INCLUDING 1 AND 100

# final_sum = 0

# for number in range(2, 101, 2):
#     final_sum += number

# print(f"The sum of even numebers from 1 to 100 including both the last numbers is {final_sum}")


############################################## FIZZ BUZZ

# for number in range(1, 101):
#     if (number % 3 == 0) and (number % 5 == 0):
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


############################################## RANDOM PASSWORD GENERATOR

# import random

# chars = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
# ['!', '#', '$', '%', '&', '(', ')', '*', '+']]

# choices = [ int(input("How many letters do you want in your password? ")),
# int(input("How many numbers do you want in your password? ")),
# int(input("How many symbols do you want in your password? ")) ]

# password_list = []

# counter_1 = 0
# for option in choices:
#     for i in range(0, option):
#         password_list.append(random.choice(chars[counter_1]))
#     counter_1 += 1
    
# random.shuffle(password_list)

# final_password = ""
# for char in password_list:
#     final_password += char

# print(final_password)


###############################################################################

# Day 5 done, planning to do more today itself!