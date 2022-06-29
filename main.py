import pygame
from sys import exit
from Player import Player
from Space import Space

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((500,600))
player=pygame.sprite.GroupSingle()
player.add(Player())
space=Space()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(space.image, (-80, -30))
    space.space_animation()
    player.draw(screen)
    player.sprite.player_update()
    pygame.display.update()
    clock.tick(60)