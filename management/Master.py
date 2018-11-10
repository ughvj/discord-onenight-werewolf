import random

class Master():

    def __init__(self, players, jobs):
        # deal
        for player in players:
            while True:
                candidate = random.choice(jobs)
                if not candidate.usingSomeone():
                    break

            player.Ibecome(candidate)
            candidate.use()

            print(str(player.Iam()))
        
        self.players = players

        # debug
        for job in jobs:
            print(str(job.usingSomeone()))

        self.nighttime = False

    def start(self):
        self.nighttime()
        for player in players:
            self.players.actAtNight()
        self.daytime()

    def nighttime(self):
        self.nighttime = True

    def daytime(self):
        self.nighttime = False
