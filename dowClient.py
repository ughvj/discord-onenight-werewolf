import discord
from management.PlayerMaster import PlayerMaster
from management.JobMaster import JobMaster
from management.GameMaster import GameMaster
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
        self.gmaster = GameMaster(self.pmaster.getPlayersList(), self.jmaster.getJobsList())
        self.phase = 'night'
        for player in self.pmaster.getPlayersList():
            yield player.getName(), self.pmaster.getPlayersDisplay() + '\n' + self.jmaster.getJobsDisplay() + '\n' + self.gmaster.nightFalls(player)

    def act(self, args, author):
        for player in self.pmaster.getPlayersList():
            if author.name == player.getName():
                if len(args) == 0:
                    yield player.getName(), self.gmaster.act(player.getName(), -1)
                else:
                    yield player.getName(), self.gmaster.act(player.getName(), int(args[-1]))

        if self.gmaster.haveAllPlayerActed():
            self.phase = 'day'
            sleep(5)
            outmes = self.gmaster.sunrise()
            for player in self.pmaster.getPlayersList():
                yield player.getName(), outmes

    def vote(self, args, author):
        for player in self.pmaster.getPlayersList():
            if author.name == player.getName():
                yield player.getName(), self.gmaster.vote(player.getName(), int(args[-1]))

        if self.gmaster.haveAllPlayerVoted():
            self.phase = 'preparation'
            sleep(3)
            outmes = self.gmaster.gameset()
            for player in self.pmaster.getPlayersList():
                yield player.getName(), outmes

    def getm(self, args, author):
        outmes = '\n'.join([
            '%d: %s' % (i, member.name)
            for i, member in enumerate(self.members)
        ])
        yield author.name, outmes

    def setp(self, args, author):
        self.pmaster = PlayerMaster([self.members[int(args[i])].name for i in range(0, len(args))])
        return None

    def getp(self, args, author):
        yield author.name, self.pmaster.getPlayersDisplay()

    def setj(self, args, author):
        self.jmaster = JobMaster(args)
        return None

    def getj(self, args, author):
        yield author.name, self.jmaster.getJobsDisplay()

    def initialize(self):

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
