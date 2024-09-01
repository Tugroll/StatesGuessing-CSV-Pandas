import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)



data = pandas.read_csv("50_states.csv")


#We included it in the list to reach the row containing the states.
state_list = data.state.to_list()

guessed_states = []



while len(guessed_states) < 50:
    answer_state = screen.textinput("Guess", "Guess one of the states").lower().capitalize()
    if answer_state == "Exit":
        un_guessed_states = []
        for state in state_list:
            if state not in guessed_states:
                un_guessed_states.append(state)

        pandas.DataFrame(un_guessed_states).to_csv("un_guessed_states_csv")



        break
    if answer_state in state_list:
         guessed_states.append(answer_state)
         t = turtle.Turtle()
         t.hideturtle()
         t.penup()
      #When the condition is met and the answer we gave matches the state name in the data, we transferred this data row to the state data.
         state_data = data[data.state == answer_state]

         t.goto(state_data.x.item(), state_data.y.item())
         t.write(answer_state)

     #Finally, we moved the text to its location on the map by reaching the x,y values in the correct row  we transferred.

#unguessed_states.csv


turtle.exitonclick()
