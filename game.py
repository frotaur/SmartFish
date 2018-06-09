# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:06:49 2018

@author: Vassilis
"""
import constants as c
import pygame as pg
import fish
from Vect2D import Vect2D as v

class Game:
	def __init__(self):
		pg.init()
		self.display = pg.display.set_mode((c.WIDTH,c.HEIGHT))
		self.display.fill((0,0,100))
		self.running =True
		self.clock = pg.time.Clock()
		self.fish = fish.Fish()

	def cleanup(self):
		pg.quit()

	def events(self):
		for ev in pg.event.get():
			if ev.type == pg.QUIT:
				self.running = False
			if ev.type == pg.KEYDOWN:
				self.fish._acc+=v.Vect2D([1,0])
	def run(self):
		while(self.running):
			self.events()
			self.clock.tick(c.FPS)
			self.update(1/c.FPS)
			self.display.fill((0,0,100))
			self.draw()
			pg.display.flip()

		self.cleanup

	def update(self,dt):
		self.fish.update(dt)
	def draw(self):
		self.display.blit(self.fish.image, self.fish.rect)