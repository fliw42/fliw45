import pygame

pygame.init()

display_width = 1071
display_height = 427

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
fonImg = pygame.image.load('tttt.png')
chelImg2 = pygame.image.load('chel.png')

def chelImg(x,y):
    gameDisplay.blit(chelImg2, (x,y))
x = (0)
y = (200)	#1
gameDisplay.blit(chelImg2, (x,y))

x_change = 0
y_change = 0

x2 =  (display_width * 0)
y2 = (display_height * 0)	#1

gameDisplay.blit(fonImg, (x2,y2))

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

    x += x_change
    y += y_change

    gameDisplay.blit(fonImg, (x2,y2))
    gameDisplay.blit(chelImg2, (x,y))

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()