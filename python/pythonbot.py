import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(command_prefix=";")


roundTime = 30
emoji1 = "1️⃣"
emoji2 = "2️⃣"

cur_nom = {}


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(';instructions'))


@bot.command()
async def instructions(ctx):
    embed = discord.Embed(title="Instructions",
                          description='The prefix for this bot is ";"',
                          color=16580705)
    embed.add_field(name="1.", value='Always put your full nomination in quotations ("")', inline=True)
    embed.add_field(name="2.", value='Nomination example: ;nominate "Your Nomination | Origin"',
                    inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def nominate(ctx, nomination):
    if nomination in cur_nom.keys():
        embed = discord.Embed(title="Nomination Incomplete",
                              description=nomination + " is already nominated.")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=nomination + " Nominated",
                              description=nomination + " was added to the nominees list.")
        cur_nom[nomination] = ""
        await ctx.send(embed=embed)
        embed = discord.Embed(title="Please assign an image to " + nomination, description="Web links or uploaded images are accepted.")
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel  # Checks to see if the image posted is by the same User in the same Channel

        message = await bot.wait_for('message', check=check)
        if message.attachments:
            image = message.attachments[0].url
            embed = discord.Embed(title="Image Added",
                                  description="Your image has been added successfully")
            embed.set_thumbnail(url=image)
            cur_nom[nomination] = image
            await ctx.send(embed=embed)
            print(cur_nom)
        else:
            image = message.content
            embed = discord.Embed(title="Image Added",
                                  description="Your image has been added successfully")
            embed.set_thumbnail(url=image)
            cur_nom[nomination] = image
            await ctx.send(embed=embed)
            print(cur_nom)


@nominate.error
async def nominate_error(ctx, error):
    embed = discord.Embed(title="Nomination Error",
                          description="Your nomination was not entered. Make sure that your ENTIRE nomination is within quotations or that you provided an image when prompted.",
                          color=0xff0000)
    print(error)
    await ctx.send(embed=embed)


@bot.command()
async def delnom(ctx, nominee):
    if nominee in cur_nom.keys():
        print(nominee)
        embed = discord.Embed(title=nominee + " Removed",
                              description=nominee + " was removed from the nominees list.")
        embed.set_thumbnail(url=cur_nom[nominee])
        del cur_nom[nominee]
        await ctx.send(embed=embed)


@delnom.error
async def delnom_error(ctx, error):
    embed = discord.Embed(title="Nomination Not Found",
                          description="The nomination was not found. Check spelling by using the ;nominations command.",
                          color=0xff0000)
    print(error)
    await ctx.send(embed=embed)


@bot.command()
async def update_image(ctx, nominee):
    if nominee in cur_nom.keys():
        embed = discord.Embed(title=nominee + " selected. Please choose an image.")
        embed.set_thumbnail(url=cur_nom[nominee])
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel  # Checks to see if the image posted is by the same User in the same Channel

        message = await bot.wait_for('message', check=check)
        if message.attachments:
            image = message.attachments[0].url
            embed = discord.Embed(title="Image Added",
                                  description="Your image has been added successfully")
            embed.set_thumbnail(url=image)
            cur_nom[nominee] = image
            await ctx.send(embed=embed)
            print(cur_nom)
        else:
            image = message.content
            embed = discord.Embed(title="Image Added",
                                  description="Your image has been added successfully")
            embed.set_thumbnail(url=image)
            cur_nom[nominee] = image
            await ctx.send(embed=embed)
            print(cur_nom)
    else:
        embed = discord.Embed(title=nominee + " not found. Please check spelling and try again.")
        await ctx.send(embed=embed)


@bot.command()
async def clear_nominations(ctx):
    embed = discord.Embed(title="Nomination list cleared.")
    await ctx.send(embed=embed)
    cur_nom.clear()


@clear_nominations.error
async def clear_nominations_error(ctx, error):
    embed = discord.Embed(title="Nominations list was already empty.",
                          color=0xff0000)
    print(error)
    await ctx.send(embed=embed)


@bot.command()
async def nominations(ctx):
    if not cur_nom:
        embed = discord.Embed(title="There are no current nominations.")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Current Nominations")
        keys = list(cur_nom.keys())
        numberOfNominees = len(keys)
        for x in range(numberOfNominees):
            embed.add_field(name=str(x), value=keys[x], inline=True)
        await ctx.send(embed=embed)
        print(cur_nom.items())


@bot.command()
async def vote(ctx):
    await tournament(ctx)


