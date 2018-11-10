from player.Player import Player
from job.Villager import Villager
from management.Master import Master

if __name__ == '__main__':
    players = []
    jobs = []
    pnames = ['alpha', 'bravo', 'castle', 'dva']

    for i in range(0, 4):
        players.append(Player(pnames[i]))

    for i in range(0, 6):
        jobs.append(Villager('villager', 'white'))

    master = Master(players, jobs)
