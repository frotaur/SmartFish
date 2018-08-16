# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:54:56 2018

@author: Vassilis
"""
import pygame as pg
from Vect2D import Vect2D as v


class Objet(pg.sprite.Sprite):
	"""Base class for all objects, using Sprite from pygame.
	Doesn't do much more than sprite, just uses a custom position
	and add some properties. It's just to know what is happening."""

	def __init__(self,pos_or_x ,y = None, *groups):
		pg.sprite.Sprite.__init__(self,groups)
		self._image = None
		self._rect = None
		self._pos = v.Vect2D(pos_or_x,y)

	def update(self):
		""" Override this function to update the object"""
		pass

	def _get_img(self):
		return self._image

	def _get_rect(self):
		return self._rect

	def _get_pos(self):
		return self._pos

	def collide(self, group, dokill):
		"""Find Objet in group that collide with self and returns them in a list.
		Uses the _rect attribute to determine collision, will fail otherwise.
		dokill : boolean, if True then removes colliding sprites from group."""
		return pg.sprite.spritecollide(self, group, dokill)

	def draw(self, screen):
		"""Override this function to tell how to draw the object"""
		pass

	image = property(_get_img)
	rect = property(_get_rect)
	pos = property(_get_pos)
