# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 00:54:06 2023

@author: Dell
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
    




