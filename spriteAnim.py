# -*- coding: utf-8 -*-
"""
Created on Mon June 18 23:34:36 2018

@author: Vassilis
"""
import pygame as pg
import os

class SpriteAnim():
	"""Class containing all the necessary information to create an animation"""
	def __init__(self, looptime_or_sprit, animationlist = None, framelist = None):
		""" #looptime_or_sprit : time to complete one animation loop (in number of frames) OR another SpriteAnim
			#animationlist : list containing surfaces of the animation in order,
			#framelist : list with time at which to flip frames. Must have length
				n-1 where n = len(animationlist). Also, max(framelist)<looptime 
				If no framelist is provided, frames are evenly distributed"""
		if(isinstance(looptime_or_sprit,SpriteAnim)):
			self._looptime = looptime_or_sprit.looptime
			self._animationlist = looptime_or_sprit.animationlist
			self._framelist = looptime_or_sprit.framelist
		else:
			if(isinstance(animationlist,list)):
				#If a list is provided, add it :
				self._animationlist = animationlist
				if(len(animationlist)==1):
					self._looptime = 0
					self._framelist = [0]
				else:
					self._looptime = looptime_or_sprit
					if(framelist == None):
						self._evenOutAnimation()
					else :
						self._addFramelist(framelist)

				
			else:
				#If no list is provided we are done
				self._looptime = looptime_or_sprit
				self._animationlist = None
				self._framelist = None

	def loadImage(self,folder,filename,frametime=None):
		"""Loads image folder/filename into the animationlist.
		Pass folder = "" if in current working folder.
		frametime is the time at which the frame should switch off.
		Not providing this parameter will evenly space the animation."""
		newframe = pg.image.load(os.path.join(folder,filename))
		self._animationlist.append(newframe)
		if(frametime != None):
			if(frametime>self._looptime):
				raise ValueError("frametime > looptime")
				self._framelist.pop()
				self._framelist.append(frametime)
				self._framelist.append(self._looptime)
		else :
			self._evenOutAnimation()

	def _evenOutAnimation(self):
		frameDist = int(self._looptime/len(self._animationlist))
		self._framelist = []
		finishFrame = frameDist
		for i in range(len(self._animationlist)-1):
			self._framelist.append(finishFrame)
			finishFrame+=frameDist
		self._framelist.append(self._looptime)
		print("made framelist : {}".format(self._framelist))

	def _addFramelist(self,framelist):
		framelist.sort()
		if(framelist[-1]>self.looptime):
			raise ValueError("Framelist contains time higher than looptime")
		elif(len(framelist)!=len(self.animationlist)-1):
			raise ValueError("Framelist is wrong length")

		framelist.append(self._looptime)
		self._framelist = framelist

	# def rotate(self,angle):
	# 	""" Returns SpriteAnim with rotated animation"""
	# 	newAnimationList = []
	# 	for surf in self._animationlist:
	# 		newAnimationList.append(pg.transform.rotate(surf,angle))
	# 	newSprit = SpriteAnim(self._looptime,newAnimationList,self._framelist[:-1])
	# 	return newSprit


	def loadAll(self,folder,filename,framelist=None):
		"""Load all images in folder that have name filename1, filename2...
		Example : a.loadAll("thing.png","") loads thing1.png,thing2.png etc...
		Wipes previous animationlist. """
		self._animationlist = []
		dot = filename.index(".")
		i = 1
		nextfile = filename[:dot]+str(i)+filename[dot:]
		toOpen = os.path.join(folder,nextfile)
		while(os.path.isfile(toOpen)):
			self._animationlist.append(pg.image.load(toOpen))
			i+=1
			nextfile = filename[:dot]+str(i)+filename[dot:]
			toOpen = os.path.join(folder,nextfile)
		if(framelist!=None):
			self._addFramelist(framelist)
		else:
			self._evenOutAnimation()

	def reset(self, looptime,animationlist =None, framelist= None):
		"""Wipes all information on the sprite, and initialize it with new values"""
		self.__init__(looptime,animationlist,framelist)

	def findCurrentImage(self,frame):
		"""Returns the image corresponding to frame"""
		if(self.looptime==0):
			return self.animationlist[0]

		frame = frame%self.looptime
		if(frame<self.framelist[0]):
			return self.animationlist[0]
		i = 0

		while(True):
			if(self.framelist[i]<=frame<self.framelist[i+1]):
				return self.animationlist[i+1]
			i+=1

	def _getAnimationList(self):
		return self._animationlist

	def _getLooptime(self):
		return self._looptime

	def _getFrameList(self):
		return self._framelist

	animationlist = property(_getAnimationList)
	looptime = property(_getLooptime)
	framelist = property(_getFrameList)
