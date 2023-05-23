'''
Author: allendred
Date: 2023-05-18 17:01:48
LastEditors: allendred
LastEditTime: 2023-05-23 09:58:58
FilePath: /Play-Monopoly-like-with-ChatGPT/src/monopoly/game.py
Description: Follow your heart
'''
import yaml
from rand.dice import Dice
from .player import Player
from .board import Board
from prompts.prompts import ask
class Game(object):

    def __init__(self,config,player_names=('player1','I')):
        self.config = yaml.load(open(config,'r'),Loader=yaml.FullLoader)
        self.dice = Dice(self.config['dice_num'],self.config['dice_faces'])
        self.board = Board(self.config['board'])
        self.prompts = yaml.load(open(self.config['prompts'],'r'),Loader=yaml.FullLoader)
        self.players = [Player(name,self.config['init_money']) for name in player_names]
    

    def show_result(self):
        print(f'Round: {self.round}')
        for player in self.players:
            print(f'{player.name}: {player.money}')
    
    def start(self):
        # self.board.reset()
        # for player in self.players:
        #     player.reset()
        self.round = 0
        while True:
            self.round += 1
            for player in self.players:
                input(f'>>>{player.name}:')
                _,player_info=player.play(self.dice.roll()[0])
                if player.position >= self.board.max_position:
                    done = True
                    break
                done,board_info = self.board.activate(player)
                prompt_template=f'Now  {player_info}' + '\t'+ board_info +  '\t'+self.prompts['feelings']
                if player.name == self.players[-1].name:
                    ask_info = ask(
                        prefix=f'{self.prompts["prefix"]},you play a role of {player.name}\n',
                        prompt_template= prompt_template,

                    )
                    print(ask_info)
                if done:
                    break
            if done:
                print(f'winner is {player.name} {player.position}')
                break
        # Todo
        # self.board.show() 
        # self.show_result()

if __name__ == "__main__":
    game1 = Game('config/default.yml')  
    game1.start()

