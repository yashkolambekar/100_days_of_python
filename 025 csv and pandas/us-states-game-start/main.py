import pandas
import turtle

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# answer_state = screen.textinput(title="Guess a state", prompt="What's another state's name?")
# print(answer_state)

states_data = pandas.read_csv("50_states.csv")

result_dict = {}
for index, row in states_data.iterrows():
    state = row['state']
    x = row['x']
    y = row['y']
    result_dict[state] = {'x': x, 'y': y}

print(result_dict)

guessed_states = 0
while guessed_states < 50:
    answer_state = screen.textinput(title="Guess a state", prompt="What's another state's name?")
    if answer_state in result_dict :
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(result_dict[answer_state]["x"], result_dict[answer_state]["y"])
        t.write(answer_state)

        guessed_states += 1
    else:
        print("Does not exists")

print("You win!!!")

screen.exitonclick()