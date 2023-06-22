import turtle, time, winsound, vlc, random

bgmusic = vlc.MediaPlayer("/Task Performance (MingMong)/bgmusic.wav")
deadsound = "C:\\Users\\Maybuena\\OneDrive - STI College Munoz\\Desktop\\My Files\\4th Year 1st Sem\\Computer Graphics\\Task Performance (MingMong)\\deadsound.wav"
boink = "C:\\Users\\Maybuena\\OneDrive - STI College Munoz\\Desktop\\My Files\\4th Year 1st Sem\\Computer Graphics\\Task Performance (MingMong)\\boink.wav"
winner_sound = "C:\\Users\\Maybuena\\OneDrive - STI College Munoz\\Desktop\\My Files\\4th Year 1st Sem\\Computer Graphics\\Task Performance (MingMong)\\winner.wav"

# Game Variable
colorList = ['#053996', '#DB1851', '#DFFF00', '#F54E11', '#02FAE5', '#00FF7B', 'white', 'black', 'violet']
wait = False
pen = turtle.Turtle()
pen.hideturtle()
pen2 = turtle.Turtle()
pen2.color('white')
pen2.hideturtle()
FPS = 0.01
left_score = 0
right_score = 0
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.color('white')
score.goto(0,250)
score.write(f'Left: {left_score} | Right: {right_score}', font=('Courier', 24, 'bold'), align='Center')

# For Screen
mainScreen = turtle.Screen()
mainScreen.title('MingMong By BT701')
mainScreen.tracer(0)
mainScreen.cv._rootwindow.resizable(False, False)

# For Ball
mainBall = turtle.Turtle()
mainBall.shape('circle')
mainBall.color('white')
mainBall.penup()
mainBall.speed(0)
mainBall.goto(0,0)
mainBall.dx = 2
mainBall.dy = 2

# For paddles
leftPaddle = turtle.Turtle()
leftPaddle.shape('square')
leftPaddle.shapesize(stretch_len=1, stretch_wid=5)
leftPaddle.color('blue')
leftPaddle.penup()
leftPaddle.speed(0)
leftPaddle.goto(-350,0)

rightPaddle = turtle.Turtle()
rightPaddle.shape('square')
rightPaddle.shapesize(stretch_len=1, stretch_wid=5)
rightPaddle.color('red')
rightPaddle.penup()
rightPaddle.speed(0)
rightPaddle.goto(345,0)

leftPaddle.hideturtle()
rightPaddle.hideturtle()
mainBall.hideturtle()

def waiting():
    global wait
    try:
        if wait is True:
            wait = False
            print('Game is Resumed')
            pen2.clear()
        else:
            wait = True
            print('Game is Paused')
            pen2.penup()
            pen2.clear()
            pen2.goto(0, 40)
            pen2.write('( Game Paused )', font=('Arial', 15, 'normal'), align='center')
    except Exception as e:
        print(str(e))
        
def rect(t, l, b):
    t.pendown()
    for i in range(2):
        t.forward(l)
        t.right(90)
        t.forward(b)
        t.right(90)
        
def winner(message):
    global wait, left_score, right_score
    left_score = 0
    right_score = 0
    leftPaddle.hideturtle()
    rightPaddle.hideturtle()
    mainBall.hideturtle()
    bgmusic.stop()
    winsound.PlaySound(winner_sound, winsound.SND_ASYNC | winsound.SND_ALIAS)
    pen.clear()
    pen2.clear()
    pen2.penup()
    score.goto(0,0)
    score.write(message, font=('Courier', 40, 'bold'), align='Center')
    mainScreen.update()
    pen2.clear()
    time.sleep(7)
    score.clear()
    welcome_screen()
    mainScreen.onclick(menu_select)
    mainScreen.mainloop()

# Function for moving the paddles
def leftPaddle_up():
    if wait is False:
        if leftPaddle.ycor() + 55 < 300:
            leftPaddle.sety(leftPaddle.ycor() + 30)
def leftPaddle_down():
    if wait is False:
        if leftPaddle.ycor() - 55 > -300:
            leftPaddle.sety(leftPaddle.ycor() - 30)
    
def rightPaddle_up():
    if wait is False:
        if rightPaddle.ycor() + 55 < 300:
            rightPaddle.sety(rightPaddle.ycor() + 30)
def rightPaddle_down():
    if wait is False:
        if rightPaddle.ycor() - 55 > -300:
            rightPaddle.sety(rightPaddle.ycor() - 30)
    
# Events for paddles
mainScreen.listen()
mainScreen.onkeypress(leftPaddle_up, "w")
mainScreen.onkeypress(leftPaddle_down, "s")
mainScreen.onkeypress(rightPaddle_up, "Up")
mainScreen.onkeypress(rightPaddle_down, "Down")
mainScreen.onkey(waiting, 'space')

