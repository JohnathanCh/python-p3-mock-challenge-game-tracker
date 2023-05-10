import ipdb

class Player:

    all = []

    def __init__(self, username):
        if 2 <= len(username) <= 16:
            self.username = username
            self._results = []
            self._games_played = []
            Player.all.append(self)
        else:
            raise Exception("INVALID USERNAME: Username must be between 2 and 16 characters")
        
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if 2 <= len(value) <= 16:
            self._username = value
        else:
            raise Exception("Username must be between 2 and 16 characters")
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result is not None:
            self._results.append(new_result)
        return self._results
        
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game:
            self._games_played.append(new_game)
        return self._games_played
    
    def played_game(self, game):
        # ipdb.set_trace()
        return game in self._games_played
    
    def num_times_played(self, game):
        # ipdb.set_trace()
        return game.players().count(self)
    
    @classmethod
    def highest_scored(cls, game):
        # ipdb.set_trace()
        player_dict = {}
        for player in game.players():
            player_dict[player] = game.average_score(player)
        
        max_key = max(player_dict, key=player_dict.get)
        return max_key
                
                
                
                
