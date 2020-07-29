import os
import json
import discord
from datetime import datetime


TOKEN = os.environ.get('DISCORD_TOKEN')
OUT_FILE = './data/idtable.json'
GUILD_ID = 307084334198816769


class MyClient(discord.Client):
    async def on_ready(self):
        guild = self.get_guild(GUILD_ID)

        res = {
            'created_date': datetime.now().strftime("%b %d %Y %H:%M:%S"),
            'channels': {},
            'roles': {}
        }

        for c in guild.channels:
            res['channels'][c.id] = c.name

        for r in guild.roles:
            res['roles'][r.id] = r.name

        with open(OUT_FILE, 'w') as f:
            json.dump(res, f, indent=2)

        await self.close()


client = MyClient()
client.run(TOKEN)
