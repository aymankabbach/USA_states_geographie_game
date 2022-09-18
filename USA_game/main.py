from classes import mouse, referee, scoreboard
import turtle
screen=turtle.Screen()
EndoftheGame=False
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
my_mouse=mouse()
my_referee=referee()
my_score=scoreboard()
my_referee.Fill_out_names_list()
my_referee.Fill_out_positions_list()
screen.listen()
screen.onkey(my_mouse.move,"space")
screen.update()
def start_game():
    global EndoftheGame
    while EndoftheGame==False:
        my_referee.asking_user(screen,my_score.score)
        my_referee.check_user_answer(my_mouse,my_score)
        EndoftheGame=my_referee.check_win()
start_game()
screen.exitonclick()