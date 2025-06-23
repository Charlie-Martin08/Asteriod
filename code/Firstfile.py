import pygame
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
     def __init__(self, groups):
          super().__init__(groups)
          self.image = pygame.image.load(join('..', 'images', 'player.png')).convert_alpha()
          self.rect = self.image.get_frect(center = (window_width/2,window_height/2))
          self.direction = pygame.Vector2()
          self.speed = 300

     def update(self, dt):
          keys = pygame.key.get_pressed()
          self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
          self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
          self.direction = self.direction.normalize() if self.direction else self.direction
          self.rect.center += self.direction * self.speed * dt

          recent_keys = pygame.key.get_just_pressed()
          if recent_keys[pygame.K_SPACE]:
               print('fire laser')

class Star(pygame.sprite.Sprite):
     def __init__(self, groups, star_surf):
          super().__init__(groups)
          self.image = star_surf
          self.rect = self.image.get_frect(center = (randint(0,window_width), randint(0,window_height)))


pygame.init()
window_width, window_height = 1280, 720
display_surface = pygame.display.set_mode((window_width, window_height))
running = True
pygame.display.set_caption('Asteriod')
clock = pygame.time.Clock()

surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('..', 'images', 'star.png')).convert_alpha()
for i in range (20):
     Star(all_sprites, star_surf)
player = Player(all_sprites)

meteor_surf = pygame.image.load(join('..', 'images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (window_width/2, window_height/2))

laser_surf = pygame.image.load(join('..', 'images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, window_height-20))

while running:
     dt = clock.tick() /1000
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
     
     all_sprites.update(dt)

     display_surface.fill('darkgray')

     all_sprites.draw(display_surface)

     pygame.display.update()

pygame.quit()