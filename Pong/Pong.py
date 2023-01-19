import pygame
from pygame import mixer
from random import *
import time
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60 #fps of game
screen_x = 700 #dimensions screen
screen_y = 500
size = (screen_x, screen_y)
vel_players = 5 #vel_playersocity of players
Plyer1_y = 250 #first position of rectangle
Player2_y = 250
width = 10 #dimensions of paddle
height = 70 #dimension of paddle
score_pl1 = 0 #score players
score_pl2 =0

vel_ball = 4 #velocity of ball
ball_x = 350 #initial position of ball
ball_y = 250 #initaial position of ball
ball_scale_x = 32 #dimensions of ball
ball_scale_y = ball_scale_x - 3
#set run for game
running = True
#set up screen

#set up mixer for music 
mixer.init()
pop = pygame.mixer.Sound("pop.wav")
sad = pygame.mixer.Sound("sad.wav")


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

class Ball(pygame.sprite.Sprite):

    def __init__(self, pos):
        
        super(Ball, self).__init__()

        self.image = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.image, (ball_scale_x, ball_scale_y))

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.velocity = [vel_ball, vel_ball]
        self.score_pl1 = score_pl1 
        self.score_pl2 = score_pl2 

    def update(self):
        #left side
        if self.rect.left < 0:
            #print("left")
            self.score_pl2 +=1
            pygame.mixer.Sound.play(sad)
            ball_center_left()
            redirecting() #redirecting ball to center 

        #right side
        if self.rect.right >= screen_x:
            #print("right")
            self.score_pl1 +=1
            pygame.mixer.Sound.play(sad)
            ball_center_right()
            redirecting()
            #self.rect.x = 350 #redirecting ball to center after score
            #self.rect.y = 250    

        if self.rect.top < 0 or self.rect.bottom >= screen_y:
            self.velocity[1] *= -1

        self.rect.move_ip(self.velocity)
        
#create ball
ball = Ball((ball_x, ball_y))
group = pygame.sprite.RenderPlain()
group.add(ball)

#init pygame
pygame.font.init()

#set variable for when keys are pressed and for clock
clock = pygame.time.Clock()

#font
main_font = pygame.font.SysFont("helvetica", 30)

def ball_center_right():
    FPS = 1
    screen.blit(Player1_score_text, (8, 0))
    screen.blit(Player2_score_text, (screen_x-text2_width-8, 0))

    pygame.draw.line(screen, RED, [(screen_x-3), 0], [(screen_x-3), screen_y], 5)
    pygame.draw.line(screen, WHITE, [(screen_x//2)-1, 0], [(screen_x//2)-1, screen_y], 5)

    paddleA = pygame.draw.rect(screen, WHITE, [10, Plyer1_y, width, height], 0, 6)
    paddleB = pygame.draw.rect(screen, WHITE, [screen_x - 20, Player2_y, width, height], 0, 6)

    pygame.display.flip()
    clock.tick(FPS)


def ball_center_left():
    FPS = 1
    screen.blit(Player1_score_text, (8, 0))
    screen.blit(Player2_score_text, (screen_x-text2_width-8, 0))

    pygame.draw.line(screen, RED, [(3), 0], [(3), screen_y], 5)
    pygame.draw.line(screen, WHITE, [(screen_x//2)-1, 0], [(screen_x//2)-1, screen_y], 5)

    paddleA = pygame.draw.rect(screen, WHITE, [10, Plyer1_y, width, height], 0, 6)
    paddleB = pygame.draw.rect(screen, WHITE, [screen_x - 20, Player2_y, width, height], 0, 6)

    pygame.display.flip()
    clock.tick(FPS)

def redraw():
    screen.blit(Player1_score_text, (8, 0))
    screen.blit(Player2_score_text, (screen_x-text2_width-8, 0))
    paddleA = pygame.draw.rect(screen, WHITE, [10, Plyer1_y, width, height], 0, 6)
    paddleB = pygame.draw.rect(screen, WHITE, [screen_x - 20, Player2_y, width, height], 0, 6)

def redirecting():
    global a
    a = ball.rect
    a.x = 333 #redirecting ball to center after score
    a.y = 250 #redirecting ball to center after score
    ball.velocity = [0, 0]

#move ball
def Move():
    global ball_y, ball_x
    ball_x += vel_ball
    ball_y += vel_ball
    
#pause the game
def Pause():
    GREY = ((211, 211, 211))
    paused_text = main_font.render("PAUSE", True, (BLACK))
    press_space = main_font.render("Press c to continue", True, (BLACK))
    screen.fill(GREY)
    paused_text_width = paused_text.get_width()
    press_space_width = press_space.get_width()

    screen.blit(paused_text, (screen_x/2-paused_text_width/2, screen_y/2-30))
    screen.blit(press_space, (screen_x//2-press_space_width//2, screen_y/2 +30))

    while pause:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                 #Unpause()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    Unpause()     
        pygame.display.update()

def Unpause():
    global pause
    pause = False

#while loop for playing
while running == True:
    global pause

    #first fill screen 
    screen.fill(BLACK)

    group.update()
    group.draw(screen)

    #draw players and middle line
    pygame.draw.line(screen, WHITE, [(screen_x//2)-1, 0], [(screen_x//2)-1, screen_y], 5)

    #draw paddles for game
    paddleA = pygame.draw.rect(screen, WHITE, [10, Plyer1_y, width, height], 0, 6)
    paddleB = pygame.draw.rect(screen, WHITE, [screen_x - 20, Player2_y, width, height], 0, 6)

    #varibale for keys
    keys = pygame.key.get_pressed() 
    
    #score text of two players
    Player1_score_text = main_font.render(f'Score:{ball.score_pl1}', True, (WHITE))
    Player2_score_text = main_font.render(f'Score:{ball.score_pl2}', True, (WHITE))

    #text to play again
    play_again = main_font.render("Press P to play again", True, (WHITE))

    #get width of text 2 so we can substract it form the position
    text2_width = Player2_score_text.get_width()

    #show scores
    screen.blit(Player1_score_text, (8, 0))
    screen.blit(Player2_score_text, (screen_x-text2_width-8, 0))

    #eevnt for quitting  
    for event in pygame.event.get():

        if event.type  == pygame.QUIT:
            running = False 

    #input keys for movements
    if keys[pygame.K_w] and Plyer1_y > 10:
        Plyer1_y -= vel_players
    if keys[pygame.K_s] and Plyer1_y < 490-height:
        Plyer1_y += vel_players

    if keys[pygame.K_UP] and Player2_y > 10:
        Player2_y -= vel_players
    if keys[pygame.K_DOWN]and Player2_y < 490-height:
        Player2_y += vel_players

    if keys[pygame.K_SPACE]:
        pause = True
        Pause()

    if ball.rect.x== 333 and ball.rect.y == 250:
        screen.fill(BLACK)
        group.draw(screen)

        redraw()
        screen.blit(play_again, (screen_x//2-play_again.get_width()//2, 200))
        if keys[pygame.K_p]:
            ball.velocity = [vel_ball, vel_ball]

    #touching paddles
    obj = ball.rect
    velocity = ball.velocity

    if obj.colliderect(paddleA):
        pygame.mixer.Sound.play(pop)
        velocity[0] *= -1

    if obj.colliderect(paddleB):
        pygame.mixer.Sound.play(pop)
        velocity[0] *= -1

    #flip screen
    pygame.display.flip()

    #clock has to tick
    clock.tick(FPS)