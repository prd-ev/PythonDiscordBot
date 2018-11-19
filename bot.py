# Work with Python 3.6
import discord, requests, json

TOKEN = 'NTE0MDQ0MjQyOTYwODQyNzYy.DtQ5xA.2WR5-62vw-aPRq8IHL84ILT1Zpc'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = "There"
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!mcplayers'):
        r = requests.get('https://mcapi.us/server/status?ip=pytatki-beta.pl')
        r_dict = json.loads(r.text)
        msg = "Na serwerze MC jest {0}/{1} graczy".format(r_dict["players"]["now"],r_dict["players"]["max"])
        await client.send_message(message.channel, msg)
    
    elif message.content.startswith('!weather'):
        location = message.content[8:]
        try:
            api_key = "cad63d58be4335873686cf6efaf774bc"
            url = "http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}".format(location, api_key)
            response = requests.get(url)
            response.raise_for_status()
            weather_data = json.loads(response.text)
            msg = "Weather data for: {0}\nTemperature: {1} Celcius degrees\nHumidity: {2} %\nPressure: {3}hPa".format(
                weather_data['name'],
                int(weather_data['main']['temp']-272),
                weather_data['main']['humidity'],
                weather_data['main']['pressure']
            )
            await client.send_message(message.channel, msg)
        except Exception:
            msg = "Wrong syntax, try !weather [where]"
            await client.send_message(message.channel, msg)
        
    elif message.content.startswith('!trump'):
        r = requests.get('https://api.whatdoestrumpthink.com/api/v1/quotes/random')
        r_dict = json.loads(r.text)
        msg = "Donald Trump: {0}".format(r_dict['message'])
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
