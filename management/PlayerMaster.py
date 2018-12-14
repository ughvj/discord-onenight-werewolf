from player.Player import Player

class PlayerMaster():

    def __init__(self, player_names):
        self.players = [Player(i, player_names[i]) for i in range(0, len(player_names))]
        self.players_display = '\n'.join([
            '%d: %s' % (self.players[i].getId(), self.players[i].getName())
            for i in range(0, len(self.players))
        ])

    def getPlayersList(self):
        return self.players

    def getPlayersDisplay(self):
        return self.players_display
