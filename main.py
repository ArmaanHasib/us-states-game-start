import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed_states = []

data = pandas.read_csv("50_states.csv")

state_list = data["state"].to_list()
# print(state_list)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is another state's name?")
    guess = answer_state.title()

    if guess == "Exit":
        missed_states = [state for state in state_list if state not in guessed_states]
        # for state in state_list:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if guess in state_list:
        guessed_states.append(guess)
        my_turtle = turtle.Turtle()
        my_turtle.penup()
        my_turtle.hideturtle()
        state_data = data[data.state == guess]
        my_turtle.goto(int(state_data.x), int(state_data.y))
        my_turtle.write(guess)

# missed_states = state_list
#
# for state in guessed_states:
#     if state in missed_states:
#         state_index = missed_states.index(state)
#         del missed_states[state_index]

# print(missed_states)

# states_to_learn = pandas.DataFrame(missed_states)
# states_to_learn.to_csv("states_to_learn.csv")






