# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:54:56 2018

@author: Vassilis
"""
import pygame as pg

class Objet(pg.sprite.Sprite):

	def __init__(self, *groups):
		pg.sprite.Sprite.__init__(self,groups)
		self._image = None
		self._rect = None

	def update(self):
		""" Override this function to update the object"""
		pass

	def _get_img(self):
		return self._image
	def _get_rect(self):
		return self._rect

	def draw(self, screen):
		pass
	image = property(_get_img)
	rect = property(_get_rect)