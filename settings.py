import pygame


pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

y1, y2, y3 = 0, 0, 0
speed1, speed2, speed3 = 20, 30, 40
timer = 0
stop = False
speed_stop = False

font = pygame.font.Font(None, int(width*0.05))
slot1 = ["7", "Bar", "Zitrone", "Kirsche", "Glocke", "Diamant", "Melone", "Orange", "Trauben", "Stern"]
slot2 = ["7", "Bar", "Zitrone", "Kirsche", "Glocke", "Diamant", "Melone", "Orange", "Trauben", "Stern"]
slot3 = ["7", "Bar", "Zitrone", "Kirsche", "Glocke", "Diamant", "Melone", "Orange", "Trauben", "Stern"]
save_text = [None, None, None]
