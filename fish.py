# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:27:24 2018

@author: Vassilis
"""
import constants as c

import objetAnime
import spriteAnim as spri
from Vect2D import Vect2D as v
import os
import pygame as pg
import math as m
import food

class Fish(objetAnime.ObjetAnime):
	def __init__(self,pos_or_x = (c.WIDTH/2,c.HEIGHT/2),y = None,*groups):
		super().__init__(pos_or_x,y,groups)
		self._force = 2000 #This describes basically how well the fish can change direction
		self._mass = 3
		self._score = 0
		self._angle = 0

		self._statedict = {}
		tempSpri = spri.SpriteAnim(60)
		tempSpri.loadAll(os.path.join("Graphics","rest"),"rest.png")
		self._statedict["stop"] = tempSpri

		tempSpri2 = spri.SpriteAnim(30)
		tempSpri2.loadAll(os.path.join("Graphics","swim"),"swim.png")
		self._statedict["move"] = tempSpri2

		self._vit = v.Vect2D(0,0)
		self._acc = v.Vect2D(0,0)

		self._state = "stop"
		self._image = self._statedict[self._state].findCurrentImage(0)
		self._rect = self.image.get_rect()

	def update(self,dt):
		#Normalise acceleration to match newton's law in all directions
		if(self._acc != v.Vect2D(0,0)):
			self._acc.r = self._force/self._mass
		#Equations of motion :
		self._rect = self._image.get_rect()
		self._vit += self._acc*dt-(c.ETA/self._mass)*self._vit
		self._pos += self._vit*dt
		self._rect.center = self._pos.vec
		collided = {"x" : False,"y":False}

		if(self._rect.centerx+self._rect.width/2>c.WIDTH):
			self._pos.x = c.WIDTH-self._rect.width/2
			collided["x"] = True
		elif(self._rect.centerx-self._rect.width/2<0):
			self._pos.x = self._rect.width/2
			collided["x"] = True

		if(self._rect.centery+self._rect.height/2>c.HEIGHT):
			self._pos.y = c.HEIGHT-self._rect.height/2
			collided["y"] = True
		elif(self._rect.centery-self._rect.height/2<0):
			self._pos.y = self._rect.height/2
			collided["y"] = True

		if(collided["x"] == True):
			self._rect.center = self._pos.vec
			self._vit.x= 0
		if(collided["y"]== True):
			self._rect.center = self._pos.vec
			self._vit.y= 0
		#This is just to stop the fish when its too slow
		if(self._vit.r<1 and self._acc.r == 0):
			self._vit*= 0

		#Animate :
		self._animate()
	def _animate(self):
		self._nbframes = (self._nbframes+1)%c.MAXLOOPFRAME
		
		if(self._vit != v.Vect2D(0,0)):
				self._angle = self._vit.phi
		
		if(self._acc == v.Vect2D(0,0)):
			self._state = "stop"
		elif(self._acc!=v.Vect2D(0,0)):
			if(self._state != "move"):
				self._nbframes = 0
			self._state = "move"
			#self._angle = self._acc.phi
			#for anim in self._statedict:
			#	self._statedict[anim] = self._statedict[anim].rotate(self._acc.phi-90)
		self._image = pg.transform.rotate(self._statedict[self._state].findCurrentImage(self._nbframes),-self._angle-90)

	def draw(self,screen):
		screen.blit(self._image, self._rect)

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