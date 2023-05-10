import pdb

class Game:
    def __init__(self, title):
        if len(title) == 0:
            raise Exception("Title must be longer than 0")
        else:
            self._title = title
            self._results = []
            self._players = []
            
    @property
    def title(self):
        return self._title
    
    def results(self, new_result=None):
        from classes.result import Result
        if new_result:
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player:
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        # pdb.set_trace()
        scores = [result.score for result in player.results()]
        avg = sum(scores)/len(scores)
        return avg