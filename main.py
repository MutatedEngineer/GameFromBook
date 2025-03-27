import pygame
import sys
import os

'''
Переменные
'''
# Сюда поместить переменные-константы
worldx = 1024
worldy = 597
fps = 40
ani = 4
main = True

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0) #Альфа канал, заливка

'''
Объекты
'''
#Функции и классы
class Player(pygame.sprite.Sprite):
    #Класс двигающегося персонажа
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 #Перемещение по X
        self.movey = 0 #Перемещение по Y
        self.frame = 0 #Подсчет кадров

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

class Enemy(pygame.sprite.Sprite): #Создание врага

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images', '#Вставить название файлов' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()



'''
Настройка
'''
#Сюда код, выполняющийся однократно
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
backdrop = pygame.image.load(os.path.join('images', 'country-platform-preview.png'))
backdropbox = world.get_rect()

player = Player() #Создание объекта персонажа и его координаты
player.rect.x = 0
player.rect.y = 290
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10 #Количество пикселей для перемещения

#enemy = Enemy(300, 290, '# Вставить название первого спрайта') #Создание объекта врага
#enemy_list = pygame.sprite.Group() #Список группы врагов
#enemy_list.add(enemy) #Добавление врага в список

'''
Главный цикл
'''
#Игровой цикл
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
