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
ALPHA = (255, 255, 255) #Альфа канал, заливка

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
        self.health = 10 #Здоровье персонажа
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images\\hero\\walk', 'walk' + str(i) + '.png')).convert()
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
        #обновление позиции спрайта
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        # движение влево
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
        #Движение вправо
        if self.movex > 0:
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]

        #Хиты
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.health -= 1
            print(self.health)


class Enemy(pygame.sprite.Sprite): #Создание врага
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0  # Перемещение по X
        self.frame = 0
        self.counter = 0  # Переменная счетчик перемещения
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(os.path.join('images\\enemy', 'enemy_walk' + str(i) + '.png')).convert()
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
    def move(self):
        '''
        Перемещение врага
        '''
        distance = 50
        speed = 5
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        elif self.counter >= distance and self.counter <= distance * 2:
            self.rect.x -= speed
            self.frame += 1
            if self.frame > 3 * ani:
                self.frame = 0
            self.image = self.images[self.frame // ani]
        else:
            self.counter = 0

        self.counter += 1

class Level():
    def bad(lvl, eloc):
        if lvl == 1:
            enemy = Enemy(eloc[0], eloc[1])  # Создание объекта врага
            enemy_list = pygame.sprite.Group()  # Список группы врагов
            enemy_list.add(enemy)  # Добавление врага в список
        if lvl == 2:
            print('Level' + str(lvl))

        return enemy_list

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
player.rect.y = 490
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10 #Количество пикселей для перемещения

eloc = []
eloc = [600, 467]
enemy_list = Level.bad(1, eloc)

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

    world.fill(BLUE) #Мир заливка цвета
    world.blit(backdrop, backdropbox) #Мир картинка заднего фона

    player.update() #Cоздание постоянного фрейма персонажа
    player_list.draw(world)
    enemy_list.draw(world) #Cоздание постоянного фреймов врагов из списка
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)
