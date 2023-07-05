from turtle import Turtle


class Invader(Turtle):

    def __init__(self, position):
        super().__init__()
        
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.goto(position)
        self.x_move = 10
        self.y_move = 10

    def move_side(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())
    

    def move_side_back(self):
        self.x_move *= -1

