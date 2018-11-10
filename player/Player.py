class Player():

    def __init__(self, name):
        self.name = name
        self.wins = 0

    def getName(self):
        return self.name

    def Ibecome(self, job):
        self.job = job

    def Iam(self):
        return self.job

    def won(self):
        self.wins += 1

    def howManyWins(self):
        return self.wins
