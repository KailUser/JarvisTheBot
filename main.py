import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = 'U!', intents=intents)




@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if "Moderator" in [role.name for role in ctx.author.roles]:
        await member.kick(reason=reason)
        await ctx.send(f'{member} has been kicked by {ctx.author} for {reason}')
    else:
        await ctx.send("You do not have permission to use this command.")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    if "Moderator" in [role.name for role in ctx.author.roles]:
        await member.ban(reason=reason)
        await ctx.send(f'{member} has been banned by {ctx.author} for {reason}')
    else:
        await ctx.send("You do not have permission to use this command.")

@client.command()
async def mute(ctx, member : discord.Member, *, reason=None):
    if "Moderator" in [role.name for role in ctx.author.roles]:
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(f'{member} has been muted by {ctx.author} for {reason}')
    else:
        await ctx.send("You do not have permission to use this command.")

words = ["python", "discord", "bot", "programming", "game"]
current_word = random.choice(words)

@client.command()
async def hangman(ctx):
    await ctx.send("Welcome to Hangman! Type a letter to guess the word.")
    await ctx.send("_ _ _ _ _ _ _")

def check_letter(letter):
    global current_word
    word_list = list(current_word)
    if letter in word_list:
        for i in range(len(word_list)):
            if word_list[i] == letter:
                word_list[i] = letter
        current_word = "".join(word_list)
        return True
    else:
        return False

@client.event
async def on_message(message):
    if message.content.isalpha() and len(message.content) == 1:
        if check_letter(message.content.lower()):
            await message.channel.send("Correct! The word is now:" + ' '.join(current_word))
@client.command()
async def botCommands(ctx):
    embed = discord.Embed(title='Commands', description='List of available commands')
    commands = [f'{c.name} - {c.help}' for c in client.commands]
    embed.add_field(name='Commands', value='\n'.join(commands))
    await ctx.send(embed=embed)

@client.command()
async def clear(ctx, amount: int):
    if "Moderator" in [role.name for role in ctx.author.roles]:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{amount} messages have been deleted.')
    else:
        await ctx.send("You do not have permission to use this command.")
client.run('')
