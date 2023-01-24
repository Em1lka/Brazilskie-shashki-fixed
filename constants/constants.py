import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ANTIQUEWHITE = (255, 239, 219)
BURNTSIENNA = (138, 54, 15)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
