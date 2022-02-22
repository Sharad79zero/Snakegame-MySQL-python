import pygame
import random
import os
pygame.mixer.init()
pygame.init()

## defining Colors into rgb colour codes. format = (0-255,0-255,-255)  ##
white = (255, 255, 255)         # in use
red = (255, 0, 0)               # in use
black = (0, 0, 0)               # in use
Blue = (0,0,255)                # in use
snakecolor=(171, 228, 10)       # in use
Orange=(255, 213, 128)          # in use
green = (0,100,0)               # in use
Darkorange=(255,140,0)          # in use
Darkgreen=(0,128,0)             # in use

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

### retrieving top 3 high score from SQL ###

import mysql.connector as sqltor
mycon = sqltor.connect(host="localhost",user="root",passwd="123456",database="snakegamescores")

top3scorer = mycon.cursor()
top3scorer.execute("SELECT * FROM scores ORDER BY score DESC")
displaytop3scorer = top3scorer.fetchall()
a=str(displaytop3scorer[0])
b=str(displaytop3scorer[1])
c=str(displaytop3scorer[2])
d='  Player      Highscore'

##############################################

# Game Title
pygame.display.set_caption(" Snakegame_with_Sharad_Kartik_Sourabh :  ver_3.21 (OSHMKUFA) added MORE random Funny/cute snake image each Retry ;) ")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    TIPS=['"Nagin Song Is Imp Part of Marriage"','"~~~ Nagin Dance ~~~"','"Snakes Are Cute!"','"Snake Wanna Have Fun!"','"Snakes Are Dangerous!"','"Snakes Are AEWSOME!"','"Dont Forget To Feed Your Snakes!"','"Snakes Are Good Pets!"','"Snakes Likes To Be Your Belt!"','"Never Wound a Snake, Kill It"','"The Snake Will Always Bite Back"','"Sometimes Just Ssssmile!"','"Life is Snake&Ladder, Without Ladder"','"Snakes Are COOL Creatures!"']
    CHOOSENTIP= random.choice(TIPS)
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        text_screen("Welcome To Snakes;Gate", black, 240, 40 )
        text_screen("Tip of the Day! :", green, 30, 120 )
        text_screen(CHOOSENTIP, Blue, 135, 200 )
        text_screen("Press SPACEBAR To Play" ,Darkorange , 225 , 350 )
        text_screen("~~~~~~~~~~~~~~~" ,Darkgreen ,270 ,425 )
        text_screen("@" ,red , 640, 425 )
        text_screen("~~~~~~~~~~~~~~~" ,Darkgreen ,220 ,470 )
        text_screen("@" ,red ,140 , 470 )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('background.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables

    snakepics=["angrysnake.jpg","dabsnake.jpg","gentelsnake.jpg","hatsnake.jpg","heygurlsnake.jpg","twosnake.jpg","musclesnake.jpg","jazzsnake.jpg","snakegameu.jpg","hisnake.jpg","fistsnake.jpg","drumsnake.jpg","smartsnake.jpg","harrysnake.jpg","voilinsnake.jpg","praysnake.jpg","funsnake.jpg","Cutehatsnake.jpg","tiesnake.jpg"]
    # Choosing random background pics
    CHOOSEBACKGROUND=random.choice(snakepics)

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over!", red, 350,400)
            text_screen("Press ENTER to Continue!", green, 225, 460)
            text_screen(a, Blue, 150, 200 )
            text_screen(b, Blue, 150, 250 )
            text_screen(c, Blue, 150, 300 )
            text_screen(d, Darkorange, 150, 125 )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<30 and abs(snake_y - food_y)<30:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            #Background Image
            bgimg = pygame.image.load(CHOOSEBACKGROUND)
            bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
            
            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), Blue, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, snakecolor, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
        
    # CONNECTING the python game to mysql database through mysql-connector-python
    import mysql.connector as sqltor
    mycon = sqltor.connect(host="localhost",user="root",passwd="123456",database="snakegamescores")
    if mycon.is_connected():
        print("successful connected to python database")

    username=input("write a username:")
    cursor=mycon.cursor()
    query="INSERT INTO scores(name,score) VALUES('{}',{})".format(username,score)
    cursor.execute(query)
    mycon.commit()
    print("data insertion successfully")
    pygame.quit()
    quit()
welcome()
