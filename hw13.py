import turtle
import random
import math
from turtle import Turtle

# Finishing touches:
# 1: Every time fuel depletes 10, the velocity increase from each thrust increases
# 2: A random amount of obstacles spawn at the beginning of each round (ranging from 8-20)
# 3: The colors of each object randomizes each call of game() (From list of pink, red, green, white)

class SpaceCraft(Turtle):
    '''
    Purpose: Create a spacecraft turtle object which is controlled by the user.

    Instance variables: self.xpos: The position on the x axis of the spacecraft
                        self.ypos: The position on the y axis of the spacecraft
                        self.xvelo: The velocity of the spacecraft on the x axis
                        self.yvelo: The velocity of the spacecraft on the y axis
                        self.fuel: The level of fuel the spacecraft has
                        self.status: The status of whether or not the spacecraft can be moved by the user

    Methods: move: Enables and characterizes the movement of the spacecraft
             thrust: Provides the user the ability to push the spacecraft forward
             left_turn: Allows the user to turn the spacecraft left
             right_turn: Allows the user to turn the spacecraft right
    '''

    def __init__(self, xpos, ypos, xvelo, yvelo):
        turtle.Turtle.__init__(self)
        self.xpos = xpos
        self.ypos = ypos

        self.xvelo = xvelo
        self.yvelo = yvelo

        self.fuel = 40
        self.status = True

        self.left(90)
        self.penup()
        self.speed = 0
        self.goto(xpos, ypos)
    
    def move(self):
        if self.status == True:
            self.yvelo -= 0.0486

            self.xpos = self.xcor() + self.xvelo
            self.ypos = self.ycor() + self.yvelo

            if self.xpos <= -10:
                self.xpos = 505
                # self.xvelo *= -0.8
                # self.yvelo *= 0.4
            
            if self.xpos >= 510:
                self.xpos = -5
                # self.xvelo *= -0.8
                # self.yvelo *= 0.4

            if self.ypos >= 499:
                self.ypos = 499
                self.yvelo *= -0.2


            self.goto(self.xpos, self.ypos)
    
    def thrust(self):
        if self.status == True:
            if self.fuel > 0 and self.fuel > 30:
                self.fuel -= 1
                angle = math.radians(self.heading())

                cos_angle = math.cos(angle)
                self.xvelo += cos_angle

                sin_angle = math.sin(angle)
                self.yvelo += sin_angle

                print(f'Fuel remaining:   {self.fuel} units')

            elif self.fuel <= 30:
                self.fuel -= 1
                angle = math.radians(self.heading())

                cos_angle = math.cos(angle)
                self.xvelo += cos_angle*2.0

                sin_angle = math.sin(angle)
                self.yvelo += sin_angle*2.0

                print(f'Fuel remaining:   {self.fuel} units')

            elif self.fuel <= 20:
                self.fuel -= 1
                angle = math.radians(self.heading())

                cos_angle = math.cos(angle)
                self.xvelo += cos_angle*4.0

                sin_angle = math.sin(angle)
                self.yvelo += sin_angle*4.0

                print(f'Fuel remaining:   {self.fuel} units')

            elif self.fuel <= 10:
                self.fuel -= 1
                angle = math.radians(self.heading())

                cos_angle = math.cos(angle)
                self.xvelo += cos_angle*6.0

                sin_angle = math.sin(angle)
                self.yvelo += sin_angle*6.0

                print(f'Fuel remaining:   {self.fuel} units')
            else:
                self.clear()
                self.write('No fuel!')


    def left_turn(self):
        if self.status == True:
            if self.fuel > 0:

                self.fuel -= 1
                self.left(15)
                print(f'Fuel remaining:   {self.fuel} units')
            else:
                self.clear()
                self.write('No fuel!')

    def right_turn(self):
        if self.status == True:
            if self.fuel > 0:

                self.fuel -= 1
                self.right(15)
                print(f'Fuel remaining:   {self.fuel} units')
            else:
                self.clear()
                self.write('No fuel!')


class Obstacles(SpaceCraft):
    '''
    Purpose: Creates an object to act as an obstacle during the spacecraft's travel.

    Instance variables: self.status: The status of whether the obstacles should be moving or not
                        self.xpos: The position on the x axis of the obstacle
                        self.ypos: The position on the y axis of the obstacle
                        self.xvelo: The velocity of the obstacle on the x axis
                        self.yvelo: The velocity of the obstacle on the y axis

    Methods: movement: Enables and characterizes the movement of the obstacle
             
    '''

    def __init__(self, xpos, ypos, xvelo, yvelo, color):
        turtle.Turtle.__init__(self)
        self.status = True
        self.penup()
        self.speed(0)
        self.setpos(xpos, ypos)

        self.shape('circle')
        self.shapesize(1)
        self.color(color)

        self.xpos = xpos
        self.ypos = ypos
        self.xvelo = xvelo
        self.yvelo = yvelo
        

    
    def movement(self):
        if self.status == True:
            self.yvelo -= 0.07

            self.xpos = self.xcor() + self.xvelo
            self.ypos = self.ycor() + self.yvelo

            if self.xpos <= 1:
                self.xpos = 1
                self.xvelo *= -1

            if self.xpos >= 499:
                self.xpos = 499
                self.xvelo *= -1

            if self.ypos <= 15:
                self.ypos = 20
                self.yvelo *= -1

            if self.ypos >= 499:
                self.ypos = 499
                self.yvelo *= -1

            self.goto(self.xpos, self.ypos)


