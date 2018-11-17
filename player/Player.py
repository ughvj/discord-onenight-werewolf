class Player():

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.acted = False
        self.voted = False
        self.vote_count = 0

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def Ibecome(self, job):
        self.job = job

    def Iam(self):
        return self.job

    def actedPlayer(self):
        self.acted = True

    def haveIActed(self):
        return self.acted

    def votedPlayer(self):
        self.voted = True

    def haveIVoted(self):
        return self.voted

    def someoneWasVoted(self):
        self.vote_count += 1

    def howMuchIWasVoted(self):
        return self.vote_count

    def IVotedThisPlayer(self, vote_target):
        self.vote_target = vote_target

    def whomDidIVoted(self):
        return self.vote_target