async def tournament(ctx):
    # Check to see if there are any nominations.
    if not cur_nom:
        embed = discord.Embed(title="Error",
                              description="The nominations list is empty.",
                              color=0xff0000)
        await ctx.send(embed=embed)
        return  # if there are none then erorr and return.
    numberofcontestants = len(cur_nom)
    embed = discord.Embed(title="Starting Vote",
                          description="Select the reaction associated with each contestant to vote.")
    noms = list(cur_nom.keys())  # Turn dictionary of keys into list to be able to iterate through.
    for x in range(numberofcontestants):
        embed.add_field(name=str(x), value=noms[x])
    await ctx.send(embed=embed)
    if numberofcontestants % 2 == 0:
        numberofcontestants = len(cur_nom)
        numberofrounds = numberofcontestants // 2
        embed = discord.Embed(title="Number of rounds: " + str(numberofrounds),
                              description="No one is seeded.")
        await ctx.send(embed=embed)
        for x in range(numberofrounds):
            print(cur_nom.items())
            aOne = random.choice(list(cur_nom.keys()))
            a = aOne
            a_Image = cur_nom[a]
            del cur_nom[a]
            bOne = random.choice(list(cur_nom.keys()))
            b = bOne
            b_Image = cur_nom[b]
            del cur_nom[b]
            embed = discord.Embed(title="Contestant One", description=a)
            embed.set_thumbnail(url=a_Image)
            await ctx.send(embed=embed)
            embed = discord.Embed(title="Contestant Two", description=b)
            embed.set_thumbnail(url=b_Image)
            await ctx.send(embed=embed)
            embed = discord.Embed(title="Vote!", description="Vote by clicking the corresponding reaction.")
            embed.add_field(name="Contestant One", value=a, inline=True)
            embed.add_field(name="Contestant Two", value=b, inline=True)
            message = await ctx.send(embed=embed)
            await message.add_reaction(emoji1)
            await message.add_reaction(emoji2)
            await asyncio.sleep(roundTime)
            cache_msg = discord.utils.get(bot.cached_messages, id=message.id)
            tally = []
            for item in cache_msg.reactions:
                tally.append(item.count)
            if tally[0] > tally[1]:
                embed = discord.Embed(title="Winner", description=a, color=0x00ff00)
                embed.set_thumbnail(url=a_Image)
                await ctx.send(embed=embed)
                cur_nom[a] = a_Image
            elif tally[0] < tally[1]:
                embed = discord.Embed(title="Winner", description=b, color=0x00ff00)
                embed.set_thumbnail(url=b_Image)
                await ctx.send(embed=embed)
                cur_nom[b] = b_Image
            else:
                embed = discord.Embed(title="Tie", description="Both contestants have been re-added to the voting pool",
                                      color=0xff0000)
                await ctx.send(embed=embed)
                cur_nom[a] = a_Image
                cur_nom[b] = b_Image
    else:  # Number of contestants is odd. Time to seed a contestant.
        choice = random.choice(list(cur_nom.keys()))
        seededContestant = choice
        seededContestantImage = cur_nom[seededContestant]
        del cur_nom[seededContestant]
        numberofcontestants = len(list(cur_nom.keys()))
        numberofrounds = numberofcontestants // 2
        embed = discord.Embed(title="Number of rounds: " + str(numberofrounds),
                              description=seededContestant + " is Seeded.")
        embed.set_thumbnail(url=seededContestantImage)
        await ctx.send(embed=embed)
        for x in range(numberofrounds):
            print(cur_nom.items())
            aOne = random.choice(list(cur_nom.keys()))
            a = aOne
            a_Image = cur_nom[a]
            del cur_nom[a]
            bOne = random.choice(list(cur_nom.keys()))
            b = bOne
            b_Image = cur_nom[b]
            del cur_nom[b]
            embed = discord.Embed(title="Contestant One", description=a)
            embed.set_thumbnail(url=a_Image)
            await ctx.send(embed=embed)
            embed = discord.Embed(title="Contestant Two", description=b)
            embed.set_thumbnail(url=b_Image)
            await ctx.send(embed=embed)
            embed = discord.Embed(title="Vote!", description="Vote by clicking the corresponding reaction.")
            embed.add_field(name="Contestant One", value=a, inline=True)
            embed.add_field(name="Contestant Two", value=b, inline=True)
            message = await ctx.send(embed=embed)
            await message.add_reaction(emoji1)
            await message.add_reaction(emoji2)
            await asyncio.sleep(roundTime)
            cache_msg = discord.utils.get(bot.cached_messages, id=message.id)
            tally = []
            for item in cache_msg.reactions:
                tally.append(item.count)
            if tally[0] > tally[1]:
                embed = discord.Embed(title="Winner", description=a, color=0x00ff00)
                embed.set_thumbnail(url=a_Image)
                await ctx.send(embed=embed)
                cur_nom[a] = a_Image
            elif tally[0] < tally[1]:
                embed = discord.Embed(title="Winner", description=b, color=0x00ff00)
                embed.set_thumbnail(url=b_Image)
                await ctx.send(embed=embed)
                cur_nom[b] = b_Image
            else:
                embed = discord.Embed(title="Tie", description="Both Contestants have been re-added to the voting pool",
                                      color=0xff0000)
                await ctx.send(embed=embed)
                cur_nom[a] = a_Image
                cur_nom[b] = b_Image
        if seededContestant in cur_nom.keys():
            return
        else:
            cur_nom[seededContestant] = seededContestantImage


bot.run("")
