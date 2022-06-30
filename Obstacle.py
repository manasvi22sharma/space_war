from random import randint
import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'rock':
            self.type='rock'
            self.rock_1=pygame.image.load('images\obstacle_rock.png').convert_alpha()
            self_rock_2=pygame.image.load('images\obstacle_rock_2.png').convert_alpha()
            self.frames=[self.rock_1,self_rock_2]
            self.animation_index=0
            self.image=self.frames[self.animation_index]
            self.image=pygame.transform.rotozoom(self.image,0,0.2)
            self.rect=self.image.get_rect(midbottom = (randint(0,625),-5))


    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
        self.image=pygame.transform.rotozoom(self.image,0,0.2)
    def update(self):
        self.animation_state()
        if self.type=='rock':
            self.rect.x -=1
            self.rect.y += 3
        self.rect
        self.destroy()

    def destroy(self):
        if self.rect.y>= 610:
            self.kill()