loop = True
    
def start_game():
    bgmusic.play()
    global wait, loop, left_score, right_score, FPS
    mainScreen.setup(width=800, height=600)
    mainScreen.bgcolor('green')
    leftPaddle.showturtle()
    rightPaddle.showturtle()
    mainBall.showturtle()
    score.goto(0,250)
    score.write(f'Left: {left_score} | Right: {right_score}', font=('Courier', 24, 'bold'), align='Center')
    leftPaddle.goto(-350,0)
    rightPaddle.goto(345,0)
    while loop:
        
        if wait is False:
            if left_score == 10:
                winner('Player 1 Wins!')
            elif right_score == 10:
                winner('Player 2 Wins!')
            else:
                
                # For Moving the ball
                mainBall.setx(mainBall.xcor() + mainBall.dx)
                mainBall.sety(mainBall.ycor() + mainBall.dy)
                
                # For screen collision
                if mainBall.ycor() > 290:
                    mainBall.dy *= -1
                    mainBall.color(random.choice(colorList))
                    winsound.PlaySound(boink, winsound.SND_ASYNC | winsound.SND_ALIAS)
                elif mainBall.ycor() < -285:
                    mainBall.dy *= -1
                    mainBall.color(random.choice(colorList))
                    winsound.PlaySound(boink, winsound.SND_ASYNC | winsound.SND_ALIAS)
                    
                if mainBall.xcor() > 365:
                    left_score += 1
                    score.clear()
                    score.write(f'Left: {left_score} | Right: {right_score}', font=('Courier', 24, 'bold'), align='Center')
                    mainBall.dx *= -1
                    FPS = 0.01
                    winsound.PlaySound(deadsound, winsound.SND_ASYNC | winsound.SND_ALIAS)
                    mainBall.goto(0,0)
                elif mainBall.xcor() < -365:
                    right_score += 1
                    score.clear()
                    score.write(f'Left: {left_score} | Right: {right_score}', font=('Courier', 24, 'bold'), align='Center')
                    mainBall.dx *= -1
                    FPS = 0.01
                    winsound.PlaySound(deadsound, winsound.SND_ASYNC | winsound.SND_ALIAS)
                    mainBall.goto(0,0)
                
                # For paddle collision
                if mainBall.xcor() < leftPaddle.xcor() + 20 and mainBall.ycor() < leftPaddle.ycor() + 70 and mainBall.ycor() > leftPaddle.ycor() - 70:
                    if FPS == 0.0002000000000000005 or FPS == 0:
                        FPS = 0
                    else:
                        FPS -= 0.0002
                    mainBall.color(random.choice(colorList))
                    mainBall.dx *= -1
                    winsound.PlaySound(boink, winsound.SND_ASYNC | winsound.SND_ALIAS)
                elif mainBall.xcor() > rightPaddle.xcor() - 20 and mainBall.ycor() < rightPaddle.ycor() + 70 and mainBall.ycor() > rightPaddle.ycor() - 70:
                    if FPS == 0.0002000000000000005 or FPS == 0:
                        FPS = 0
                    else:
                        FPS -= 0.0002
                    mainBall.color(random.choice(colorList))
                    mainBall.dx *= -1
                    winsound.PlaySound(boink, winsound.SND_ASYNC | winsound.SND_ALIAS)
                # For updating the game
        mainScreen.update()
        time.sleep(FPS)

def welcome_screen():
    bgmusic.play()
    mainScreen.setup(500, 400)
    mainScreen.bgcolor('#000011')
    pen.color('white')
    pen.penup()
    pen.goto(0, 50)
    pen.write('MINGMONG', font=('Jokerman', 45, 'normal'), align='center')
    pen.pensize(2)
    pen.goto(-150, 20)
    pen.seth(0)
    rect(pen, 300, 50)
    pen.penup()
    pen.goto(-150, -60)
    pen.seth(0)
    pen.pendown()
    rect(pen, 300, 50)
    pen.penup()
    pen.goto(0, -20)
    pen.write('Start', font=('comic sans ms', 20, 'normal'), align='center')
    pen.goto(0, -100)
    pen.write('Exit', font=('comic sans ms', 20, 'normal'), align='center')
    mainScreen.update()
    
def menu_select(x, y):
    global mode, delay_time
    bgmusic.stop()
    if y >= -30 and y <= 20:
        if x >= -150 and x <= 150:
            mode = 1
            pen.clear()
            start_game()
    elif y >= -110 and y <= -60:
        if x >= -150 and x <= 150:
            mode = 2
            delay_time = 0.007
            pen.clear()
            mainScreen.bye()

welcome_screen()
mainScreen.onclick(menu_select)
mainScreen.mainloop()