class Game:
    '''
    Purpose: Creates an environment to play the rocket game

    Instance variables: self.player: A spacecraft object
                        self.initial_x_pos: A random initial position on the x axis
                        self.initial_y_pos: A random initial position on the y axis
                        self.initial_x_velo: A random initial velocity value on the x axis
                        self.initial_y_velo: A random initial velocity value on the y axis
                        self.obs: A list of obstacle objects existing within each game sequence.
                        self.collision:

    Methods: explosion: Animates an explosion upon impact with another object
             gameloop: Initiates the game sequence and activates each object
    '''

    def __init__(self):
        turtle.setworldcoordinates(0, 0, 500, 500)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        turtle.Screen().bgcolor('#6495ED')
        turtle.title('Rocket Game')
        turtle.delay(0)
        turtle.tracer(0, 0)    

        turtle.penup()
        turtle.pensize(0.5)
        turtle.color('yellow')
        turtle.goto(20, 480)
        
        for y in range(20):
            
            for x in range(10):
                turtle.right(30)
                turtle.pendown()
                turtle.forward(5)
                turtle.back(10)
                turtle.forward(5)
                turtle.left(90)
                turtle.forward(5)
                turtle.left(180)
                turtle.forward(10)
                turtle.left(180)
                turtle.forward(5)
                turtle.right(90)
                turtle.left(30)
                turtle.penup()
                turtle.forward(50)
            
            turtle.right(90)
            turtle.forward(30)
            turtle.right(90)
            turtle.forward(500)
            turtle.right(180)
        

        turtle.goto(-20,0)
        turtle.pendown()
        turtle.color('gray')
        turtle.pensize(60)
        turtle.forward(540)
        turtle.penup()
    
        turtle.goto(500,0)
        turtle.left(180)
        moon_dist_list = [10, 60, 80, 72, 40, 81]

        for dist in moon_dist_list:
            turtle.pencolor('#787276')
            turtle.pensize(60)
            turtle.forward(dist)
            turtle.pendown()
            turtle.forward(0.00001)
            turtle.penup()

        turtle.left(180)
        turtle.forward(530)
        turtle.right(180)

        for dist in moon_dist_list:
            turtle.pencolor('#9897A9')
            turtle.pensize(60)
            turtle.forward(dist+45)
            turtle.pendown()
            turtle.forward(0.00001)
            turtle.penup()

        turtle.left(180)
        turtle.forward(480)
        turtle.right(180)

        for dist in moon_dist_list:
            turtle.pencolor('#322D31')
            turtle.pensize(60)
            turtle.forward(dist+45)
            turtle.pendown()
            turtle.forward(0.00001)
            turtle.penup()

        

        turtle.left(90)

        

        self.collision = False

        self.initial_x_pos = random.uniform(100,400)
        self.initial_y_pos = random.uniform(250, 400)
        self.initial_x_velo = random.uniform(-4, 4)
        self.initial_y_velo = random.uniform(-2, 0)

        self.player = SpaceCraft(self.initial_x_pos, self.initial_y_pos, self.initial_x_velo, self.initial_y_velo)

        self.obs = []

        amt = random.randint(8,20)
        for i in range(amt):
            xpos = random.uniform(100,400)
            xvelo = random.uniform(-4, 4)
            yvelo = random.uniform(-0.4, 3)
            color_list = ['red', 'white', 'green', 'pink']

            self.obs.append(Obstacles(xpos, 495, xvelo, yvelo, color_list[random.randint(0,3)]))

        turtle.onkeypress(self.player.thrust, 'Up')
        turtle.onkeypress(self.player.left_turn, 'Left')
        turtle.onkeypress(self.player.right_turn, 'Right')
        self.gameloop()

        turtle.listen()
        turtle.mainloop()

    def explosion(self):
        self.player.color('#d35400')
        self.player.shape('circle')
        self.player.shapesize(2)
        
    def gameloop(self):
        status = True

        if status == True:
            
            if self.player.ypos > 24:
                self.player.move()

                if self.player.status == True:
                    turtle.ontimer(self.gameloop, 30)
                    turtle.update()

                else:
                    self.player.color('black')
                    self.player.write('You crashed!', False, 'center', font = (60))
                    self.explosion()
                    turtle.update()
                
                for ob in self.obs:
                    ob.movement()

                    if abs(self.player.xpos - ob.xpos) < 11 and abs(self.player.ypos - ob.ypos) < 11:
                        self.player.status = False
                        ob.shapesize(0.0001)
                        ob.color('#154360')

                        for ob in self.obs:
                            ob.status = False

                        self.collision = True

            if -3.00 < self.player.xvelo < 3.0 and -3.0 < self.player.yvelo < 3.0 and self.player.ypos <= 24:
                self.player.clear()
                self.player.write('Successful Landing!', False, 'center', font = (20))
                self.player.status = False

            elif self.collision == True or self.player.ypos <= 24:
                turtle.update()
                self.player.clear()
                self.player.color('black')
                self.player.write('You crashed!', False, 'center', font = (60))
                self.explosion()
                self.player.status = False


if __name__ == '__main__':
    Game()
