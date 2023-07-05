from turtle import Turtle

#### MY SHOTS
class Shot(Turtle):

    def __init__(self, position):
        super().__init__()
        # self.shape()
        self.color("green")
        
        self.penup()
        self.y_move = +20
        self.left(90)
        self.goto(position)


    

    def move_shot(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    


#### INVADERS SHOTS BACK
class ShotInvader(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("red")
        self.penup()
        self.y_move = -20
        self.left(-90)
        self.goto(position)


    def move_shot_invader(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

