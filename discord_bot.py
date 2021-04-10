import discord

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('hello!')
    if message.content.startswith('!Alex'):
            await message.channel.send('Alex likes cock in his ass!')
    if message.content.startswith('!alexPic'):
        await message.channel.send('https://cdn.discordapp.com/attachments/800763978782998558/829000997769838662/20210406_153320.jpg')
    if message.content.startswith('!Alfie'):
        await message.channel.send('Alfie likes cock in his ass')

#@client.group(invoke_without_command=True)
#async def help(ctx, ball=8):
 #   em = discord.Embed(title = "help", description = "use >help <command> for extended i")

  #  em.add_field(name = "Moderation", value = "kick,ban,warn")
   # em.add_field(name = "Fun", value = ball,reverse")

    #await ctx (embed = em)

#@help.command()
#async def kick(ctx):

        #em = discord.Embed(title = "ping",description = kicks a member from the guild,col)
        #em.add_field(name = "**Syntax**", value = ">kick <member> [reason]")

        #await ctx.send(embed = em))


client.run('ODMwMzkzMzE4OTAxODA5MTg0.YHGCCw.NxjJ-dl3Rq0BpKIWjCjQPSOF2U0')



