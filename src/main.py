#main.py
import os #for importing env vars for  the bot to use
from twitchio.ext import commands

O_TOKEN= "oauth:s4ey0c8x9ld7grngvgq6kbcrqkim92"
CLIENT_ID= "gp762nuuoqcoxypju8c569th9wz7q5"
BOT_NICK= "TheUntamableBot"
BOT_PREFIX= "!"
CHANNEL=['DJ_Mozzie']
bot = commands.Bot(
    #irc_token=O_TOKEN,
    token='2o06jrffqpay58miglygnlky4sgrj7',
    #client_id=CLIENT_ID,
    prefix='!',
    #nick=BOT_NICK,
    initial_channels=['#TheUntamableBot'])

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot.ws
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


if __name__ == '__main__':
    bot.run()
