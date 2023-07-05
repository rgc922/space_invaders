from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, high_score):
        super().__init__()
        self.current_score = 0
        self.high_score = high_score

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)

        self.string = "Lives:         Score: " + str(self.current_score) + \
                    "       High Score: " + str(self.high_score)
        self.write(self.string, font=FONT, align=ALIGNMENT)


    
    def increase_score(self):
        self.clear()
        
        self.current_score += 1
        # self.increase_high_score()
        self.string = "Lives:           Score: " + str(self.current_score) + \
                    "         High Score: " + str(self.high_score)
        self.write(self.string, font=FONT, align=ALIGNMENT)


    def increase_high_score(self):
        # self.clear()
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            # self.current_score = 0
            # self.increase_score()


    def game_over(self):
        self.clear()
        
        
        self.increase_high_score()

        # self.goto(x=0, y=0)
        # self.string("           GAME OVER\nPlay another game? 'Y' or 'N'")
        # self.write(self.string, font=FONT, align=ALIGNMENT)

        pass
        
    