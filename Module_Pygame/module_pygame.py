import pygame as pg
from PyGame_Player import Player

WIDTH = 800
HEIGHT = 600

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT)) #экран
pg.display.set_caption("PyGame test") #название
player = Player(WIDTH, HEIGHT) #наделение перемнной классом игрока
ball = Player()
all_sprites = pg.sprite.Group() #создание переменной со спрайтами
all_sprites.add(player) #добавление игрока к спрайтам
clock = pg.time.Clock() #создание переменной, контролирующей FPS

while True:
	screen.fill((0, 0, 0)) #заливка экрана
	for event in pg.event.get(): #начало цикла
		if event.type == pg.QUIT: #условие закрытия игры
			pg.quit() #закрытие игры
		elif event.type == pg.KEYDOWN: #условие движения игрока
			if event.key == pg.K_RIGHT: #условие нажатия кнопки
				player.rect.x += 10 #движение по х на 10

	all_sprites.update() #обновление спрайтов
	all_sprites.draw(screen) #рисовка экрана
	pg.display.flip() 
	clock.tick(60) #FPS

