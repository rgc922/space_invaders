from turtle import Turtle

STEP = 20

class Ship(Turtle):

    def __init__(self, position):
        super().__init__()
        # self.color("white")
        
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.goto(position)
        
    def go_left(self):
        if self.xcor() > -335:
            self.goto(self.xcor() - STEP, self.ycor())


    def go_right(self):
        if self.xcor() < 335:
            self.goto(self.xcor() + STEP, self.ycor())
        
        

class ShipLives(Turtle):

    def __init__(self, position):
        super().__init__()
        # self.color("white")
        
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(position)