from dowClient import dowClient

client = dowClient()

with open('./key', 'r') as f:
    key = f.read()

client.run(key[0:-1])
