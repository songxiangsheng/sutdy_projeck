import time
import pygame
from pygame.locals import *
import random

class PlayerPlane(object):

    def __init__(self, screen):
        # 储存子弹列表
        self.bulle = []
        yj = '/Users/songxiangsheng/study_project/xuxi/yj.jpg'
        # 将飞机icon添加到图片中
        self.image = pygame.image.load(yj).convert()
        # 设置坐标
        self.x = 200
        self.y = 550
        #设置窗口
        self.chuangkou = screen
        self.name = 'player'

    def draw(self):
        self.chuangkou.blit(self.image, (self.x, self.y))
        for tmpe in self.bulle:
            tmpe.draw()


    def Playermove(self,dxs):
        if dxs == 'right':
            print("按下 右键")
            self.x += 10
        if dxs == 'left':
            print("按下 左键")
            self.x -= 10
        if dxs == 'down':
            print("按下 下键")
            self.y += 10
        if dxs =='up':
            print("按下 上键")
            self.y -= 10
        if dxs == 'space':
            print("按下空格")
            self.bulle.append(Bullet(self.chuangkou,self.name, self.x+17.5, self.y-10))

# 新建子弹
class Bullet(object):
    def __init__(self, cd,players, x, y):
        if players == 'player':
            ca = '/Users/songxiangsheng/study_project/xuxi/zd.jpg'
        else:
            ca = '/Users/songxiangsheng/study_project/xuxi/zd.jpg'
        self.df = pygame.image.load(ca).convert()
        self.x = x
        self.y = y
        self.chuangkou = cd  # self.move()
        self.players = players

    # 画子弹
    def draw(self):
        if self.players == 'player':
            self.y -= 5
        elif self.players == 'dj':
            self.y += 5
        self.chuangkou.blit(self.df, (self.x, self.y))

#新建敌机
class Dj(object):
    def __init__(self, screen, x=0, y=0):
        self.x = x
        self.y = y
        dg = '/Users/songxiangsheng/study_project/xuxi/dj.jpg'
        self.image = pygame.image.load(dg).convert()
        self.mov = 'right'
        self.screen = screen

        self.name = 'dj'
        self.bulle = []


    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        for tmpe in self.bulle:
            tmpe.draw()
    def move(self):
        if self.mov == 'right':
            self.x += 4
        elif self.mov == 'left':
            self.x -= 4
        if self.x >= 460:
            self.mov = 'left'
        elif self.x < 0:
            self.mov = 'right'
        randomnum = random.randint(1,100)
        if randomnum in [67,66,88]:

            self.bulle.append(Bullet(self.screen,self.name, self.x+6, self.y+10))

if __name__ == '__main__':
    screen = pygame.display.set_mode((480, 600))
    cf = '/Users/songxiangsheng/study_project/xuxi/bj.png'
    backgound = pygame.image.load(cf).convert()
    player = PlayerPlane(screen)
    dj = Dj(screen)


    while True:
        screen.blit(backgound, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_d or event.key == K_RIGHT:
                    player.Playermove('right')
                elif event.key == K_a or event.key == K_LEFT:
                    player.Playermove('left')
                elif event.key == K_SPACE:
                    player.Playermove('space')
                elif event.key == K_w or event.key == K_DOWN:
                    player.Playermove('down')
                elif event.key == K_s or event.key == K_UP:
                    player.Playermove('up')

        player.draw()
        dj.move()
        dj.draw()



        pygame.display.update()
        time.sleep(0.1)
