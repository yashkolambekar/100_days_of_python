# Day 9 let's try to do 2 days' work today! 

########################################################### DICTIONARIES

# dictionary_of_states = {
#     "Maharashtra": "Nice state, unsaid financial hub of India",
#     "Uttar Pradesh": "Growing economy under the Yogi Ji",
#     "Uttarakhand": "Dev Bhoomi",
#                   }

# for state in dictionary_of_states:
#     print(state)


########################################################### GRADING PROGRAM

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score >= 91:
#         student_grades[student] = "Outstanding"
#     elif score >= 81:
#         student_grades[student] = "Exceeds Expectations"
#     elif score >= 71:
#         student_grades[student] = "Acceptable"
#     elif score <= 70:
#         student_grades[student] = "Fail"

# print(student_grades)


########################################################### DICTIONARY IN LIST

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
#     {
#         "country": "India",
#         "visits": 108,
#         "cities": ["Mumbai", "Gurgaon", "Shillong"]
#     }
# ]

# def add_new_country(name, visits, cities):
#     travel_log.append({
#         "country": name,
#         "visits": visits,
#         "cities": cities
#     })

# add_new_country("Russia", 12, ["Moscow", "Saint Petersberg"])

# print(travel_log)


########################################################### BLIND AUCTION PROGRAM

import os

print("Welcome to the online blind bidder!")

bids = []

def add_bid():
    name = input("What is your name? ")
    amount = int(input("Please your bid ammount: $"))
    bid = {
        "bidder": name,
        "amount": amount
    }
    bids.append(bid)

def declare_winner():
    max_bid = 0
    max_pos = 0
    pos = 0
    for bid in bids:
        if bid["amount"] > max_bid:
            max_bid = bid["amount"]
            max_pos = pos
        pos += 1
    
    winner = bids[max_pos]
    print(f"The winner is {winner['bidder']} with a bid of ${winner['amount']}")


def start_bidder():
    add_bid()
    selection = input("Are there more bidders? 'yes' or 'no': ")
    if selection == "yes":
        os.system('cls')
        start_bidder()
    elif selection == "no":
        declare_winner()

start_bidder()