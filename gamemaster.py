import discord
from player.Player import Player
from job.Villager import Villager
from management.Master import Master


client = discord.Client();

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('/start'):
        players = []
        jobs = []
        pnames = ['alpha', 'bravo', 'castle', 'dva']

        for i in range(0, 4):
            players.append(Player(pnames[i]))

        for i in range(0, 6):
            jobs.append(Villager('villager', 'white'))

        master = Master(players, jobs)
        dest = None

        for member in client.get_all_members():
            if member.name == 'ugh':
                dest = member
                
        await client.send_message(dest, 'hi')

with open('./key', 'r') as f:
    key = f.read()

client.run(key[0:-1])
