import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy {bot.user} y me encuentro diseñado para ayudarte a conocer que objetos puedes reciclar y cuales desechar!')


reciclables = ["botella", "lata", "papel", "cartón", "vidrio", "tetrabrik", "revista", "hoja", "envase", "bolsa", "periódico", "lata atún", "botella vidrio", "caja", "folder", "lata cerveza", "tubo cartón", "tapita", "frasco", "envoltura papel"]
basura = ["pañal", "colilla", "papel higiénico", "cáscara", "bolsa", "chicle", "servilleta", "vaso plástico", "sorbete", "toallita", "pañuelo", "cuchara plástica", "bombilla", "esponja", "cepillo viejo", "plato plastico", "pañal húmedo", "cinta adhesiva", "hisopo"]


@bot.command()
async def clasificar(ctx, palabra: str):
    palabra = palabra.lower()
    for x in reciclables:
        if x == palabra:
            await ctx.send('✅ se puede reciclar.')
            return
    for x in basura:
        if x == palabra:
            await ctx.send('❌ debe ir a la basura.')
            return
    await ctx.send('🤔 No estoy seguro. Consulta con tu centro de reciclaje local.')
    
bot.run('introduce tu token aqui!')
