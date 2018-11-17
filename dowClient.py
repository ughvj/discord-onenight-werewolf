import discord
from player.Player import Player
from job.Villager import Villager
from job.Werewolf import Werewolf
from job.Seer import Seer
from job.Thief import Thief
from job.Madman import Madman
from job.Suisider import Suisider
from management.Master import Master
from time import sleep

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
        self.master = Master(self.players, self.jobs)
        self.phase = 'night'
        for player in self.players:
            yield player.name, self.players_display + '\n' + self.master.nightFalls(player)

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
        outmes = ''
        for i, member in enumerate(self.members):
            outmes += '%d: %s\n' % (i, member.name)
        yield author.name, outmes

    def setp(self, args, author):
        self.players = []
        for i in range(0, len(args)):
            self.players.append(Player(i, self.members[int(args[i])].name))

        self.players_display = ''
        for i in range(0, len(self.players)):
            self.players_display += '%d: %s\n' % (self.players[i].getId(), self.players[i].getName())
        return None

    def getp(self, args, author):
        yield author.name, self.players_display

    def setj(self, args, author):
        self.jobs = []
        for jobname in args:
            self.jobs.append(self.jobdict[jobname])

        self.jobs_display = ''
        for job in self.jobs:
            self.jobs_display += job.getDisplayName() + ' '
        return None

    def getj(self, args, author):
        yield author.name, self.jobs_display

    def initialize(self):
        self.joblist = [Villager(), Werewolf(), Seer(), Thief(), Madman(), Suisider()]
        self.jobdict = {}
        for job in self.joblist:
            self.jobdict[job.getName()] = job

        self.members = []
        for member in self.get_all_members():
            self.members.append(member)

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
