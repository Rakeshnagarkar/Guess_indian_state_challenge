import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess indian state")
image = "temp_image.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("36_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 35:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/35 States Correct",
                                    prompt="What's another state's name?").title()
    
    
    if answer_state == "Exit":
        
        #using List comprehesion
        missing_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn_in_india.csv")
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(float(state_data.x)), int(float(state_data.y)))
        t.write(answer_state)
        
if len(guessed_states) == 35:
    print("Congratulations! You know all Indian states and union territories.")  
    
    
      