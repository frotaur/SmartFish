# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:02:16 2018

@author: Vassilis
"""
import pygame as pg
class GroupObjet(pg.sprite.Group):
	"""Re-implementation of sprite.Group class. Simply overrides
	the original "draw" function to make sure it calls actually 
	calls the "draw" function of contained sprites, instead of
	blitting them itself.
	It would be better to code a personalised one since I actually
	use "Objet" instead of "Sprite" as a base class, but it should 
	do for now. This however should contain "Objet", not "Sprite" """
	def draw(self, surface):
		todraw = self.sprites()
		for spr in todraw :
			spr.draw(surface)