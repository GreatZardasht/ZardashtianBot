import discord
import random
import os
import asyncio
from discord.ext import commands
import aiohttp
import box
from .utils.utils import Utils

client = commands.Bot(command_prefix='Z-')


@client.event
async def on_ready():
    print("On: True, Off: False")


@client.event
async def on_member_join(member, ctx):
    await ctx.say(f'Welcome {member} to our server! Have fun!')


@client.event
async def on_member_remove(member, ctx):
    await ctx.say(f'{member} had just left our server. Bye Bye {member}.')


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong!, {round(client.latency * 1000)}ms")


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt",
                 "Yes, definitely.",
                 "You may reply on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 'Cannot predict now.',
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]

    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    try:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Message(s) Deleted!')
    except:
        await ctx.send("You don't have permission.")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    try:
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member}. Reason: {reason}")
    except:
        await ctx.send(f"You don't have permission.")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member}. Reason: {reason}")
    except:
        await ctx.send(f"You don't have permission.")


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    try:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
    except:
        await ctx.send(f"Couldn't ban {user.mention}. Reason : You don't have permission. / This user isn't banned.")

@client.command()
async def information(ctx):
    await ctx.send('**This shows you the information of the bot not the owner.**\nOwner: Zardasht HQ\nFriend: Buckled Flea\nIDE: Python-3.6.8\nVersion: Big Chungus\nSo get the hell away.')

# Nsfw Stuff Beware!! #

    async def req(self, url):
        res = await self.bot.session.get(f"https://nekos.life/api/v2/img/{url}")
        res = await res.json()
        return box.Box(res)

    async def handle_not_upvoted(self, ctx):
        em = discord.Embed(color=0xfc281d, title="It's No Nut November!")
        em.description = """
Hey! That means no nutting. Get some self control of yourself.

If you seriously can't, I'll do you a favor and run this command **after you upvote me on Discord Bot List.** 

It ain't hard, I got the link right here!

https://discordbots.org/bot/388476336777461770/vote

All you gotta do is hit that giant **VOTE** button!

(If you are seeing this message after upvoting, DBL's API is a bit slow, so you will have to wait around 5-10 minutes before retrying this command.)
"""
        await ctx.send(embed=em)

    # async def __local_check(self, ctx):
    #     if not ctx.channel.nsfw:
    #         await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")
    #     return ctx.channel.nsfw

    @client.command()
    async def feet(self, ctx, is_gif=None):
        """WARNING: NSFW command. Gets a random picture of feet."""
        if not ctx.channel.nsfw:
            return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")

        res = await self.req("feetg")
        em = discord.Embed(color=0xf9e236, title="Feet :eggplant:")
        em.set_image(url=res.url)
        em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by nekos.life", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)


    @client.command()
    async def hentai(self, ctx, is_gif=None):
        """WARNING: NSFW command. Gets a hentai picture."""
        if not ctx.channel.nsfw:
            return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")

        res = await self.req("Random_hentai_gif")
        em = discord.Embed(color=0xf9e236, title="Hentai :eggplant: ")
        em.set_image(url=res.url)
        em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by nekos.life", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)


    @client.command()
    async def boobs(self, ctx):
        """WARNING: NSFW command. Gets pictures of boobs."""
        if not ctx.channel.nsfw:
            return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")
        if not ctx.channel.nsfw:
            return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")

        res = await self.req("boobs")
        em = discord.Embed(color=0xf9e236, title="Boobs :eggplant: ")
        em.set_image(url=res.url)
        em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by nekos.life", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @client.command()
    async def lewdneko(self, ctx):
        """WARNING: NSFW command. Gets a picture of a lewd neko."""
        if not ctx.channel.nsfw:
            return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")

        res = await self.req("nsfw_neko_gif")
        em = discord.Embed(color=0xf9e236, title="Lewd Neko :eggplant: ")
        em.set_image(url=res.url)
        em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by nekos.life", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @client.command(aliases=['nsfwpfp'])
    async def nsfwavatar(self, ctx):
        """WARNING: NSFW command. Gets you a lewd profile picture."""
        if not ctx.channel.nsfw:
            return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")

        res = await self.req("nsfw_avatar")
        em = discord.Embed(color=0xf9e236, title="Lewd Profile Picture :eggplant: ")
        em.set_image(url=res.url)
        em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by nekos.life", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @client.command()
    async def lesbian(self, ctx):
        """WARNING: NSFW command. Gets you a lesbian pic."""
        if not ctx.channel.nsfw:
            return await ctx.send("Are you trying to **kill innocent people's eyes**?? I think not!")

        res = await self.req("les")
        em = discord.Embed(color=0xf9e236, title="Lesbian :eggplant: ")
        em.set_image(url=res.url)
        em.set_footer(text=f"Requested by: {str(ctx.author)} | Powered by nekos.life", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=em)

client.run(str(os.environ.get('BOT_TOKEN')))
