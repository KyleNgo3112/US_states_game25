import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()

guess_state = []
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

while len(guess_state) < 50:
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guess_state]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_need_to_learns.csv")
        break
    # If user answer is in the list of states
    answer_state = answer_state[0].upper() + answer_state[1:].lower() if " " not in answer_state else answer_state
    if answer_state in states_list:
        #create a turtle to write the name of the state to right location
        guess_state.append(answer_state)
        name_write = turtle.Turtle()
        name_write.hideturtle()
        name_write.penup()
        states_data = data[data.state == answer_state]
        name_write.goto(states_data.x.item(), states_data.y.item())
        name_write.write(answer_state)
        answer_state = screen.textinput(title=f"{len(guess_state)}/50 States Correct", prompt="What's another state's name?").title()
    else:
        if len(guess_state) == 0:
            answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
        else:
            answer_state = screen.textinput(title=f"{len(guess_state)}/50 States Correct", prompt="What's another state's name?").title()

            

