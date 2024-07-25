from turtle import Turtle, Screen
import random

#Setting up the screen
screen = Screen()
screen.setup(500, 400)


#Asking user for the input
user_bet = screen.textinput("Turtle Color", "Place your bet on any turtle: ")

#Initializaing variables
turtle_colors = ["red", "blue", "green", "black", "orange", "purple"]
winning_turtle = ""
game_stop = False
X_POS = -230
Y_POS = 110
turtles = []

for i in range(6):                              #For loop to generate 6 turtles
    turtle = Turtle()                           #We will create a turtle
    turtle.penup()                              #It should not leave any trace lines
    turtle.color(turtle_colors[i])              #Choose the color according to its index from turtle_colors
    turtle.shape("turtle")                      #Shape will be set to turtle
    turtle.goto(X_POS, Y_POS)                   #It will go to these initial coordinates
    Y_POS -= 40                                 #Decrement y co-ordinate so the next turtle would go to a lower position
    turtles.append(turtle)                      #Add the turtle in the turtles list

if user_bet:                                    #If user has entered their bet
    game_stop = False                           #Set the game_stop flag to False

while not game_stop:                            #While the game is running
    for turtle in turtles:
        steps = random.randint(0, 10)
        turtle.forward(steps)                   #Each turtle will move forward random paces
        if turtle.xcor() > 230:                 #Whichever turtle reaches the wall first
            winning_turtle = turtle.pencolor()  #Store its color in the winning_turtle variable
            game_stop = True                    #Set the game_stop variable to True
            break                               #Break out of the loop

if user_bet == winning_turtle:                  #If user's bet equals the winning turtle's color
    print(f"You guessed it right. The winning turtle is {winning_turtle}")
else:
    print(f"Oops, you lost. The winning turtle is {winning_turtle}")

screen.exitonclick()
