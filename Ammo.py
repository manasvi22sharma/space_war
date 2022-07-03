from random import randint
import pygame
from sys import exit

class Ammo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type='Ammo'
        self.image=pygame.image.load('images/ammo.png').convert_alpha()
        self.image=pygame.transform.rotozoom(self.image,0,0.15)
        self.rect=self.image.get_rect(midbottom=(randint(0,599),-5))

    def ammo_movement(self):
        self.rect.y+=3
        if self.rect.bottom> 600:
            self.kill()
    def update(self):
        self.ammo_movement()