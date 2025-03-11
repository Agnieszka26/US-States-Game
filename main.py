import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get coordinate values for states
# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)


#1. Convert the guess to title case
#2. check if the guess is among the 50 states
#3. Write correct guesses onto the map
#4. Use a loop to allow the user to keep guessing
#5. Record the correct guesses in a list
#6. Keep track of the score
def state_name_print(x,y):
    print_s=turtle.Turtle()
    print_s.hideturtle()
    print_s.penup()
    print_s.goto((coordinate_x, coordinate_y))
    print_s.write(f"{answer_state}", align=ALIGNMENT, font=FONT)

correct_user_guesses = []
states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
title="Guess the state"
score = 0
game_on = True

while game_on:
    answer_state = screen.textinput(title=title, prompt="What is another state's name?").title()

    if answer_state == "Exit":
        print("Game Over!")
        break

    for state in states_list:
        if answer_state == state and answer_state not in correct_user_guesses:
            coordinate_x = states_data[states_data.state == answer_state].iloc[0]["x"]
            coordinate_y = states_data[states_data.state == answer_state].iloc[0]["y"]
            correct_user_guesses.append(answer_state)
            state_name_print(coordinate_x, coordinate_y)
            score+=1
            title=f"{score}/50 States correct!"

turtle.mainloop()
