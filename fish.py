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
	def __init__(self,pos = (c.WIDTH/2,c.HEIGHT/2)):
		super().__init__()

		self._image = pg.Surface((30,30))
		self._image.fill((255,0,0))

		self._rect = self.image.get_rect()

		self._pos = v.Vect2D(pos)

		self._vit = v.Vect2D(0,0)
		self._acc = v.Vect2D(0,0)

	def update(self,dt):
		self._vit += self._acc*dt
		self._pos += self._vit*dt
		self._rect.center= self._pos.vec
		#Eventually need to add the animations here too
		
	def _get_pos(self):
		return self._pos

	pos = property(_get_pos)