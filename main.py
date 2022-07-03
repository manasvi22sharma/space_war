from secrets import choice
import pygame
from sys import exit
from Bullet import Bullet
from Obstacle import Obstacle
from Player import Player
from Space import Space

def collisons_between_obstacles(obstacles):
    for obstacle in obstacles.sprites():
        list_collsions=pygame.sprite.spritecollide(obstacle,obstacles,False)
        if len(list_collsions)>=2:
            for sprite in list_collsions:
                sprite.blast=True
        
def fire_bullet(player,player_group):
    pos=player.rect.midtop
    player_group.add(Bullet(pos[0],pos[1]))

def collsion_player(obstacles,player_group):
    list_collison=pygame.sprite.groupcollide(player_group,obstacles,True,False)
    for i in list_collison:
        if i.type=='Player':
            return False
        #    print('stop')
        for sprite in list_collison[i]:
            sprite.blast=True
    #print(list_collison)
    return True


pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((500,600))
player=Player()
player_group=pygame.sprite.Group()
player_group.add(player)
space=Space()
obstacles=pygame.sprite.Group()
obstacles.add(Obstacle('rock'))
game_active=True
#timmer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1000)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type==obstacle_timer:
                obstacles.add(Obstacle(choice(['enemy_ship_type1','enemy_ship_type1','enemy_ship_type1','enemy_ship_type1','enemy_ship_type1','enemy_ship_type2','rock'])))
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fire_bullet(player,player_group)
        
    if game_active:
        screen.blit(space.image, (-80, -30))
        space.space_animation()
        player_group.draw(screen)
        player_group.update()
        obstacles.draw(screen)
        obstacles.update()
        collisons_between_obstacles(obstacles)
        game_active=collsion_player(obstacles,player_group)

    pygame.display.update()
    clock.tick(60)