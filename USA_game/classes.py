from turtle import Turtle
import pandas
data=pandas.read_csv("50_states.csv")
class mouse:
    def __init__(self):
        self.body=[]
    def creating_new_turtle(self):
        mouse=Turtle()
        mouse.hideturtle()
        mouse.penup()
        self.body.append(mouse)
    def move(self,position):
        self.body[-1].goto(position)
    def write_state_name(self,state_name):
        self.body[-1].write(f"{state_name}")
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
    def update_score(self):
        self.score+=1
class referee():
    def __init__(self):
        self.user_answer=""
        self.states_names=[]
        self.states_positions=[]
    def Fill_out_names_list(self):
        for x in range(len(data["state"])):
            state_name=data["state"][x].lower()
            self.states_names.append(state_name)
        x+=1
    def Fill_out_positions_list(self):
        for position in range(len(data["x"])):
            state_position=(data["x"][position],data["y"][position])
            self.states_positions.append(state_position)
        position+=1
    def asking_user(self,sc,score):
        self.user_answer=sc.textinput(title=f"{score}/50 correct",prompt="guess a state")
    def check_user_answer(self,m,sc):
        if self.user_answer.lower() in self.states_names:
            index=self.states_names.index(self.user_answer)
            position=self.states_positions[index]
            sc.update_score()
            sc.write
            m.creating_new_turtle()
            m.move(position)
            m.write_state_name(self.user_answer.lower())
            self.states_names.remove(self.user_answer.lower())
            self.states_positions.remove(position)
    def check_win(self):
        if len(self.states_names)==0:
            return True
        else:
            return False

        