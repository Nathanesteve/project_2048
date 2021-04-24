__version__ = '0.0.1'

from Game2048.game.Main import Game_2048, Game_6561
from Game2048.Visual_game import Visual_game
from Game2048.AI_versus import Versus
from Game2048.statsmaker import Make_stats1, Make_stats2


def Launch_2048():
    Game = Game_2048()
    Game.main()


def Launch_2048_demo():
    AI_one = Game_2048()
    AI_one.demo()


def Launch_6561():
    Game = Game_6561()
    Game.main()


def Launch_2048_visual():
    Visual_game()

