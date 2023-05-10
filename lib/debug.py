#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")
    game1 = Game("This is a good title")
    # game_error = Game("")

    player1 = Player("solder69")
    # player_error1 = Player("s")
    # player_error2 = Player("dsflkjsdaflkhsadglkasdjg")
    
    result1 = Result(player1, game1, 100)



    ipdb.set_trace()
    
