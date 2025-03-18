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
ALPHA = (0, 255, 0) #альфа канал, заливка

'''
Объекты
'''
# функции и классы
class Player(pygame.sprite.Sprite):
    # класс двигающегося персонажа
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # перемещение по X
        self.movey = 0 # перемещение по Y
        self.frame = 0 # подсчет кадров

        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', 'walk0' + str(i) + '.png')).convert()
            img.convert_alpha() # оптимизацияф альфа диапазона
            img.set_colorkey(ALPHA) # все пиксели этого цвета станут прозрачными
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()

    def control(self, x, y):
        # управление перемещением персонажа
        self.movex += x
        self.movey += y

    def update(self):
        # обновление позиции спрайта
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        # движение влево
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
        # движение вправо
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

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
steps = 10 # количество пикселей для перемещения

'''
Главный цикл
'''
# игровой цикл
while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(- steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(- steps, 0)
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

    world.fill(BLUE)
    world.blit(backdrop, backdropbox)
    player.update()
    player_list.draw(world) # создание постоянного фрейма персонажа
    pygame.display.flip()
    clock.tick(fps)
