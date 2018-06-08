# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:27:24 2018

@author: Vassilis
"""
import constants as c
import pygame as pg
import objet

class Fish(objet.Objet):
	def __init__(self,pos = (c.WIDTH/2,c.HEIGHT/2)):
		super().init()

		self._image = pg.Surface(30,30)
		self._image.fill((255,0,0))

		self._rect = self.image.get_rect()

		self._x = pos[0]
		self._y = pos[1]

		self._vx = pos[0]
		self._vy = pos[1]

	def update(self):
		pass