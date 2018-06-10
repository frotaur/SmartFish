# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:45:14 2018

@author: Vassilis
"""

import numpy as np

class Vect2D:
	def __init__(self,vec_or_x=(0,0),y=None):
		"""Constructor expects a pair of numbers, in a tuple, list or Vect2D"""
		if(y!=None):
			self._vec=np.array([vec_or_x,y])
		elif(isinstance(vec_or_x,Vect2D)):
			self._vec = np.array(vec_or_x._vec)
		else:
			self._vec = np.array(vec_or_x)

	def get_x(self):
		return self._vec[0]
	def get_y(self):
		return self._vec[1]
	def get_r(self):
		return self.norm()
	def get_phi(self):
		if(self.x==0 and self.y == 0):
			return 0
		return np.deg2rad(np.arctan2(self.y,self.x))
	def get_vec(self):
		return (self.x,self.y)

	def set_x(self,x):
		self._vec[0] =x
	def set_y(self,y):
		self._vec[1]=y
	def set_r(self,r):
		self._vec = r/self.norm()*self._vec
	def set_phi(self,phi):
		""" Set phi in degrees"""
		r=self.r
		self.x = np.cos(np.deg2rad(phi))*r
		self.y = np.sin(np.deg2rad(phi))*r
	def set_vec(self,vec):
		if(len(vec)==2):
			self._vec = np.array(vec)
		else:
			raise ValueError("vec attribute of Vect2D is supposed to be length 2")
	x = property(get_x,set_x)
	y = property(get_y,set_y)
	r = property(get_r,set_r)
	phi = property(get_phi,set_phi)
	vec = property(get_vec)

	def __str__(self):
		return "({},{})".format(self._vec[0],self._vec[1])

	def __add__(self, v2):
		"""Addition operator with +"""
		return Vect2D(self._vec+v2._vec)

	def __sub__(self, v2):
		"""Substraction operator with -"""
		return self+(-1)*v2

	def __mul__(self,v2):
		"""Works as multiplication by a scalar, or dot product for 2 vectors"""
		if(isinstance(v2,Vect2D)):
			return np.dot(self._vec,v2._vec)
		else:
			return Vect2D(v2*self._vec)

	def __rmul__(self,nb):
		"""Multiplication with a number of the left."""
		return Vect2D(nb*self._vec)

	def __neg__(self):
		return self*(-1)

	def __xor__(self,v2):
		"""Cross product operator with ^"""
		return np.cross(self._vec,v2._vec)

	def __eq__(self,v2):
		"""Test equality of vectors. Careful if using with float vectors"""
		return -1e-13<(self-v2).norm()<1e-13

	def norm(self):
		"""Returns the norm of the vector"""
		return np.sqrt(self.normSq())

	def normSq(self):
		"""Returns the norm squared of the vector"""
		return self.x*self.x+self.y*self.y