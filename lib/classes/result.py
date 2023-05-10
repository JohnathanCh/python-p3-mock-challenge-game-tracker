from classes.player import Player
from classes.game import Game
class Result:

    all = []

    def __init__(self, player, game, score):
        if type(score) is int and 1 <= score <= 5000:
            self.player = player
            player.results(self)
            player.games_played(game)
            
            self.game = game
            game.results(self)
            game.players(player)
            
            self.score = score
            Result.all.append(self)
        else:
            raise Exception("Score must be integers between 1 and 5000")
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if type(score) is int and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be integers between 1 and 5000")
        
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if isinstance(new_player, Player):
            self._player = new_player
        else:
            raise Exception("Player must be an instance of the Player class")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
            self._game = new_game
        else:
            raise Exception("Game must be an instance of the Game class")





