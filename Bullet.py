import pygame
from sys import exit

class Bullet(pygame.sprite.Sprite):
    def __init__(self,player_x,player_y):
        super().__init__()
        self.type='Bullet'
        self.fire_animmation1=pygame.image.load('images\player_bullet.png').convert_alpha()
        self.fire_animation_2=pygame.image.load('images\player_bullet2.png').convert_alpha()
        self.frames=[self.fire_animation_2,self.fire_animmation1]
        self.index=0
        self.image=self.frames[int(self.index)]
        self.image=pygame.transform.rotozoom(self.image,0,0.02)
        self.rect=self.image.get_rect(midbottom=(player_x,player_y))

    def fire_animation(self):
        self.index+=0.05
        if self.index>=len(self.frames):self.index=0
        self.image=self.frames[int(self.index)]
        self.image=pygame.transform.rotozoom(self.image,0,0.04)
    def fire_movement(self):
        self.rect.bottom-=2
        if self.rect.bottom< 0:
            self.kill()
    def update(self):
        self.fire_movement()
        self.fire_animation()