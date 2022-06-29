import pygame
from sys import exit

class Space(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.space_animation_1=pygame.image.load('images\space.jpg').convert_alpha()
        self.space_animation_2=pygame.image.load('images\space2.jpg').convert_alpha()
        self.space_list=[self.space_animation_1,self.space_animation_2]
        self.index=0
        #self.rotation_index=0
        self.image=self.space_list[int(self.index)]
        print(self.image)
        self.image=pygame.transform.rotozoom(self.image,0,0.5)

    def space_animation(self):
        self.index+=0.07
        #self.rotation_index += 0.001
        if self.index>=len(self.space_list):self.index=0
        self.image=self.space_list[int(self.index)]
        self.image=pygame.transform.rotozoom(self.image,0,0.5)
        
