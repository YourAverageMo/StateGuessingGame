import csv
import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("./blank_states_img.gif")
screen.setup(height=491, width=725)
turtle.shape("./blank_states_img.gif")

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's Another States's Name").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_date = pandas.DataFrame(missing_states)
        new_date.to_csv("States_to_Learn")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        guessed_states.append(state_data.state.item())
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())


screen.exitonclick()
