from random import randint
import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'rock':
            self.type='rock'
            self.frame_1=pygame.image.load('images\obstacle_rock.png').convert_alpha()
            self.frame_2=pygame.image.load('images\obstacle_rock_2.png').convert_alpha()
            self.frames=[self.frame_1,self.frame_2]
            self.animation_index=0
            self.image=self.frames[self.animation_index]
            self.image=pygame.transform.rotozoom(self.image,0,0.2)
            self.rect=self.image.get_rect(midbottom = (randint(20,625),-5))
        if type == 'enemy_ship_type1':
            self.type='enemy_ship_type1'
            self.frame_1=pygame.image.load('images\enemy_ship1.png').convert_alpha()
            self.frame_2=pygame.image.load('images\enemy_ship1_2.png').convert_alpha()
            self.frames=[self.frame_1,self.frame_2]
            self.animation_index=0
            self.image=self.frames[self.animation_index]
            self.image=pygame.transform.rotozoom(self.image,0,0.2)
            self.rect=self.image.get_rect(midbottom = (randint(0,499),-5))
        if type == 'enemy_ship_type2':
            self.type='enemy_ship_type2'
            self.frame_1=pygame.image.load('images\enemy_ship2.png').convert_alpha()
            self.frame_2=pygame.image.load('images\enemy_ship2_2.png').convert_alpha()
            self.frames=[self.frame_1,self.frame_2]
            self.animation_index=0
            self.image=self.frames[self.animation_index]
            self.image=pygame.transform.rotozoom(self.image,0,0.2)
            self.rect=self.image.get_rect(midbottom = (randint(0,599),-5))


    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        self.image=pygame.transform.rotozoom(self.image,0,0.2)
    def update(self):
        self.animation_state()
        if self.type=='rock':
            self.rect.x -=1
            self.rect.y += 2
        if self.type=='enemy_ship_type1':
            self.rect.y += 4
        if self.type=='enemy_ship_type2':
            self.rect.y +=5
        self.rect
        self.destroy()

    def destroy(self):
        if self.rect.y>= 610:
            self.kill()