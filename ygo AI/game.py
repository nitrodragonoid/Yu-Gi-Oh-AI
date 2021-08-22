import pygame
import cards
import random


pygame.init()  
screen = pygame.display.set_mode((600, 800))  
done = False  
  
##### Defining game objects #####
c1 = cards.crystal_clear_wing_synchro_dragon
deck_list_1 = {1 : c1}
deck_list_2 = {}

deck1 = []
deck2 = []
for i in range(1,41):
    deck1.append(i)
    deck2.append(i)
####### Game functions #######

def shuffle(deck):
    random.shuffle(deck)

def draw(deck,deck_list):
    if len(deck) > 0:
        card_drawn = deck[0]
        deck.pop()
        return deck_list[card_drawn]
    else:
        return False

#def start_hand(deck, deck_list):


#def summon(card,position,zone):
    



##### defining constants #####  
grey = (155, 155, 155)
deck = (150, 150, 150)
fieldA = (0,150,255) 
fieldb = (255,150,0)
Red = (255,0,0) 
Blue = (0,0,255)  
empty = (50,50,50)
white = (255,255,255)  
color = empty
x = 110
y = 120 
Y = 475
Hand1 = 0

phases = ["draw", "standby", "main 1", "battle", "main 2", "end"]

##### GAME LOOP #####


while not done:  
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True
    #Drawing field
        for i in range(5):  
            pygame.draw.rect(screen, fieldA, [x+(80*i), y, 70, 102]) 
            pygame.draw.rect(screen, fieldA, [x+(80*i), y+110, 70, 102]) 

            pygame.draw.rect(screen, fieldb, [x+(80*i), Y, 70, 102]) 
            pygame.draw.rect(screen, fieldb, [x+(80*i), Y+110, 70, 102]) 
    #Draw extra deck and field spell
        pygame.draw.rect(screen, deck, [x+(400), y-5, 75, 107])
        pygame.draw.rect(screen, deck, [x+(400), y+(115), 75, 107])

        pygame.draw.rect(screen, deck, [x+(400), Y-5, 75, 107])
        pygame.draw.rect(screen, deck, [x+(400), Y+(115), 75, 107])

        pygame.draw.rect(screen, deck, [x+(80*3), y+(115*2), 70, 101])
        pygame.draw.rect(screen, deck, [x+(80), y+(115*2), 70, 101])
    #Draw deck and graveyard
        pygame.draw.rect(screen, deck, [x-85, y-5, 75, 107])
        pygame.draw.rect(screen, deck, [x-85, y+(115), 75, 107])

        pygame.draw.rect(screen, deck, [x-85, Y-5, 75, 107])
        pygame.draw.rect(screen, deck, [x-85, Y+(115), 75, 107])

        image = pygame.image.load('1.jpg')
        image = pygame.transform.scale(image, (70, 101))
        screen.blit(image, (x, Hand1))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                print("Get you game on")
            if event.key == pygame.K_d:
                print("I draw!")


    pygame.display.flip()  
