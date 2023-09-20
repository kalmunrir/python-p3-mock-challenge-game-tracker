class Game:
    def __init__(self, title):
        self.title = title

    def __get_title(self):
        return self._title
    def __set_title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title
        else:
            raise Exception("Title must be a string")
    title = property(__get_title, __set_title)

    def results(self):
        return ([result for result in Result.all if result.game == self])

    def players(self):
        all_players = []
        for result in self.results():
            if result.player not in all_players:
                all_players.append(result.player)
        return all_players

    def average_score(self, player):
        total = 0
        for result in self.results():
            if result.player == player:
                total += result.score
        return (total / len([ result for result in self.results() if result.player == player]))

class Player:
    def __init__(self, username):
        self.username = username

    def __get_username(self):
        return self._username
    def __set_username(self, username):
        if isinstance(username, str) and len(username) > 2 and len(username) < 16:
            self._username = username
        else:
            raise Exception("Username must be a string between 2 and 16 characters in length")
    username = property(__get_username, __set_username)

    def results(self):
        return ([result for result in Result.all if result.player == self])

    def games_played(self):
        played_games = []
        for result in self.results():
            if result.game not in played_games:
                played_games.append(result.game)
        return played_games

    def played_game(self, game):
        return (True if game in self.games_played() else False)

    def num_times_played(self, game):
        all_games = [result.game for result in self.results()]
        return (all_games.count(game))

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    def _get_score(self):
        return self._score
    def _set_score(self, score):
        if isinstance(score, int) and score >= 1 and score <= 5000 and not hasattr(self, 'score'):
            self._score = score
        else:
            raise Exception('Score must be an int, between 1 and 5000, and not exist')
    score = property(_get_score, _set_score)

    def _get_player(self):
        return self._player
    def _set_player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception('Player must be of type Player')
    player = property(_get_player, _set_player)

    def _get_game(self):
        return self._game
    def _set_game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception('Game must be of type Game')
    game = property(_get_game, _set_game)