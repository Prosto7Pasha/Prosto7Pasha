python
import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = hero.image
        self.x = hero.x
        self.y = hero.y
        self.rect = self.image.get_rect()
        self.speed = 5

pygame.init()
screen = pygame.display.set_mode((1600, 1050))
pygame.display.set_caption("SamuraiPingPong")

hero1 = 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            moving = False
            value = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        hero1.rect.y -= hero.speed
        moving = True
        value += 1
    elif keys[pygame.K_s]:
        hero1.rect.y += hero.speed
        moving = True
        value += 1


    if keys[pygame.K_UP]:
        hero2.rect.y -= hero.speed
        moving = True
        value += 1
    elif keys[pygame.K_DOWN]:
        hero2.rect.y += hero.speed
        moving = True
        value += 1


    all_sprites.update(moving)

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()