# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:06:49 2018

@author: Vassilis
"""
import constants as c
import pygame as pg
import fish
import groupObjet
import food
import random as rand

class Game:
	def __init__(self):
		pg.init()
		self.display = pg.display.set_mode((c.WIDTH,c.HEIGHT))
		self.background = (0,0,100)
		self.display.fill(self.background)
		self.running =True
		self.clock = pg.time.Clock()
		self.playfish = fish.Fish()
		self.foods = groupObjet.GroupObjet()
		self.foodQty = 10
		for i in range(self.foodQty):
			self.foods.add(food.Food(rand.randrange(0,c.WIDTH),rand.randrange(0,c.HEIGHT)))
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
			self.playfish.move(c.RIGHT,False)
		if(noy):
			self.playfish.move(c.UP,False)
		if(not(noy and nox)):
			if(pressed[pg.K_UP] and not pressed[pg.K_DOWN]):
				self.playfish.move(c.UP,True)
			elif(pressed[pg.K_DOWN] and not pressed[pg.K_UP]):
				self.playfish.move(c.DOWN,True)
			if(pressed[pg.K_LEFT] and not pressed[pg.K_RIGHT]):
				self.playfish.move(c.LEFT,True)
			elif(pressed[pg.K_RIGHT] and not pressed[pg.K_LEFT]):
				self.playfish.move(c.RIGHT,True)

	def run(self):
		while(self.running):
			self.events()
			self.clock.tick(c.FPS)
			self.update(1/c.FPS)
			self.draw()
			pg.display.flip()

		self.cleanup

	def update(self,dt):
		self.playfish.update(dt)
		eat = pg.sprite.spritecollide(self.playfish,self.foods,True)
		for dude in eat:
			self.playfish.eat()
		nbFood = len(self.foods.sprites())
		if(nbFood<self.foodQty):
			for i in range(self.foodQty-nbFood):
				self.foods.add(food.Food(rand.randrange(0,c.WIDTH),rand.randrange(0,c.HEIGHT)))
	def draw(self):
		self.display.fill(self.background)#TO be changed with draw(background or something)
		self.playfish.draw(self.display)
		self.foods.draw(self.display)