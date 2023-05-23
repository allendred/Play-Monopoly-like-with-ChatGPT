'''
Author: allendred
Date: 2023-05-18 20:25:56
LastEditors: allendred
LastEditTime: 2023-05-23 09:45:41
FilePath: /Play-Monopoly-like-with-ChatGPT/src/monopoly/board.py
Description: Follow your heart
'''
import yaml
class Board(object):

    def __init__(self,board_config):
        self.board = yaml.load(open(board_config,'r'),Loader=yaml.FullLoader)['board']
        self.max_position = len(self.board)
        print(self.board)
        
    def activate(self,player):
        return self.run(self.board[player.position]['event'],player)
    
    def run(self,event_type,player):
        board_station = player.position
        if event_type == 'forward':
            player.position += self.board[board_station]['value']
           # print(f'{self.board[board_station]["description"]} -> {player.name} forward {self.board[board_station]["value"]} step move to {player.position}')
        elif event_type == 'backward':
            player.position -= self.board[board_station]['value']
        print(f'{self.board[board_station]["description"]}  {player.name}  step move to {player.position}')
        if player.position >= self.max_position:
            print(f'{player.name} win')
            return True,f'{player.name} win'
        return False,f'{self.board[board_station]["description"]}  {player.name} step move to {player.position}'
