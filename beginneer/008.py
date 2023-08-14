# Day 8, physical and mental tension building, but let's fucking GOOOO  

########################################################### FUNCTIONS WITH PARAMETERS

# def greet(name):
#     print(f"Hello Mr. {name}")
#     print("Welcome to the Greet Function")
#     print("I see that you are going to be the greatest coder ever")

# greet(input("What is your name dear sir? "))
# greet("Donald Trump")


########################################################### FUNCTIONS WITH MULTIPLE PARAMS

# def greet_with_params(name="James Smith", location="North Pole"):
#     print(f"Hello {name}, how's everything going on in {location}")

# greet_with_params("Vladimir Putin", "Moscow")
# greet_with_params("Donalad Trump", "Washington DC")
# greet_with_params(location="Mumbai", name="Yash")


########################################################### AREA CALCULATION FUNCTION

# def area_calculator(height, width, coverage):
#     import math

#     print(math.ceil((float(height) * float(width)) / float(coverage)))

# area_calculator(3, 1, 0.3)


########################################################### PRIME NUMBER CHECKER

# def is_prime_number(number):
#     for i in range(2, number):
#         if number % i == 0:
#             print("Not a prime number")
#             exit()
#     print("It's a prime number")
        

# is_prime_number(101)


########################################################### CAESAR CIPHER

alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

def encoder(message, shift): 
    message_list = list(message.upper())
    encrypted_message = ""

    for i in range(len(message_list)):
        if(message_list[i] == " "):
            encrypted_message+= " "
        else:
            index = alphabets.index(message_list[i])
            encrypted_index = index + shift
            if encrypted_index > 25:
                encrypted_index -= 26
                encrypted_message += alphabets[encrypted_index]
            elif encrypted_index < 0:
                encrypted_index += 26
                encrypted_message += alphabets[encrypted_index]
            else:
                encrypted_message += alphabets[encrypted_index]

    print(f"{encrypted_message}\n")

def decoder(message, shift):
    shift = -shift
    encoder(message, shift)

def enc_or_dec():
    answer = input("Your want to 'encode' or 'decode'? ")
    if answer == "encode":
        message = input("What is your message? ")
        shift = int(input("How much shift do you want? "))
        encoder(message, shift)
    elif answer == "decode":
        message = input("What is your message? ")
        shift = int(input("How much shift do you want? "))
        decoder(message, shift)
    resume = input("Do you want to use again? 'yes' or 'no': ")
    if resume == "yes":
        enc_or_dec()
    else:
        exit()

print("Welcome to the CAESAR CIPHER")
enc_or_dec()