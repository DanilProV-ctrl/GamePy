import pygame as pg
import sys
import time
import os
import random

WIDTH = HEIGHT = 750
FPS = 220
clock = pg.time.Clock()

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('PLVSZ')


images = []
path = 'Images/Human/'
path2 = 'Images/BG/'
path3 = 'Images/Zombies'
path4 = 'Images/Left'
path5 = 'Images/Right'
path6 = 'Images/Left'
path7 = 'Images/Right'
pathK = 'Images/Weapons'

Zombie_img = []
BG_imgs = []
Lefty = []
Righty = []
Up = []
Down = []
knf = []

for file_name in os.listdir(path):
    image = pg.image.load(path + os.sep + file_name)
    images.append(image)


for file_name in os.listdir(path2):
    BG_img = pg.image.load(path2 + os.sep + file_name)
    BG = pg.transform.scale(BG_img, (WIDTH, HEIGHT))
    BG_imgs.append(BG_img)


for file_name in os.listdir(path3):
    Zomb_img = pg.image.load(path3 + os.sep + file_name)
    Zombie_img.append(Zomb_img)


for file_name in os.listdir(path4):
    Left = pg.image.load(path4 + os.sep + file_name)
    Lefty.append(Left)


for file_name in os.listdir(path5):
    Right = pg.image.load(path5 + os.sep + file_name)
    Righty.append(Right)


for file_name in os.listdir(path6):
    Upy = pg.image.load(path6 + os.sep + file_name)
    Up.append(Upy)


for file_name in os.listdir(path7):
    Downy = pg.image.load(path7 + os.sep + file_name)
    Down.append(Downy)


for file_name in os.listdir(pathK):
    knife = pg.image.load(pathK + os.sep + file_name)
    knf.append(knife)



class AnimSprite(pg.sprite.Sprite):
    def __init__(self, x, y, img, rot, sz):
        pg.sprite.Sprite.__init__(self)
        self.images = img
        self.index = 0
        self.image = self.images[self.index]
        self.rot = rot
        self.size = sz
        self.image = pg.transform.rotozoom(self.image, self.rot, self.size)
        self.images[0] = self.image
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.index += 0.1
        self.image = self.images[int(self.index % len(self.images))]


class AnimSpriteZ(pg.sprite.Sprite):
    def __init__(self, x, y, img, rot):
        pg.sprite.Sprite.__init__(self)
        self.images = img
        self.index = 0
        self.image = self.images[self.index]
        self.rot = rot
        self.image = pg.transform.rotozoom(self.image, self.rot, 0.2)
        self.images[0] = self.image
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.index += 0.1
        self.image = self.images[int(self.index % len(self.images))]


s = 0.2
human = AnimSprite(x=WIDTH//2, y=HEIGHT//2, img = images, rot=0, sz=s)
left = AnimSprite(x=human.rect.x+50, y=human.rect.y+50, img=Lefty, rot=180, sz=s)
right = AnimSprite(x=human.rect.x+50, y=human.rect.y+50, img=Righty, rot=0, sz=s)
up = AnimSprite(x=human.rect.x+50, y=human.rect.y+50, img = Up, rot=90, sz=s)
down = AnimSprite(x=human.rect.x+50, y=human.rect.y+50, img=Down, rot=-90, sz=s)
Knife = AnimSprite(x=WIDTH//3+20, y=HEIGHT//2+10, img=knf, rot=90, sz=0.02)

i = 200
zombie = AnimSpriteZ(x=WIDTH //3, y=HEIGHT //3, img=Zombie_img, rot=i)

sprites = pg.sprite.Group(Knife, human, zombie)

chslx = [int(220), int(230), int(240), int(250), int(260)]
chsly = [int(320), int(330), int(340), int(350), int(360)]

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit(0)


    screen.blit(BG, (0, 0))

    # Human

    if human.rect.x > int(WIDTH):
        human.rect.x = WIDTH//WIDTH-100

    elif human.rect.x <= int(WIDTH//WIDTH-100):
        human.rect.x = WIDTH

    if human.rect.y > int(WIDTH):
        human.rect.y = WIDTH//WIDTH-100

    elif human.rect.y <= int(WIDTH//WIDTH-100):
        human.rect.y = WIDTH


    # Zombie

    if zombie.rect.x >= int(human.rect.x):
        zombie.rect.x -= 1
        if zombie.rect.x == human.rect.x and zombie.rect.y == human.rect.y:
            print('Game Over')
            sprites.remove(Knife)

    elif zombie.rect.x >= int(-human.rect.x):
        zombie.rect.x += 1
        if zombie.rect.x == human.rect.x and zombie.rect.y == human.rect.y:
            print('Game Over')
            sprites.remove(Knife)

    if zombie.rect.y >= int(human.rect.y):
        zombie.rect.y -= 1
        if zombie.rect.x == human.rect.x and zombie.rect.y == human.rect.y:
            print('Game Over')
            sprites.remove(Knife)

    elif zombie.rect.y >= int(-human.rect.y):
        zombie.rect.y += 1
        if zombie.rect.x == human.rect.x and zombie.rect.y == human.rect.y:
            print('Game Over')
            sprites.remove(Knife)


    keys = pg.key.get_pressed()

    if keys[pg.K_a]:
        human.rect.x -= 6
        sprites.remove(human)
        sprites.remove(down)
        sprites.remove(up)
        sprites.remove(right)
        sprites.add(left)
        right.rect.x = human.rect.x
        left.rect.x = human.rect.x
        up.rect.x = human.rect.x
        down.rect.x = human.rect.x


    if keys[pg.K_d]:
        human.rect.x += 6
        sprites.remove(left)
        sprites.remove(human)
        sprites.remove(down)
        sprites.remove(up)
        sprites.add(right)
        right.rect.x = human.rect.x
        left.rect.x = human.rect.x
        up.rect.x = human.rect.x
        down.rect.x = human.rect.x

    if keys[pg.K_w]:
        human.rect.y -= 6
        sprites.remove(human)
        sprites.remove(right)
        sprites.remove(down)
        sprites.remove(left)
        sprites.add(up)
        right.rect.y = human.rect.y
        left.rect.y = human.rect.y
        up.rect.y = human.rect.y
        down.rect.y = human.rect.y

    if keys[pg.K_s]:
        human.rect.y += 6
        right.rect.y = human.rect.y
        left.rect.y = human.rect.y
        up.rect.y = human.rect.y
        down.rect.y = human.rect.y
        sprites.remove(human)
        sprites.remove(right)
        sprites.remove(up)
        sprites.remove(left)
        sprites.add(down)

    sprites.update()

    sprites.draw(screen)

    pg.display.update()

    clock.tick(FPS)