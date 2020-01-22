import turtle # Importing turtle library
wn=turtle.Screen()  #Creating a window
wn.title("Pong By Sobhit")  #Giving a title
wn.bgcolor("black")   #giving background color
wn.setup(width=800,height=600)
wn.tracer(0)  #Helps to speed up our game

#score


score_a=0
score_b=0
#Paddle A
paddle_a = turtle.Turtle()  #Creating paddle object
paddle_a.speed(0)  #Setting speed of animation
paddle_a.shape("square") #Giving our paddle a shape
paddle_a.color("blue")  #Giving our paddle a color
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #Giving our paddle to a given height and width
paddle_a.penup()
paddle_a.goto(-350,0)  #Make the paddle place at given coordinate considering center as origin


#Paddle B
paddle_b = turtle.Turtle()  #Creating paddle object
paddle_b.speed(0)  #Setting speed of animation
paddle_b.shape("square") #Giving our paddle a shape
paddle_b.color("yellow")  #Giving our paddle a color
paddle_b.shapesize(stretch_wid=5,stretch_len=1) #Giving our paddle to a given height and width
paddle_b.penup()
paddle_b.goto(350,0)  #Make the paddle place at given coordinate considering center as origin


#Ball

ball = turtle.Turtle()  #Creating ball object
ball.speed(0)  #Setting speed of animation
ball.shape("circle") #Giving our ball a shape
ball.color("red")  #Giving our ball a color
ball.penup()
ball.goto(0,0)  #Make the ball place at given coordinate considering center as origin
ball.dx=0.1 #Giving the ball a velocity in x-direction
ball.dy=-0.1 #and a velocity in y-direction



#Pen -Display score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() #As we don't want to see the pen
pen.goto(0,260)
pen.write("Player A : 0    Player B :0",align = "center",font=("Courier" ,24,"normal"))



#FUNCTIONS
def paddle_a_up():
    y=paddle_a.ycor() #Returns y-coordinate
    y+=20 #increase y to move it upwards
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor() #Returns y-coordinate
    y-=20 #increase y to move it downwards
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor() #Returns y-coordinate
    y+=20 #increase y to move it upwards
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor() #Returns y-coordinate
    y-=20 #increase y to move it downwards
    paddle_b.sety(y)


#KEYBOARD BINDING
wn.listen()   #Instructs it to listen to keyboard input
wn.onkeypress(paddle_a_up,"w") #When user presses w call the function paddle_a_up
wn.onkeypress(paddle_a_down,"s") #When user presses s call the function paddle_a_down

wn.onkeypress(paddle_b_up,"Up") #When user presses w call the function paddle_a_up
wn.onkeypress(paddle_b_down,"Down") #When user presses s call the function paddle_a_down















#MAIN GAME LOOP

while True:
    wn.update() #Everytime the loop runs the game window updates

    #Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy*=-1   #Reverses the direction in up border

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*=-1  #Reverses the direction in bottom border

    if ball.xcor() >390:
        ball.goto(0,0) #Goes to the center
        ball.dx*=-1 #Reverses direction
        score_a+=1 #If player B  misses then player A takes a point
        pen.clear()
        pen.write("Player A : {}    Player B :{}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() <-390:
        ball.goto(0,0) #Goes to the center
        ball.dx*=-1 #Reverses direction
        score_b+=1 #If player A  misses B gets takes a point
        pen.clear() #To clear the scoreboard before writing new value
        pen.write("Player A : {}    Player B :{}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    #Paddle and ball collisions


    if ball.xcor() > 340 and ball.xcor()<350 and ball.ycor()<paddle_b.ycor() +40 and ball.ycor()>paddle_b.ycor() -40:
        ball.setx(340)
        ball.dx*=-1


    if ball.xcor() < -340 and ball.xcor()>-350 and ball.ycor()<paddle_a.ycor() +40 and ball.ycor()>paddle_a.ycor() -40:
        ball.setx(-340)
        ball.dx*=-1




