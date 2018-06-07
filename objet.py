# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:54:56 2018

@author: Vassilis
"""
import pygame as pg

class Objet(pg.sprite.Sprite):
    
    def __init__(self,*groups):
        pg.sprite.Sprite.__init__(self,groups)
    
    def update(self):
        """ Override this function to update the object"""
        pass