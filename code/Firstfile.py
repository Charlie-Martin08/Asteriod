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

star_surf = pygame.image.load(join('..', 'images', 'star.png')).convert_alpha()
star_positions = [(randint(0,window_width), randint(0,window_height)) for i in range(20)]

while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False

     display_surface.fill('darkgray')
     for pos in star_positions:
          display_surface.blit(star_surf, pos)
     x+= 0.1
     display_surface.blit(player_surf, (x,150))
     pygame.display.update()

pygame.quit()