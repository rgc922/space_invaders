from turtle import Screen
from ship import Ship, ShipLives
from shot import Shot, ShotInvader
from invader import Invader
from scoreboard import Scoreboard, GameOver
from random import randint

import time
import datetime

screen = Screen()

screen.setup(width=800, height=660)

screen.bgcolor("black")
screen.title("Space Invaders RGC")
screen.tracer(0)


def invader_shot(position):
    global invader_shot_list
    
    if randint(0, 130) == 0:
        invader_shot_list.append(ShotInvader(position))


#### MY SHOTS WITH SPACE KEYBOARD
def new_shot():

    global shot_list
    global temp_date
    
        #### limit the shots per second
    
    elapsed = datetime.datetime.now() - temp_date

    if elapsed > datetime.timedelta(seconds=1):

        new_shot = Shot((ship.xcor(), ship.ycor()))
        shot_list.append(new_shot)

        temp_date = datetime.datetime.now()




high_score = 0








def space_game():

    global invader_shot_list
    global shot_list
    global lives
    global temp_date
    global ship
    global score
    global game_over

    lives = 3


    ### My ship
    image = "Space_Invaders_ship.gif"


    ### My ship 
    ship = Ship((0, -250))
    screen.addshape(image)
    ship.shape(image)


    #### Lives SHIPS
    lives_ship_1 = ShipLives((-200, 300))
    lives_ship_1.shape(image)

    lives_ship_2 = ShipLives((-140, 300))
    lives_ship_2.shape(image)


    #### my shots list
    shot_list = []
    
    temp_date = datetime.datetime.now()

        


    ##### INVADERS SHOTS
    invader_shot_list = []

    #### invaders

    invader_gif_1 = "giphy_1.gif"
    invader_gif_2 = "giphy_2.gif"

    screen.addshape(invader_gif_1)
    screen.addshape(invader_gif_2)

    invaders_list = [(Invader((-340 + itemx * 70, 240 - itemy * 50))) for itemx in range(8) for itemy in range(4)]

    try:
            
        game_over.clear()
        game_over.hideturtle()
        
        score.clear()
        score.hideturtle()
    
    except:
        pass


    score = Scoreboard(high_score)


    screen.onkey(ship.go_left, "Left")
    screen.onkey(ship.go_right, "Right")
    screen.onkey(new_shot, "space")
    screen.onkey(None, "y")
    screen.onkey(None, "Y")
    screen.onkey(None, "n")
    screen.onkey(None, "N")

    screen.listen()

    game_is_on = True

    anima = True
    move_right = 0


    while game_is_on:

        #### ANIMACION
        if anima == True:
            anima = False
            invader_gif = (invader_gif_1)
            
        else:
            anima = True
            invader_gif = (invader_gif_2)
        



        

        #### invaders to left or right
        if move_right < 18:
            move_right += 1
            right = False
        else:
            move_right = 0
            right = True
        
        
        for invader in invaders_list:
            invader.shape(invader_gif)
            invader.move_side()
            if right:
                invader.move_side_back()

            #### invaders shot back
            # print(invader.xcor(), invader.ycor())
            invader_shot((invader.xcor(), invader.ycor()))


            #### move invaders shots
        for shot_back in invader_shot_list:
            shot_back.move_shot_invader()
            #### delete shot if it's to low
            if shot_back.ycor() < -400:
                
                invader_shot_list.remove(shot_back)
                shot_back.hideturtle()
                shot_back.clear()
                # print(item)

            #### check if a shot back hit my ship
            if shot_back.distance(ship) < 25:
                # print("HIT")
                lives -= 1
                # score.increase_high_score()
                # score.current_score = 0

                ship.goto((0, -250))

                # for 
                # shot_list = []
                # invader_shot_list = []

                for shot in shot_list:
                    shot.clear()
                    shot.hideturtle()
                shot_list = []

                for shot in invader_shot_list:
                    shot.clear()
                    shot.hideturtle()
                invader_shot_list = []

                if lives == 2:
                    lives_ship_2.clear()
                    lives_ship_2.hideturtle()
                elif lives == 1:
                    lives_ship_1.clear()
                    lives_ship_1.hideturtle()
                elif lives == 0:
                    game_is_on = False
                    # score.game_over()
                    game_over = GameOver()
                    screen.onkey(space_game, "y")
                    screen.onkey(space_game, "Y")
                    screen.onkey(screen.bye, "n")
                    screen.onkey(screen.bye, "N")

                    score.increase_high_score()

                    for item in invaders_list:
                        item.clear()
                        item.hideturtle()
                    invaders_list = []
                    
                    ship.clear()
                    ship.hideturtle()

                    # score.clear()
                    # score.hideturtle()
                    # 


        ##### my shots
        for item in shot_list:
            # if item != None:
            item.move_shot()
            
            #### delete shot if it's to high
            if item.ycor() > 800:
                
                shot_list.remove(item)
                item.hideturtle()
                item.clear()
                # print(item)

            #### check if a shot hits an invader.
            for invader in invaders_list:
                if invader.distance(item) < 15:
                    shot_list.remove(item)
                    item.hideturtle()
                    item.clear()

                    invaders_list.remove(invader)
                    invader.hideturtle()
                    invader.clear()

                    score.increase_score()
        
        screen.update()
        time.sleep(0.2)


space_game()

#### 
screen.mainloop()