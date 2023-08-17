# Second session of today
# First Capstone project, I don't know what it is

import random
import os

cards = [2, 3 ,4, 5 ,6 ,7 ,8 ,9 ,10 ,"K", "J", "Q", "A"]

def draw_new(score):
    card =  random.choice(cards)
    card_value = 0
    if card == "K" or card == "J" or card == "Q":
        card_value = 10
    elif card == "A":
        if not(score + 11 > 21):
            card_value = 11
        else:
            card_value = 1
    else:
        card_value = card
    
    return {
        "card": card,
        "value": card_value
    }


def draw_initial():
    score = 0
    cards_drawn = 0
    cards_list = []
    while cards_drawn <= 1:
        card = random.choice(cards)
        if card == "K" or card == "J" or card == "Q":
            card_value = 10
        elif card == "A":
            if not(score + 11 > 21):
                card_value = 11
            else:
                card_value = 1
        else:
            card_value = card
        if not (card_value + score > 21):
            score += card_value
            cards_list.append(card)
            cards_drawn += 1

    output= {
        "cards": cards_list,
        "score": score
    }

    return output
        
def play():

    os.system("cls")

    def reveal_scores():
        print(f"\nYour score is {player['score']} and computer's score is {computer['score']}\nYou had {player['cards']} and computer had {computer['cards']}")

    def check_win():
        reveal_scores()
        if(computer["score"] == 21):
            print(f"Computer hit a blackjack! Computer cards: {computer['cards']}")
            print("Computer wins")
        elif(player["score"] == 21):
            print(f"You hit a black jack! Your cards: {player['cards']}")
            print("You win")
        else:
            if player["score"] > computer["score"]:
                print("You won!")
            elif player["score"] < computer["score"]:
                print("Computer won!")
            elif player["score"] == computer["score"]:
                print("It's a draw")

    print("Welcome to the new game of the Blackjack")

    computer = draw_initial() 
    player = draw_initial()

    nobody_has_won = True

    while nobody_has_won:
        print(f"Your cards: {player['cards']}, your score: {player['score']}")
        comp_hidden = [*computer["cards"]]
        comp_hidden[len(comp_hidden) - 1] = "#"
        print(f"Computer's cards = {comp_hidden}")
        new_or_show = input("\nDo you want to draw a new card (y) or show (n): ")
        if new_or_show == "y":
            new_card = draw_new(player["score"])
            player["cards"].append(new_card["card"])
            player["score"] += new_card["value"]
            if player["score"] > 21:
                reveal_scores()
                print("Your score exceeded 21, computer won!")
                nobody_has_won = False
        else:
            nobody_has_won = False
            check_win()
        
    replay_question = input("\nDo you want to play again? y or n: ")
    if replay_question == "y":
        play()
    else:
        exit()

play()