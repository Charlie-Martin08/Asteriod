import pygame
from os.path import join
from random import randint

pygame.init()
window_width, window_height = 1280, 720
display_surface = pygame.display.set_mode((window_width, window_height))
running = True
pygame.display.set_caption('Asteriod')

surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

player_surf = pygame.image.load(join('..', 'images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (window_width/2,window_height/2))

star_surf = pygame.image.load(join('..', 'images', 'star.png')).convert_alpha()
star_positions = [(randint(0,window_width), randint(0,window_height)) for i in range(20)]

meteor_surf = pygame.image.load(join('..', 'images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (window_width/2, window_height/2))

laser_surf = pygame.image.load(join('..', 'images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (window_width-(window_width-10), window_height-10))

while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False

     display_surface.fill('darkgray')
     for pos in star_positions:
          display_surface.blit(star_surf, pos)
     moving = True
     while moving:
          if player_rect.right < window_width and moving == True:
               player_rect.left += 0.1
          elif player_rect.right == window_width:
               moving_right = False
          else:
               player_rect.left -= 0.1
     laser_rect.bottomleft
     display_surface.blit(player_surf, player_rect)
     display_surface.blit(meteor_surf, meteor_rect)
     display_surface.blit(laser_surf, laser_rect)
     pygame.display.update()

pygame.quit()