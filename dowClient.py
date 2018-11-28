import discord
from player.Player import Player
from job.Villager import Villager
from job.Werewolf import Werewolf
from job.Seer import Seer
from job.Thief import Thief
from job.Madman import Madman
from job.Suicider import Suicider
from job.Topvillager import Topvillager
from job.Wolfking import Wolfking
from management.Master import Master
from time import sleep
import copy

class dowClient(discord.Client):

    async def on_ready(self):
        print('Logged in')
        print('------')

        self.initialize()

    async def on_message(self, message):
        s = message.content.split(' ')
        author = message.author
        try:
            if not s[0] in self.forbidden_commands_per_phase[self.phase]:
                gen = self.commands[s[0]](s[1:], author)
                if gen != None:
                    for mem, mes in gen:
                        await self.send_message(self.createDest(mem), mes)
        except KeyError:
            pass

    def createDest(self, name):
        for member in self.members:
            if member.name == name:
                return member

    def startg(self, args, author):
        self.master = Master(copy.copy(self.players), copy.copy(self.jobs))
        self.phase = 'night'
        for player in self.players:
            yield player.name, self.players_display + '\n' + self.jobs_display + '\n' + self.master.nightFalls(player)

    def act(self, args, author):
        for player in self.players:
            if author.name == player.getName():
                if len(args) == 0:
                    yield player.name, self.master.act(player.getName(), -1)
                else:
                    yield player.name, self.master.act(player.getName(), int(args[-1]))

        if self.master.haveAllPlayerActed():
            self.phase = 'day'
            sleep(5)
            outmes = self.master.sunrise()
            for player in self.players:
                yield player.name, outmes

    def vote(self, args, author):
        for player in self.players:
            if author.name == player.getName():
                yield player.name, self.master.vote(player.getName(), int(args[-1]))

        if self.master.haveAllPlayerVoted():
            self.phase = 'preparation'
            sleep(3)
            outmes = self.master.gameset()
            for player in self.players:
                yield player.name, outmes

    def getm(self, args, author):
        outmes = '\n'.join([
            '%d: %s' % (i, member.name)
            for i, member in enumerate(self.members)
        ])
        yield author.name, outmes

    def setp(self, args, author):
        self.players = [Player(i, self.members[int(args[i])].name) for i in range(0, len(args))]
        self.players_display = '\n'.join([
            '%d: %s' % (self.players[i].getId(), self.players[i].getName())
            for i in range(0, len(self.players))
        ])
        return None

    def getp(self, args, author):
        yield author.name, self.players_display

    def setj(self, args, author):
        self.jobs = [self.jobdict[jobname] for jobname in args]
        self.jobs_display = ' '.join([job.getDisplayName() for job in self.jobs])
        return None

    def getj(self, args, author):
        yield author.name, self.jobs_display

    def initialize(self):
        self.joblist = [Villager(), Werewolf(), Seer(), Thief(), Madman(), Suicider(), Topvillager(), Wolfking()]
        self.jobdict = {job.getName():job for job in self.joblist}
        self.members = [member for member in self.get_all_members()]

        self.commands = {
            '/start': self.startg,
            '/act': self.act,
            '/vote': self.vote,
            '/getm': self.getm,
            '/setp': self.setp,
            '/getp': self.getp,
            '/setj': self.setj,
            '/getj': self.getj
        }

        self.forbidden_commands_per_phase = {
            'preparation': ['/act', '/vote'],
            'night': ['/start', '/vote', '/setj', '/setp'],
            'day': ['/start', '/act', '/setj', '/setp']
        }

        self.phase = 'preparation'
