# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:45:14 2018

@author: Vassilis
"""

import numpy as np

class Vect2D:
	def __init__(self,vec=(0,0)):
		"""Constructor expects a pair of numbers, in a tuple, list or Vect2D"""
		if(type(vec)==Vect2D):
			self._vec = np.array(vec._vec)
		else:
			self._vec = np.array(vec)

	def get_x(self):
		return self._vec[0]
	def get_y(self):
		return self._vec[1]

	def set_x(self,x):
		self._vec[0] =x
	def set_y(self,y):
		self._vec[1]=y

	x = property(get_x,set_x)
	y = property(get_y,set_y)

	def __str__(self):
		return "({},{})".format(self._vec[0],self._vec[1])

	def __add__(self, v2):
		return Vect2D(self._vec)

a = Vect2D((1,2))