from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")




class Scoreboard(Turtle):

    def __init__(self, high_score):
        super().__init__()
        self.current_score = 0

        with open ("high_file.txt", mode="r+") as high_file:
            high_score_file = high_file.read()

        print("High Score print", high_score_file)

        if high_score_file == '':
            high_score_file = 0


        self.high_score = int(high_score_file)

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
        if self.current_score > (self.high_score):
            self.high_score = self.current_score
            # self.current_score = 0
            # self.increase_score()
            self.clear()
            self.string = "Lives:           Score: " + str(self.current_score) + \
                    "         High Score: " + str(self.high_score)
            self.write(self.string, font=FONT, align=ALIGNMENT)

            with open ("high_file.txt", mode="w") as high_file:
                high_file.write(str(self.current_score))



        
class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        
        self.color("red")
        self.hideturtle()
        self.penup()


        self.goto(x=0, y=0)
        self.string = "           GAME OVER\nPlay another game? 'Y' or 'N'"

        self.write(self.string, font=FONT, align=ALIGNMENT)