# user_counter = 0
 
# class User:

#     def __init__(self, username):
#         global user_counter
#         user_counter += 1
#         self.user_number = user_counter
#         self.username = username
        

# user_1 = User("classicaf") 

# user_2 = User()

# print(f"{user_1.username}, count = {user_1.user_number}")
# print(f"{user_2.username}, count = {user_2.user_number}")

# class Car:

#     def __init__(self):
#         self.seats = 4
    
#     def enter_race_mode(self):
#         self.seats = 2

# supra = Car()
# supra.enter_race_mode()
# print(supra.seats)

# users_counts = 0

# class User:

#     def __init__(self, username):
#         global users_counts
#         users_counts += 1
#         self.id = users_counts
#         self.username = username
#         self.followers = 0
#         self.following = 1

#     def follow(self, to_follow):
#         to_follow.followers += 1
#         self.following += 1
#         print(f"{self.username} started following {to_follow.username}")

# yash = User("classicaf")
# sai = User("saichandarkar")

################################################# QUIZ GAME

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# import os

question_bank = []

for i in question_data:
    # question_bank.append(Question(i["text"], i["answer"]))
    question_bank.append(Question(i["question"], i["correct_answer"]))

my_quiz = QuizBrain(question_bank)

while my_quiz.questions_left():
    my_quiz.next_question()

print(my_quiz.score)