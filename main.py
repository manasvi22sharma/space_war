from secrets import choice
from tkinter import CENTER
import pygame
from sys import exit

from scipy.misc import central_diff_weights
from Ammo import Ammo
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
    player_group.add(Bullet(pos[0]+15,pos[1]))

def collsion_player(obstacles,player_group):
    list_collison=pygame.sprite.groupcollide(player_group,obstacles,True,False)
    for i in list_collison:
        #    print('stop')
        for sprite in list_collison[i]:
            if i.type=='Player':
                pygame.sprite.collide_rect_ratio(0.5)(i,sprite)
                i.kill()
                return False
            else:sprite.blast=True
    #print(list_collison)
    return True
def display_bullets_left(bullets_left):
    if bullets_left>10:
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
def ammo_collected(ammo_group,player_group,bullets_left):
    list=pygame.sprite.groupcollide(player_group,ammo_group,False,True)
    for i in list:
        if i.type=='Bullet':
            i.kill()
        bullets_left=bullets_left+10 
    return bullets_left 



pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((500,600))
player=Player()
player_group=pygame.sprite.Group()
#player_group.add(player)
space=Space()
obstacles=pygame.sprite.Group()
obstacles.add(Obstacle('rock'))
ammo_group=pygame.sprite.Group()
test_font = pygame.font.Font('font/Pixeltype.ttf', 30)
bullets_left=25
start_time=0
game_active=False
score=0
#timmer
obstacle_timer = pygame.USEREVENT + 1
enemy_time=2000
ammo_time=20000
pygame.time.set_timer(obstacle_timer,enemy_time)
ammo_timer =pygame.USEREVENT+2
pygame.time.set_timer(ammo_timer,20000)
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
            if event.type==ammo_timer:
                enemy_time -=200
                if enemy_time<=100:
                    enemy_time=100
                    ammo_time=3000
                pygame.time.set_timer(ammo_timer,ammo_time) 
                pygame.time.set_timer(obstacle_timer,enemy_time)   
                ammo_group.add(Ammo())
        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                start_time = int(pygame.time.get_ticks() / 1000)
                player_group.add(player)
                bullets_left=25
                enemy_time=2000
                ammo_time=20000
                pygame.time.set_timer(ammo_timer,ammo_time) 
                pygame.time.set_timer(obstacle_timer,enemy_time) 
    screen.blit(space.image, (-80, -30))
    if game_active:
        space.space_animation()
        player_group.draw(screen)
        player_group.update()
        obstacles.draw(screen)
        obstacles.update()
        collisons_between_obstacles(obstacles)
        game_active=collsion_player(obstacles,player_group)
        ammo_group.draw(screen)
        ammo_group.update()
        bullets_left=ammo_collected(ammo_group,player_group,bullets_left)
        display_bullets_left(bullets_left)
        score=display_score(start_time)

    else:
        game_font=pygame.font.SysFont('comicsans',65,True)
        score_font=pygame.font.SysFont('Corbel',35,True)
        game_name=game_font.render(f'SPACE WARS',False,(93,227,9))
        score_message=score_font.render(f'Score : {score}',False,(10,98,245))
        game_name_rect = game_name.get_rect(center = (250,150))
        score_rect = score_message.get_rect(center = (250,250))
        start_message=test_font.render('Press Space to start!!',True,(245,7,43))
        start_message_rect=start_message.get_rect(center=(250,400))
        screen.blit(score_message,score_rect)
        screen.blit(game_name,game_name_rect)
        screen.blit(start_message,start_message_rect)
        obstacles.empty()
        player_group.empty()



    pygame.display.update()
    clock.tick(60)