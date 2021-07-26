import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
# load image (background, enemy, buttons)
#設定背景圖
background_image = pygame.image.load("Map.png")
background_image = pygame.transform.scale(pygame.image.load('images/Map.png'), (WIN_WIDTH, WIN_HEIGHT))
#設定enemy圖
enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (BTN_WIDTH, BTN_HEIGHT))
#設定hp圖
hp_image = pygame.image.load("hp.png")
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (HP_WIDTH, HP_HEIGHT))
#設定hp_gray圖
hpgray_image = pygame.image.load("hp_gray.png")
hpgray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (HP_WIDTH, HP_HEIGHT))
#設定muse圖
muse_image = pygame.image.load("muse.png")
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
#設定sound圖
sound_image = pygame.image.load("sound.png")
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))
#設定continue圖
continue_image = pygame.image.load("continue.png")
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
#設定pause圖
pause_image = pygame.image.load("pause.png")
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
# set the title
# ... (to be done)
# initialization
pygame.init()
# create window surface
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("My first game")
# clock
clock = pygame.time.Clock()

class Game:
    def __init__(self):
        # window
        # ...(to be done)

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            # event loop
                # ... (to be done)

            # draw background
            #放置背景圖
            win.blit(background_image, (0 ,0 ) )

            # draw enemy and health bar
            #設定放置血條位置跟大小
            pygame.draw.rect(win, (255, 0, 0), [90, 290, 50, 10])
            #放置enemy在血條下方
            win.blit(enemy_image, (80, 300))

            # draw menu (and buttons)
            # 設定放置黑色背景位置跟大小
            pygame.draw.rect(win, (0, 0, 0), [0, 0, 1024, 80])
            #放置hp與hp_gray
            win.blit(hp_image, (432, 0))
            win.blit(hp_image, (472, 0))
            win.blit(hp_image, (512, 0))
            win.blit(hp_image, (552, 0))
            win.blit(hp_image, (592, 0))
            win.blit(hp_image, (432, 40))
            win.blit(hp_image, (472, 40))
            win.blit(hpgray_image, (512, 40))
            win.blit(hpgray_image, (552, 40))
            win.blit(hpgray_image, (592, 40))
            #放置聲音暫停鍵
            win.blit(muse_image, (704, 0))
            win.blit(sound_image, (784, 0))
            win.blit(continue_image, (864, 0))
            win.blit(pause_image, (944, 0))
            # draw time

            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()

run = True
# game loop
while run:
    clock.tick(FPS)
    # event loop (user action)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()




