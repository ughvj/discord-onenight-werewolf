class Job():

    def __init__(self):
        self.using = False

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDisplayName(self, dname):
        self.dname = dname

    def getDisplayName(self):
        return self.dname

    def IamWerewolf(self, werewolf):
        self.werewolf = werewolf

    def amIWerewolf(self):
        return self.werewolf

    def use(self):
        self.using = True

    def usingSomeone(self):
        return self.using
