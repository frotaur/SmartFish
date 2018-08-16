# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15:39:16 2018

@author: Vassilis
"""
import pygame as pg
import fish
import constants as c
import food
from Vect2D import Vect2D as v
import random as rand
import spriteAnim as spri
import os


class AIFish(fish.Fish):
	def __init__(self,pos_or_x = (c.WIDTH/2,c.HEIGHT/2),y = None,*groups):
		super().__init__(pos_or_x,y,groups)
		self._sightr = 60
		self._wallDist = 60
		self._stateCirc = {}
		tempspri = spri.SpriteAnim(0)
		tempspri.loadAll(os.path.join("Graphics","circle"),"greenCircle.png")
		self._stateCirc["green"] = tempspri
		tempspri = spri.SpriteAnim(0)
		tempspri.loadAll(os.path.join("Graphics","circle"),"redCircle.png")
		self._stateCirc["red"] = tempspri
		self._circ = "red"

		#testing
		tempspri = spri.SpriteAnim(0)
		tempspri.loadAll(os.path.join("Graphics","circle"),"mouth.png")
		self._mouth = tempspri
		#testing

	def update(self,dt, environ):
		self._move(environ)
		super().update(dt)

	def draw(self, screen):
		super().draw(screen)

		circle = pg.transform.scale(self._stateCirc[self._circ].findCurrentImage(self._nbframes),(self._sightr*2,self._sightr*2))
		therect = circle.get_rect()

		#testing
		circle2 = self._mouth.findCurrentImage(self._nbframes)
		therect2 = circle2.get_rect()
		self._boucherel.phi = self._angle
		therect2.center = (self.pos+self._boucherel).vec
		#testing
		therect.center = self.pos.vec

		screen.blit(circle,therect)
		screen.blit(circle2,therect2)

	def _move(self,environ):
		"""Sees the surroundings and chooses to move"""
		closefood = False
		for thing in environ :
			if(isinstance(thing, food.Food)):
				diff = thing.pos-self.pos
				if(diff.r<self._sightr):
					self._push = diff
					closefood = True
					self._circ = "green"

		if(not closefood):
			self._circ = "red"
			if(self._push!=v.Vect2D(0,0)):
				self._chooseDir(self._checkSides())
			else:
				self._push = v.Vect2D(1,0)

	def _checkSides(self):
		"""Returns None if no collision, allowed angle interval otherwise"""
		interval = None
		if(self.pos.x+self._wallDist>c.WIDTH):
			interval = (90,270)
		elif(self.pos.x-self._wallDist<0):
			interval = (-90,90)

		if(self.pos.y+self._wallDist>c.HEIGHT):
			interval = (-180,0)
		elif(self.pos.y-self._wallDist<0):
			interval = (0,180)

		return interval

	def _chooseDir(self,interval = None):
		"""Choose a "random" direction. If constrained is True, interval should be a tuple
		containing two angles from which to pick the new direction."""
		changer = 120
		if(self._nbframes%changer == 0):
			if(interval is None):
				self._push.phi += (rand.random()-0.5)*180
		else :
			self._push.phi += (rand.random()-0.5)*2

		if(interval is not None):
			self._push.phi = rand.randrange(interval[0],interval[1])
