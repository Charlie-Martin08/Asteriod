import pygame
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
     def __init__(self, groups):
          super().__init__(groups)
          self.image = pygame.image.load(join('..', 'images', 'player.png')).convert_alpha()
          self.rect = self.image.get_frect(center = (window_width/2,window_height/2))

     def update(self):
               # keys = pygame.key.get_pressed()
     # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
     # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
     # player_direction = player_direction.normalize() if player_direction else player_direction
     # player_rect.center += player_direction * player_speed * dt
     # if player_rect.bottom > window_height or player_rect.top < 0:
     #      player_direction.y *= -1
     # if player_rect.right > window_width or player_rect.left < 0 :
     #      player_direction.x *=-1
     # player_rect.center += player_direction * player_speed * dt


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
player = Player(all_sprites)


# player_surf = pygame.image.load(join('..', 'images', 'player.png')).convert_alpha()
# player_rect = player_surf.get_frect(center = (window_width/2,window_height/2))
# player_direction = pygame.math.Vector2()
# player_speed = 300

star_surf = pygame.image.load(join('..', 'images', 'star.png')).convert_alpha()
star_positions = [(randint(0,window_width), randint(0,window_height)) for i in range(20)]

meteor_surf = pygame.image.load(join('..', 'images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (window_width/2, window_height/2))

laser_surf = pygame.image.load(join('..', 'images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, window_height-20))

while running:
     dt = clock.tick() /1000
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
     
     all_sprites.update()

     display_surface.fill('darkgray')
     for pos in star_positions:
          display_surface.blit(star_surf, pos)

     laser_rect.bottomleft
     display_surface.blit(meteor_surf, meteor_rect)
     display_surface.blit(laser_surf, laser_rect)
     all_sprites.draw(display_surface)
     pygame.display.update()

pygame.quit()