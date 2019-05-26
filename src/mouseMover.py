'''
Created on May 26, 2019

@author: jpeuker
'''

import pyautogui

class MouseMover:
    def __init__(self, stepsize):
        self.stepsize = stepsize
        
    def move(self):
        print("raton...")
        self.stepsize = -self.stepsize
        pyautogui.moveRel(self.stepsize, 0)