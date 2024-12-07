import pygame
import random
pygame.init()
root = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Catch the rectangle")
font_sz = 40
spd = 7
background = pygame.transform.scale(pygame.image.load("bg.jpg"), (700, 700))


clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
        
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, 700 - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, 700 - self.rect.height), 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color(color))
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
        
    def move_enemy(self):
        self.rect.move_ip(self.velocity)
        
        boundary_hit = False
        
        if self.rect.left <= 0 or self.rect.right >= 700:
            boundary_hit = True
            self.velocity[0] = -self.velocity[0]
        if self.rect.top <= 0 or self.rect.bottom >= 700:
            boundary_hit = True
            self.velocity[1] = -self.velocity[1]
        
        if boundary_hit:
            self.image.fill("#00ff00")

sprite_grp = pygame.sprite.Group()
s1 = Player("yellow", 50, 50)  
s1.rect.x = random.randint(0, 650)
s1.rect.y = random.randint(0, 650)

s2 = Enemy("red", 70, 70)  
s2.rect.x = random.randint(0, 630)
s2.rect.y = random.randint(0, 630)
sprite_grp.add(s1)
sprite_grp.add(s2)

running, win = True, False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    font = pygame.font.Font(None, font_sz)
    root.fill((0, 0, 0))
    root.blit(background, (0,0))
    if not win:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * spd
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * spd
        s1.move(x_change, y_change)
        s2.move_enemy()

        if s1.rect.colliderect(s2.rect):
            sprite_grp.remove(s2)
            win = True

    if win:
        text = font.render("YOU WON!!", True, pygame.Color("Blue"))
        root.blit(text, (350, 350))
        
    sprite_grp.draw(root)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()