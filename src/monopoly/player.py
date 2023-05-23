"""
Author: allendred
Date: 2023-05-18 17:51:58
LastEditors: allendred
LastEditTime: 2023-05-20 16:48:23
FilePath: /Play-Monopoly-like-with-ChatGPT/src/monopoly/player.py
Description: Follow your heart
"""
from rand.dice import Dice
class Player(object):
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.position = 0
    
    def reset(self):
        self.money = 0
    
    def buy(self,price):
        self.money -= price
        return self.money
    
    def sell(self,price):
        self.money += price
        return self.money
    
    # @property
    # def status(self):
    #     return self.position >= self.board.max_position
    
    def play(self,offset):
        self.position += offset
        print(f'{self.name} get {offset} point move to {self.position}')
        return self.position,f'{self.name} move to {self.position}'
    
    
    def __str__(self):
        return f'{self.name}: {self.money}'
    
    