# Work with Python 3.6
import discord, requests, json

TOKEN = 'NTE0MDQ0MjQyOTYwODQyNzYy.DtQ5xA.2WR5-62vw-aPRq8IHL84ILT1Zpc'

client = discord.Client()



@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'There'
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!players'):

        r = requests.get('https://mcapi.us/server/status?ip=pytatki-beta.pl')
        r_dict = json.loads(r.text)
        msg = "Na serwerze MC jest {0}/{1} graczy".format(r_dict["players"]["now"],r_dict["players"]["max"])
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
