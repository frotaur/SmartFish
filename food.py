# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 18:33:49 2018

@author: Vassilis
"""
import objet
import pygame as pg
import constants as c


class Food(objet.Objet):
	def __init__(self, pos_or_x=(c.WIDTH/2,c.HEIGHT/2),y=None,*groups):
		super().__init__(pos_or_x,y,groups)

		self._image=pg.Surface((5,5))
		self._image.fill((255,255,0))

		self._rect=self.image.get_rect()

		self._rect.center =self._pos.vec

	def draw(self,screen):
		screen.blit(self._image,self._rect)
