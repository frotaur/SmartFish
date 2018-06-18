# -*- coding: utf-8 -*-
"""
Created on Mon June 18 23:27:56 2018

@author: Vassilis
"""
import objet

class ObjetAnime(objet.Objet):
	def __init__(self,pos_or_x ,y = None, *groups):
		"""Objet sub-class that implements some general function to animate the object"""
		super().__init__(pos_or_x,y,*groups)
		self._nbframes = 0 #Counts number of frames elapsed
		self._state = None #The state of the objet, contains the key of the dictionary
		self._spritedict = {} #Keys are different states, each state contains a SpriteAnim


	def _animate(self):
		"""Called each loop. It finds the state of the system and uses currentImage to find the current frame.
		It should set self._image to the right image."""
		pass
