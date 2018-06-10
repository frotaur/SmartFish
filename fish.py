# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:27:24 2018

@author: Vassilis
"""
import constants as c
import pygame as pg
import objet
from Vect2D import Vect2D as v

class Fish(objet.Objet):
	def __init__(self,pos_or_x = (c.WIDTH/2,c.HEIGHT/2),y = None,*groups):
		super().__init__(pos_or_x,y,groups)

		self._image = pg.Surface((20,20))
		self._image.fill((255,0,0))

		self._rect = self.image.get_rect()

		self._vit = v.Vect2D(0,0)
		self._acc = v.Vect2D(0,0)

		self._force = 2000 #This describes basically how well the fish can change direction
		self._mass = 3

		self._score = 0
	def update(self,dt):
		#Normalise acceleration to match newton's law in all directions
		if(self._acc != v.Vect2D(0,0)):
			self._acc.r = self._force/self._mass
		#Equations of motion :
		self._vit += self._acc*dt-(c.ETA/self._mass)*self._vit
		self._pos += self._vit*dt
		self._rect.center= self._pos.vec

		#This is just to stop the fish when its too slow
		if(self._vit.r<1 and self._acc.r == 0):
			self._vit*= 0
		#Eventually need to add the animations here too
	
	def draw(self,screen):
		screen.blit(self._image, self._rect)

	def _get_pos(self):
		return self._pos

	def move(self, direction, active):
		"""Tell fish if it is currently swimming in the specified direction
		Direction : Choose from constants (UP,DOWN,RIGHT,LEFT)
		active : Bool to tell if swimming or not"""
		if(direction == c.UP):
			if(active):
				self._acc.y = -1
			else:
				self._acc.y = 0
		elif(direction == c.DOWN):
			if(active):
				self._acc.y = 1
			else:
				self._acc.y = 0
		elif(direction == c.RIGHT):
			if(active):
				self._acc.x = 1
			else:
				self._acc.x = 0
		elif(direction == c.LEFT):
			if(active):
				self._acc.x = -1
			else:
				self._acc.x = 0
		else:
			raise ValueError("Provided invalid direction")

	def eat(self):
		self._score+=1
		print("Ate a little shit, score = {}".format(self.score))

	def _get_score(self):
		return self._score
	score = property(_get_score)