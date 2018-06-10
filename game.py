# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:06:49 2018

@author: Vassilis
"""
import constants as c
import pygame as pg
import fish

class Game:
	def __init__(self):
		pg.init()
		self.display = pg.display.set_mode((c.WIDTH,c.HEIGHT))
		self.background = (0,0,100)
		self.display.fill(self.background)
		self.running =True
		self.clock = pg.time.Clock()
		self.fish = fish.Fish()

	def cleanup(self):
		pg.quit()

	def events(self):
		for ev in pg.event.get():
			if ev.type == pg.QUIT:
				self.running = False
		pressed = pg.key.get_pressed()
		noy = not(pressed[pg.K_UP] or pressed[pg.K_DOWN])
		nox = not(pressed[pg.K_LEFT] or pressed[pg.K_RIGHT])
		if(nox):
			self.fish.move(c.RIGHT,False)
		if(noy):
			self.fish.move(c.UP,False)
		if(not(noy and nox)):
			if(pressed[pg.K_UP] and not pressed[pg.K_DOWN]):
				self.fish.move(c.UP,True)
			elif(pressed[pg.K_DOWN] and not pressed[pg.K_UP]):
				self.fish.move(c.DOWN,True)
			if(pressed[pg.K_LEFT] and not pressed[pg.K_RIGHT]):
				self.fish.move(c.LEFT,True)
			elif(pressed[pg.K_RIGHT] and not pressed[pg.K_LEFT]):
				self.fish.move(c.RIGHT,True)

	def run(self):
		while(self.running):
			self.events()
			self.clock.tick(c.FPS)
			self.update(1/c.FPS)
			self.draw()
			pg.display.flip()

		self.cleanup

	def update(self,dt):
		self.fish.update(dt)
	def draw(self):
		self.display.fill(self.background)#TO be changed with draw(background or something)
		self.fish.draw(self.display)