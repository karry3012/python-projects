import pygame
import random
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
screen_width=700
screen_height=600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("game")
pygame.display.update()

exit_game= False
game_over =False
s_x=45
s_y=55
s_size=30
fps=80
clock = pygame.time.Clock() #
velocity_x = 0
velocity_y = 0
f_x=random.randint(20,screen_width/2)
f_y=random.randint(20,screen_height/2)
score =0
while not exit_game:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x +=5
                velocity_y=0
                
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x =-5
                velocity_y=0
                
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity_y =-5
                velocity_x=0
                
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                velocity_y =+5
                velocity_x=0
    s_x = s_x +velocity_x  #
    s_y = s_y+ velocity_y  #
    if abs(s_x - f_x)<10 and abs(s_y-f_y)<10:
        score +=10
        print("Score:",score)
        f_x=random.randint(20,screen_width/2)
        f_y=random.randint(20,screen_height/2)
    screen.fill(white)
    pygame.draw.rect(screen,red,[f_x,f_y,s_size,s_size])
    pygame.draw.rect(screen,black,[s_x,s_y,s_size,s_size])
    pygame.display.update()
    clock.tick(fps)   
    
    
        

pygame.quit()
quit()