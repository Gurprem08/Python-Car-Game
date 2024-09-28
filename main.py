import pygame 
import os
import random
import time
pygame.init()


display_width = 700
display_height = 700

win= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("CAR GAME")
clock =pygame.time.Clock()

gray = (128,128,128)
white = (255,255,255)

images =[
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\car1.jpg'),#0
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\car.jpg'),#1
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\car2.jpg'),#2
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\car4.jpg'),#3
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\car5.jpg'),#4
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\car6.jpg'),#5
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\car7.jpg'),#6
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\background.jpg'),#7
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\background2.jpg'),#8
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\yellow strip.jpg'),#9
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\strip.jpg'),#10
         pygame.image.load('D:\coding\python-flask\Python projects\car game py\images\\download12.jpg'),#11
         ]
audio = [
         pygame.mixer.Sound('D:\coding\python-flask\Python projects\car game py\images\\awesomeness.wav'),
         pygame.mixer.Sound('D:\coding\python-flask\Python projects\car game py\images\\racecar2.wav'),
         pygame.mixer.Sound('D:\coding\python-flask\Python projects\car game py\images\\startcar.wav'),
         pygame.mixer.Sound('D:\coding\python-flask\Python projects\car game py\images\\car_crash.wav'),
         pygame.mixer.Sound('D:\coding\python-flask\Python projects\car game py\images\\point.wav'),
]

def background(y1):
    win.blit(images[11],(0,y1+0))
    win.blit(images[11],(display_width-images[11].get_width(),y1+0))
    win.blit(images[10],((display_width-images[11].get_width())-20,y1+0))
    win.blit(images[10],(images[11].get_width()+16,y1+0))
    win.blit(images[9],(330,y1+0))
    win.blit(images[9],(330,y1+200))
    win.blit(images[9],(330,y1+400))
    win.blit(images[9],(330,y1+600))
def background1(y_change):
    win.blit(images[11],(0,y_change+0))
    win.blit(images[11],(display_width-images[11].get_width(),y_change+0))
    win.blit(images[10],((display_width-images[11].get_width())-20,y_change+0))
    win.blit(images[10],(images[11].get_width()+16,y_change+0))
    win.blit(images[9],(330,y_change+0))
    win.blit(images[9],(330,y_change+200))
    win.blit(images[9],(330,y_change+400))
    win.blit(images[9],(330,y_change+600))
    
def score(a,b):
    font = pygame.font.SysFont("Times new Roman",40) 
    text = font.render("Score is :{}".format(b),True,(0,0,0))
    font1 = pygame.font.SysFont("Times new Roman",40) 
    text1 = font1.render("Dodged cars :{}".format(a),True,(0,0,0))
    win.blit(text,(0,0))    
    win.blit(text1,(0,40))          
    

def obstacle(obs , obs_startx,obs_starty):
    if obs ==1:
        win.blit(images[1],(obs_startx,obs_starty))
    
    if obs ==2:
        win.blit(images[2],(obs_startx,obs_starty))
    
    if obs ==3:
        win.blit(images[3],(obs_startx,obs_starty))
    
    if obs ==4:
        win.blit(images[4],(obs_startx,obs_starty))
    
    if obs ==5:
        win.blit(images[5],(obs_startx,obs_starty))
    
    if obs ==6:
        win.blit(images[6],(obs_startx,obs_starty))
    
     
def car(x,y):
    win.blit(images[0],(x,y))
    

    

def start() :
  while True:
    win.blit(images[8],(0,0))
    image_b = pygame.transform.rotate(images[11],90)
    win.blit(image_b ,(0,display_height-image_b.get_height()))
    font = pygame.font.SysFont("Times new Roman",50)
    text = font.render("Welcome" , True ,(255,0,0))
    font1 = pygame.font.SysFont("Times new Roman",50)
    text1 = font1.render("PRESS SPACE TO START" , True ,(0,0,0))
    
    win.blit(text , (250,50)) 
    win.blit(text1 , (70,525)) 
    
    pygame.display.update()
    
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                pygame.quit()
        if event.type == pygame.KEYDOWN :
                pygame.quit()
    
                if event.key ==pygame.K_SPACE:
                
                    audio[2].play()
                    time.sleep(1.5)

                    game_loop()
                
    
def game_over(b,):
  while True:
    
    win.blit(images[7],(0,0))
    image_b = pygame.transform.rotate(images[11],90)
    win.blit(image_b ,(0,display_height-image_b.get_height()))
    font1 = pygame.font.SysFont("Times new Roman",50)
    text1 = font1.render("Game over" , True ,(255,0,0))
    font2 = pygame.font.SysFont("Times new Roman",50)
    text2 = font1.render("PRESS C TO RESTART " , True ,(white))
    win.blit(text1,(250,50))
    win.blit(text2,(120,550))
    font = pygame.font.SysFont("Times new Roman",40) 
    text = font.render("Score is : {} ".format(b),True,(0,0,0))
    win.blit(text,(250,150))  
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type ==pygame.KEYDOWN and event.key == pygame.K_c:
            audio[0].play()
            start()
        if event.type==pygame.QUIT:
                pygame.quit()


def game_loop ():
       
    bumped =False
    x_change = 0
    x = display_width*0.46
    y = display_height*0.8
    obstacle_speed = 5
    
    y_change = -(display_height -100)
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=0
    obs=1
    b=1
    q=60 
    a=0
    y1=0

    while True:
       
        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
                pygame.quit()
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change =-5

                if event.key == pygame.K_RIGHT: 
                    x_change=5   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x+=x_change 
        win.fill(gray)           
        background(y1)
        background1(y_change)
        score(a,b)
        obstacle(obs,obs_startx,obs_starty)
        y1+=obstacle_speed+10
        y_change+=obstacle_speed+10
        obs_starty+=obstacle_speed
        if obs_starty >= (y-images[0].get_height()+12) and x<=obs_startx<=(x+images[0].get_width()):
            pygame.mixer.Sound.play(audio[3])
            time.sleep(1.1)
            game_over(b) 
            
            
        if obs_starty >= (y-images[0].get_height()+12) and x<=(obs_startx+images[4].get_width())<=(x+images[0].get_width()):
            pygame.mixer.Sound.play(audio[3])
            time.sleep(1.1)
            game_over(b)
        
        if obs_starty>display_height:
            obs_startx=random.randrange(200,(display_width-200))
            obs_starty=0
            obs+=1
            b+=2
            a+=1
            audio[4].play()
            if obs>=7:
                obs=1
        if y1==(display_height -100):
            y1=0
        if y_change==0:
            y_change=-(display_height -100)    
        car(x,y)
        if not images[11].get_width()+10<x<display_width-images[11].get_width()+10:
            pygame.mixer.Sound.play(audio[3])
            time.sleep(1.1)
            game_over(b)
        
               
        else:
            None

           
        pygame.display.update()
        if 9<a<20:
           clock.tick(q+30)
        elif 20<=a<=60:
            clock.tick(q+60)
        else:
            clock.tick(q)       
                
                
audio[0].play()

start()


