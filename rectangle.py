import pygame
pygame.init()
screen=pygame.display.set_mode((300,300))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(20,60,60,20))
    pygame.display.flip()