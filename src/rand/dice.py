'''
Author: allendred
Date: 2023-05-18 16:37:46
LastEditors: allendred
LastEditTime: 2023-05-18 16:47:21
FilePath: /Play-Monopoly-like-with-ChatGPT/src/rand/dice.py
Description: Follow your heart
'''
import random


class Dice(object):
    def __init__(self,num,faces):
        self.num = num
        self.dice = list(range(1,faces+1))

    def roll(self):
        return random.choices(self.dice,k=self.num)
