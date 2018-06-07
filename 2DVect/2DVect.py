# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 22:45:14 2018

@author: Vassilis
"""

import numpy as np

class Vect2D:
    def __init__(self,x_or_pair=(0,0),y = None):
        if(y == None):
            self.vec = np.array(x_or_pair)
        else:
            self.vec = np.array((x_or_pair,y))
            