import turtle
import pandas as pd
from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image_path = "blank_states_img.gif"
screen.addshape(image_path)

turtle.shape(image_path)

# def get_mouse_click_coor(x, y):
#   print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)  

# turtle.mainloop()

states = pd.read_csv("50_states.csv")
# all_states = states[states.state == "Alabama"]


# all_states = states["state"].to_list()
# print(all_states)


guessed_states = []
while len(guessed_states) < 50:
  answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

  if answer_state == "Exit":
    missing_states = [state for state in states.state.values if state not in guessed_states]
    new_data = pd.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")
    break

  if answer_state in states.state.values:
    guessed_states.append(answer_state)
    state_data = states[states.state == answer_state]
    State(state_data.x.item(), state_data.y.item(), answer_state).write(answer_state)
    # print("You've guessed a state")
  # else:
  #   print("You've guessed a wrong state")

# screen.exitonclick()
