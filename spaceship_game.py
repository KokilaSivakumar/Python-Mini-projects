import pygame
import random
pygame.init()

path="work/" 
  #    "python\spaceship_game\work/"
spaceship =  pygame.image.load(path+"spaceship2.png")
alien     =  pygame.image.load(path+"aliean2.png")
bullet    =  pygame.image.load(path+"bullet2.png")

a_x,a_y =400,20
b_x,b_y =800,600
ss_x,ss_y=350,450

b_x_size,b_y_size=20,20
a_x_size,a_y_size=40,40

a_speed  =   7
ss_speed =   10
b_speed  =   15

outt=0

a_flag=0  ## for alien movement
b_out= 0  #### for bullet

fps=(50)
fpsClock = pygame.time.Clock()

win=pygame.display.set_caption(("Spaceship_Game"))
win=pygame.display.set_mode((800,600))

win.fill((0,0,0))

font_20=pygame.font.SysFont("comicsans",30,10)
score=font_20.render("SCORE: 0",1,(200,0,0))


def turn():
    global ss_x

    #speedd=20
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT] and ss_x>100:
        ss_x-=ss_speed
        #x-=vel

    if key[pygame.K_RIGHT] and ss_x<700:
        ss_x+=ss_speed
        #x+=vel

def alien_move():
      global a_x,a_y, a_flag
      a_y=20
      if a_x>700:
            a_flag=1
      elif a_x<100:
        a_flag=0

      if a_flag==0:
        a_x = a_x + a_speed 
      else:
        a_x = a_x - a_speed 

def bullet_move():
    global b_x,b_y, b_out
    key=pygame.key.get_pressed()
    if key[pygame.K_SPACE] and b_out==0:
        b_x  =  ss_x+15
        b_y  =  ss_y
        b_out=1
    if b_out:
        b_y-=b_speed
        if b_y<-30:
              b_out=0
        #x-=vel

def out():
       global outt, score, b_y
       if (b_x+b_x_size>a_x and (b_y+b_y_size>a_y or b_y<a_y+a_y_size)) and (b_y+b_y_size>a_y and (b_x+b_x_size>a_x or b_x<a_x+a_x_size)) and ((b_x<a_x+a_x_size)and(b_y+b_y_size>a_y or b_y<a_y+a_y_size)) and(b_y<a_y+a_y_size and(b_x+b_x_size>a_x or b_x<a_x+a_x_size)):
          print("out") 
          outt+=1
          b_y=-30
          score=font_20.render("SCORE: "+str(outt),1,(200,0,0))
          pass 

def display():
      win.fill((0,0,0))
      win.blit(spaceship,(ss_x,ss_y))
      win.blit(alien,(a_x,a_y))
      win.blit(bullet,(b_x,b_y))
      win.blit(score,(100,550))
      pygame.display.update()

while (True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            ff=False

    alien_move()
    display()
    turn()
    bullet_move()
    out()
    fpsClock.tick(fps)
    #print(fpsClock)
