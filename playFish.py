# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15:39:16 2018

@author: Vassilis
"""

import constants as c

import fish


class playFish(fish.Fish):
	"""Fish controlled by the player. It implements the function that allows it to be
	controlled"""

	def __init__(self,pos_or_x = (c.WIDTH/2,c.HEIGHT/2),y = None,*groups):
		super().__init__(pos_or_x,y,groups)

	def move(self, direction, active):
		"""Tell fish if it is currently swimming in the specified direction
		Direction : Choose from constants (UP,DOWN,RIGHT,LEFT)
		active : Bool to tell if swimming or not"""
		if(direction == c.UP):
			if(active):
				self._push.y = -1
			else:
				self._push.y = 0
		elif(direction == c.DOWN):
			if(active):
				self._push.y = 1
			else:
				self._push.y = 0
		elif(direction == c.RIGHT):
			if(active):
				self._push.x = 1
			else:
				self._push.x = 0
		elif(direction == c.LEFT):
			if(active):
				self._push.x = -1
			else:
				self._push.x = 0
		else:
			raise ValueError("Provided invalid direction")
