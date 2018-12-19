import discord
import asyncio
from discord.ext import commands
from itertools import cycle

TOKEN = 'NTIwNjIxNTg5Nzk3MTQyNTQw.DuwiZg.PXs4xkD_I_s10diXg4Upz1VoXqw'

client = commands.Bot(command_prefix = "./")
client.remove_command('help')
status = ['Osu', 'Q&Qアンサーズ', 'Twitter']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(120)

@client.event
async def on_ready():
    #await client.change_presence(game=discord.Game(name='Osu'), status='online')
    print('Bot 1 Ready')
    print('----------Data----------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot: return
    author = message.author
    content = message.content
    channel = message.channel
    print('Channel ( {} ) : User ( {} ) : Messages ( {} )'.format(channel, author, content))
    await client.send_message(discord.Object(id='521357501933813770'), 'Channel ( {} ) : User ( {} ) : Messages ( {} )'.format(channel, author, content))
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    print('Channel ( {} ) : User ( {} ) : Messages ( {} ) (Deleted)'.format(channel, author, content))
    await client.send_message(discord.Object(id='521356081520312322'), 'Channel ( {} ) : User ( {} ) : Messages ( {} ) (Deleted)'.format(channel, author, content))

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name = 'Example Role 1')
    await client.add_roles(member, role)

#help command 'start'
@client.group(pass_context= True)
async def help(ctx):
    if ctx.invoked_subcommand is None:
        await client.say('help command is still in progress')
@help.command(pass_context= True)
async def post(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        title = 'Command = post',
        colour = discord.Colour.blue(),
    )
    embed.set_author(name='A list of commands', icon_url = 'https://orig00.deviantart.net/81f6/f/2007/229/2/0/gif_by_ososhiro.gif')
    embed.add_field(name='Sub commands', value='funfact1 - 10'
                                               '\ncs_map'
                                               '\nhiragana'
                                               '\nkatakana', inline=True)
    embed.add_field(name='Description', value='Fun Fact 1 - 10'
                                              '\nComputer Science Map'
                                              '\n Hiragana Table'
                                              '\nKatakana Table', inline=True)
    await client.send_message(author, embed=embed)

#help command 'end'

#post command 'start'
@client.group(pass_context= True)
async def post(ctx):
    if ctx.invoked_subcommand is None:
        await client.say('Use "./help post"for a list of post commands.')
@post.command(pass_context = True)
async def funfact1(ctx):
    channel = ctx.message.channel
    image1 = 'https://gzanimelist.000webhostapp.com/image/discord%201.png'
    await client.send_message(channel, image1)
@post.command(pass_context = True)
async def funfact2(ctx):
    channel = ctx.message.channel
    image1_2 = 'https://gzanimelist.000webhostapp.com/image/how-human-brain-perceives-work-time-comic-toggl-blog.png'
    await client.send_message(channel, image1_2)
@post.command(pass_context = True)
async def funfact3(ctx):
    channel = ctx.message.channel
    image1_3 = 'https://gzanimelist.000webhostapp.com/image/toggl-how-to-kill-the-dragon-with-9-programming-languages.jpg'
    await client.send_message(channel, image1_3)
    await client.send_message(channel, 'Click the link to see clearer')
@post.command(pass_context = True)
async def funfact4(ctx):
    channel = ctx.message.channel
    image1_4 = 'https://gzanimelist.000webhostapp.com/image/What-kind-of-people-work-at-tech-companies-toggl-blog.png'
    await client.send_message(channel, image1_4)
    await client.send_message(channel, 'Click the link to see clearer')
@post.command(pass_context = True)
async def cs_map(ctx):
    channel = ctx.message.channel
    image2 = 'https://gzanimelist.000webhostapp.com/image/computerscience.png'
    await client.send_message(channel, image2)
@post.command(pass_context = True)
async def hiragana(ctx):
    channel = ctx.message.channel
    image3 = 'https://gzanimelist.000webhostapp.com/image/hiragana.jpg'
    await client.send_message(channel, image3)
@post.command(pass_context = True)
async def katakana(ctx):
    channel = ctx.message.channel
    image4 = 'https://gzanimelist.000webhostapp.com/image/katakana.jpg'
    await client.send_message(channel, image4)

#post command 'end'

@client.command()
async def hi():
    await client.say('Hello')

@client.command()
async def say(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)

@client.command(pass_context = True)
async def clear(ctx, amount = 100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit = int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages Deleted')

@client.command()
async def intro():
    embed = discord.Embed(
        title = 'Python Bot 1',
        description = 'Python Bot made by GZ_GuiZai',
        colour = discord.Colour.blue(),
    )
    embed.set_footer(text='----------End----------')
    embed.set_image(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/7e6112f2-ecb5-45ce-95c6-c1fca1559774/d9kwuji-1d9252a8-320c-4baa-bdea-d58b7eb4882c.png/v1/fill/w_1024,h_802,strp/crying_angel_render_by_animerenders98_d9kwuji-fullview.png')
    embed.set_thumbnail(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/bf98d9d6-3b83-4715-a9c5-332ea61f6018/dakmnsb-3a6fc765-79d9-428b-8a1f-ddefae00d0b3.png/v1/fill/w_800,h_450,strp/_render__005__isis_by_o0oanggraphicso0o_dakmnsb-fullview.png')
    embed.set_author(name='Python Bot 1', icon_url='https://orig00.deviantart.net/81f6/f/2007/229/2/0/gif_by_ososhiro.gif')
    embed.add_field(name='Example Image:', value='-', inline=True)

    await client.say(embed=embed)

@client.command(pass_context=True)
async def inbox(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        title = 'Python Bot 1',
        description = 'Python Bot made by GZ_GuiZai',
        colour = discord.Colour.blue(),
    )
    embed.set_footer(text='----------End----------')
    embed.set_image(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/7e6112f2-ecb5-45ce-95c6-c1fca1559774/d9kwuji-1d9252a8-320c-4baa-bdea-d58b7eb4882c.png/v1/fill/w_1024,h_802,strp/crying_angel_render_by_animerenders98_d9kwuji-fullview.png')
    embed.set_thumbnail(url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/intermediary/f/bf98d9d6-3b83-4715-a9c5-332ea61f6018/dakmnsb-3a6fc765-79d9-428b-8a1f-ddefae00d0b3.png/v1/fill/w_800,h_450,strp/_render__005__isis_by_o0oanggraphicso0o_dakmnsb-fullview.png')
    embed.set_author(name='Python Bot 1', icon_url='https://orig00.deviantart.net/81f6/f/2007/229/2/0/gif_by_ososhiro.gif')
    embed.add_field(name='Example Image:', value='-', inline=True)

    await client.send_message(author, embed=embed)


client.loop.create_task(change_status())
#client.run(TOKEN)
client.run(os.getenv('TOKEN'))
