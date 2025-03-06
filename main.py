import pygame
import sys
import os

'''
Переменные
'''
# Сюда поместить переменные-константы
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
class Player(pygame.sprite.Sprite):
    # класс двигающегося персонажа
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'walk0' + str(i) + '.png')).convert()
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
'''
Настройка
'''
# сюда код, выполняющийся однократно
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'stage.png'))
backdropbox = world.get_rect()

player = Player() # создание объекта персонажа и его координаты
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
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
    player_list.draw(world) # создание постоянного фрейма персонажа
    pygame.display.flip()
    clock.tick(fps)
