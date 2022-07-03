import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type='Player'
        self.spaceship_animation_1=pygame.image.load('images\player_ship.png').convert_alpha()
        self.spaceship_animation_2=pygame.image.load('images\player_ship2.png').convert_alpha()
        self.spaceship_animation_3=pygame.image.load('images\player_ship3.png').convert_alpha()
        self.spaceship_list=[self.spaceship_animation_1,self.spaceship_animation_3,self.spaceship_animation_2]
        self.index=0
        self.image=self.spaceship_list[int(self.index)]
        self.image=pygame.transform.rotozoom(self.image,0,0.2)
        self.rect=self.image.get_rect(midbottom=(250,598))
        self.rect = self.rect.inflate(-40, -40)

    def spaceship_animation(self):
        self.index+=0.05
        if self.index>=len(self.spaceship_list):self.index=0
        self.image=self.spaceship_list[int(self.index)]
        self.image=pygame.transform.rotozoom(self.image,0,0.2)
    def player_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.right-=2
        if keys[pygame.K_RIGHT] and self.rect.right <= 500:
            self.rect.left+=2
    def update(self):
        self.player_movement()
        self.spaceship_animation()