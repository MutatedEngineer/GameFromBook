import pygame
import sys
import os

'''
Переменные
'''
# Сюда поместить переменные
worldx = 960
worldy = 720
fps = 40
ani = 4
main = True

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)

'''
Объекты
'''
# функции и классы
'''
Настройка
'''
# сюда код, выполняющийся однократно
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

'''
Главный цикл
'''
# игровой цикл
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    world.fill(BLUE)
    world.blit(backdrop, backdropbox)
    pygame.display.flip()
    clock.tick(fps)