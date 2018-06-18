# -*- coding: utf-8 -*-
"""
Created on Mon June 18 23:34:36 2018

@author: Vassilis
"""

class SpriteAnim():
	"""Class containing all the necessary information to create an animation"""
	def __init__(self, imagelist, looptime, framelist = None):
		""" #imagelist : list containing frames of animation in order
			#looptime : time to complete one animation loop (in number of frames)
			#framelist : list with time at which to flip frames. Must have length
				n-1 where n = len(imagelist). Also, max(framelist)<looptime 
				If no framelist is provided, frames are evenly distributed"""
		self._imagelist = imagelist
		if(len(imagelist)==1):
			self._looptime = 0
		else:
			self._looptime = looptime

		if(framelist == None):
			finishFrame = int(self._looptime/len(self._imagelist))
			self._framelist = []
			for i in range(len(imagelist)):
				self._framelist.append(finishFrame)
				finishFrame+=finishFrame
		else :
			framelist.sort()
			if(framelist[-1]>looptime):
				raise ValueError("Framelist contains time higher than looptime")
			elif(len(framelist)>=len(imagelist)):
				raise ValueError("Too many frametimes in framelist")
			framelist.append(self._looptime)
			self._framelist = framelist

	def findCurrentImage(self,frame):
		"""Returns the image corresponding to frame"""
		if(self.looptime==0):
			return self.imagelist[0]

		frame = frame%self.looptime
		if(frame<self.framelist[0]):
			return self.imagelist[0]
		i = 0

		while(True):
			if(self.framelist[i]<=frame<self.framelist[i+1]):
				return self.imagelist[i+1]
			i+=1

	def getImageList(self):
		return self._imagelist

	def getLooptime(self):
		return self._looptime

	def getFrameList(self):
		return self._framelist

	imagelist = property(getImageList)
	looptime = property(getLooptime)
	framelist = property(getFrameList)
