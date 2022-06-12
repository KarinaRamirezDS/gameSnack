import turtle
import time
import random

delay = 0.1
body_snake = []
score = 0
high_score = 0

wn = turtle.Turtle()
wn = turtle.Screen()
wn.title("Game snake")
wn.setup(width=600, height=600)
wn.bgcolor('pink')

#Head setting
head = turtle.Turtle()
#fijar
head.speed(0)
head.shape('square')
head.color('purple')
head.penup()
head.goto(0,0)
head.direction = "stop"


#############FOOD

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
food.direction = "stop"

#score
text = turtle.Turtle()
text.speed(0)
text.color('white')
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write(f'Score 0       High Score: 0', align="center", font=("arial", 24) )

def mov():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 10)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
    if head.direction == "right":
        y = head.xcor()
        head.setx(y + 10)
    if head.direction == "left":
        y = head.xcor()
        head.setx(y - 10)
        
        
def dirUp():
    head.direction = "up"

def dirDown():
    head.direction = "down"
    
def dirLeft():
    head.direction = "left"
    
def dirRigth():
    head.direction = "right"
    
wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirLeft, "Left")
wn.onkeypress(dirRigth, "Right")
        
while True:
    wn.update()
   # Colission with de window
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
       time.sleep(1)
       head.goto(0,0)
       head.direction = "stop"
       
       #Esconder segmentos
       for segment in body_snake:
           segment.goto(1000,1000)
           
       body_snake.clear()
       
       score = 0
       text.clear()
       text.write(f'Score {score}       High Score: {high_score}', align="center", font=("arial", 24) )
       
      
   
    #Colision  head with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)
        ## nuevo segmento
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        body_snake.append(new_segment)
        
        score += 10
        if score > high_score:
           high_score = score
           
        text.clear()
        text.write(f'Score {score}       High Score: {high_score}', align="center", font=("arial", 24) )
        print(new_segment)
    
    totalSeg = len(body_snake)
    
    for i in range(totalSeg - 1, 0, -1):
        x = body_snake[i-1].xcor()
        y = body_snake[i-1].ycor()
        body_snake[i].goto(x,y)
        
    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_snake[0].goto(x,y)
    
    mov()
    
     #colision con el body   
    for segment in body_snake:
         if segment.distance(head) < 10:
             time.sleep(1)
             head.goto(0,0)
             head.direction = "stop"
             
             for segment in body_snake:
              segment.goto(1000,1000)
             
             body_snake.clear()
         
             score = 0
             text.clear()
             text.write(f'Score {score}       High Score: {high_score}', align="center", font=("arial", 24) )
             
    
    time.sleep(delay)
    
    
    
turtle.done()




# puntero.speed(1)

# for i in range(0,3):
#     puntero.forward(100)
#     puntero.left(120)

