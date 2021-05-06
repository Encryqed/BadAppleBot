import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="a!")

@bot.event
async def on_ready():
    print("Badapple on discord reaction in python")

@bot.command()
async def badapple(ctx: commands.Context):
    for i in range(0, 80, 10):
        message = await ctx.send("‌")
        for j in range(i, 10+i):
            emoji = discord.utils.get(bot.emojis, name=f"b{j}")
            await message.add_reaction(emoji)
        await asyncio.sleep(2)

bot.run("bot token here")
