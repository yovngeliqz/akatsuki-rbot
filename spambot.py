import discord
from discord.ext import commands 
import asyncio 
import os 
 
intents = discord.Intents.default() 
intents.message_content = True 
bot = commands.Bot(command_prefix=None, intents=intents) 

class SpamView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="CLICK", style=discord.ButtonStyle.secondary)
    async def spam_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        message = (
            "# ৭৭৭৭৭৭৭৭ ๒๒๒๒๒๒๒๒ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭৭৭৭৭৭৭ ๒๒๒๒๒๒๒๒ ৭৭۷۷۷۷৭৭\n"
            "# ৭৭৭৭৭৭৭৭ ๒๒๒๒๒๒๒๒ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭৭৭৭৭৭৭ ๒๒๒๒๒๒๒๒ ৭৭۷۷۷۷৭৭\n"
            "# ৭৭৭৭৭৭৭৭ ๒๒๒๒๒๒๒๒ ৭৭۷۷۷۷৭৭\n"
            "# ৭৭৭৭৭৭৭৭ ๒๒๒๒๒๒๒๒ ৭৭۷۷۷۷৭৭\n"
            "# ৭৭৭৭৭৭৭৭ ๒๒๒๒๒๒๒๒ ৭৭۷۷۷۷৭৭\n"
            "# ৭৭৭৭৭৭৭৭ ๒๒๒๒๒๒๒๒ ৭৭۷۷۷۷৭৭\n"
            "# ৭৭৭৭৭৭৭৭ ๒๒๒๒๒۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒๒๒๒۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷৭৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷৭৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷۷৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷۷۷\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒๒۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷۷৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷۷৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷৭৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷۷৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭۷৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷৭৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# ৭৭۷۷۷۷৭৭ ๒۲۲۲۲۲۲۲ ৭৭۷۷۷۷۷৭\n"
            "# SERVIDOR RAIDADO PELA AKATSUKI BOLADONA KKKKKKKKKK JA PODE DELETAR ESSA ABERRAÇÃO DE SERVIDOR!\n"
            "# @everyone @everyone @everyone\n"
            "https://discord.gg/CpvaQuncv4"
        )
        await interaction.response.send_message(message)

@bot.event 
async def on_ready(): 
    print(f'~ $ CREDITOS A PANSI @yovngeliqz') 
    
    try: 
        synced = await bot.tree.sync() 
        print(f"synchronised slash commands: {len(synced)}") 
    except Exception as e: 
        print(f"error: {e}") 
     
     
@bot.tree.command(name='spam', description=' Envia a mensagem de spam con botão de disparo.') 
async def spam(interaction: discord.Interaction): 
    embed = discord.Embed(
        title="PANSI MOGGED YOU",
        description="```🤣 Clique no botão abaixo para começar.```",
        color=0x8B0000
    )
    view = SpamView()
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True) 
 
bot.run("")
