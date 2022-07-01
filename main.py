from secrets import choice
import pygame
from sys import exit
from Obstacle import Obstacle
from Player import Player
from Space import Space

def collisons_between_obstacles(obstacles):
    for obstacle in obstacles.sprites():
        list_collsions=pygame.sprite.spritecollide(obstacle,obstacles,False)
        if len(list_collsions)>=2:
            for sprite in list_collsions:
                sprite.blast=True
        


pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((500,600))
player=pygame.sprite.GroupSingle()
player.add(Player())
space=Space()
obstacles=pygame.sprite.Group()
obstacles.add(Obstacle('rock'))
#timmer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1000)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==obstacle_timer:
            obstacles.add(Obstacle(choice(['enemy_ship_type1','enemy_ship_type1','enemy_ship_type1','enemy_ship_type1','enemy_ship_type1','enemy_ship_type2','rock'])))

    screen.blit(space.image, (-80, -30))
    space.space_animation()
    player.draw(screen)
    player.sprite.player_update()
    obstacles.draw(screen)
    obstacles.update()
    collisons_between_obstacles(obstacles)

    pygame.display.update()
    clock.tick(60)