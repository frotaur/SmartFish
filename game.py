# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 19:06:49 2018

@author: Vassilis
"""
import constants as c
import pygame as pg

class Game :
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((c.WIDTH,c.HEIGHT))
        self.display.fill((0,0,100))
        self.running = True
        self.clock = pg.time.Clock()

    def cleanup(self):
        pg.quit()
    
    def events(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                self.running = False
    
    def run(self):
        while(self.running):
            self.events()
            self.clock.tick(c.FPS)
        
        self.cleanup()