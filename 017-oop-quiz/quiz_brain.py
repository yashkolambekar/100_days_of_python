import os
import time

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        time.sleep(2)
        os.system("cls")
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)? ")
        if(current_question.answer == current_answer):
            self.score += 1
            print("Correct Answer!")
        else:
            print("Incorrect!!!")



    def questions_left(self):
        if len(self.question_list) - self.question_number <= 0:
            return False
        else:
            return True