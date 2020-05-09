import os

from util.bot import bot

if __name__ == '__main__':
    bot.run(os.environ.get("TOKEN"))
