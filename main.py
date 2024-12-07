import pygame
import random
pygame.init()
root = pygame.display.set_mode((700,700))
pygame.display.set_caption("Catch the rectangle")
font = 40
spd = 7

clock = pygame.time.Clock()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,color, height, width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(pygame.Color(color))  
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
        


running,win = True,False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()