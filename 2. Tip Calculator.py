# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:26:45 2023

@author: Dell
"""
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
n = int(input("How many people are splitting this bill? "))
amt = (bill + (tip/100 * bill)) / n
print(f"Each person should pay: ${round(amt,2)}")