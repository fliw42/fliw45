import pygame

pygame.init()

display_width = 1100
display_height = 450

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('tttt.png')
carImg2 = pygame.image.load('chel.png')

def car2(x,y):
    gameDisplay.blit(carImg2, (x,y))
x = (display_width * 0.01)
y = (display_height * 0.01)	#1
gameDisplay.blit(carImg, (x,y))

x_change = 0
y_change = 0

x2 =  (display_width * 0.2)
y2 = (display_height * 0.6)	#1

gameDisplay.fill(white)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0


        ######################

    x2+= x_change
    y2 += y_change

    gameDisplay.blit(carImg, (x,y))
    car2(x2, y2)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()