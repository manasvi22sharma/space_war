from secrets import choice
from tkinter import CENTER
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
def display_bullets_left(bullets_left):
    if bullets_left>15:
        bullets_lef_message=test_font.render(f'Bullets: {bullets_left}',False,(93,227,9))
    else:
        bullets_lef_message=test_font.render(f'Bullets: {bullets_left}',False,(245,7,43))
    bullets_lef_message_rect=bullets_lef_message.get_rect(center=(50,50))
    screen.blit(bullets_lef_message,bullets_lef_message_rect)
    
def display_score(start_time):
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Score: {current_time}',False,(10,98,245))
	score_rect = score_surf.get_rect(center = (450,50))
	screen.blit(score_surf,score_rect)
	return current_time

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((500,600))
player=Player()
player_group=pygame.sprite.Group()
player_group.add(player)
space=Space()
obstacles=pygame.sprite.Group()
obstacles.add(Obstacle('rock'))
test_font = pygame.font.Font('font/Pixeltype.ttf', 30)
bullets_left=100
start_time=0
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
                    if bullets_left>0:
                        fire_bullet(player,player_group)
                        bullets_left -=1
        
    if game_active:
        screen.blit(space.image, (-80, -30))
        space.space_animation()
        player_group.draw(screen)
        player_group.update()
        obstacles.draw(screen)
        obstacles.update()
        collisons_between_obstacles(obstacles)
        game_active=collsion_player(obstacles,player_group)
        display_bullets_left(bullets_left)
        display_score(start_time)

    pygame.display.update()
    clock.tick(60)