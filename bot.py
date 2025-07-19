import discord
import random
import time
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
lista_sugerencias = [
    "♻️ Recicla correctamente: separa papel, plástico, vidrio y residuos orgánicos.",
    "🛍️ Usa bolsas reutilizables: evita las bolsas de plástico de un solo uso.",
    "🚶‍♂️🚴‍♀️ Camina, usa bicicleta o transporte público para reducir la contaminación del aire.",
    "🔌 Desconecta aparatos eléctricos que no estés usando para ahorrar energía.",
    "💡 Cambia a focos LED o de bajo consumo.",
    "🚯 No arrojes basura en la calle, ríos o espacios naturales.",
    "🧴 Evita productos con envases excesivos, elige opciones reciclables o a granel.",
    "🧼 Usa productos de limpieza ecológicos, cuida el agua y el suelo.",
    "🌿 Planta árboles o cuida áreas verdes, ayudan a limpiar el aire.",
    "📢 Educa y motiva a otros sobre el cuidado del medio ambiente."
]
lista_retos = ["🌱 Hoy no uses bolsas de plástico. Lleva una bolsa reutilizable.",
    "🚶‍♂️ Usa solo transporte público, bicicleta o camina todo el día.",
    "♻️ Separa toda tu basura y recicla lo que puedas.",
    "💡 Apaga las luces y desconecta aparatos que no estés usando.",
    "🚿 Toma una ducha de máximo 5 minutos para ahorrar agua.",
    "🧴 Evita cualquier producto con envases plásticos descartables.",
    "🌳 Planta una planta o cuida una que ya tengas en casa.",
    "📢 Enseña a otra persona al menos un dato sobre el reciclaje.",
    "🔄 Reutiliza algo en casa que normalmente tirarías.",
    "📷 Sube una foto haciendo algo ecológico y etiqueta a un amigo para que lo haga también.",
    "🧼 Usa productos de limpieza ecológicos o caseros.",
    "❌ No uses papel innecesario hoy. Todo digital.",
    "🥗 Come solo comida hecha en casa y sin empaques procesados.",
    "🗑️ Recoge 3 piezas de basura en la calle o parque y tíralas correctamente.",
    "💧 Usa un solo vaso para beber agua todo el día (sin lavar cada rato)."
]
lista_chistes = [
    "🌳 —¿Por qué el árbol no fue al colegio?\n—Porque ya tenía muchas ramas.",
    "♻️ —¿Qué hace una botella en el gimnasio?\n—¡Reciclaje de peso!",
    "🐢 —¿Qué le dijo una tortuga a otra?\n—¡Vamos rápido, que se viene el calentamiento global!",
    "🌍 —¿Cómo saluda un ecologista?\n—¡Mucho gustóxigeno!",
    "🪴 —¿Qué le dice una planta a otra?\n—¡Qué onda, clorofrenda!",
    "🧴 —¿Por qué el plástico no va a fiestas?\n—Porque siempre termina en el mar.",
    "☀️ —¿Cuál es el colmo de un panel solar?\n—Tener depresión estacional.",
    "🚯 —¿Por qué el basurero rompió con su novia?\n—Porque ya no era reciclable.",
    "🐠 —¿Qué hace un pez en un basurero?\n—¡Buscando su mar-teria prima!",
    "🔥 —¿Por qué el bosque está estresado?\n—¡Porque vive en constante presión de carbono!"
]
@bot.command()
async def clasificar(ctx, palabra: str):
    palabra = palabra.lower()
    for i in reciclables:
        if i == palabra:
            time.sleep(1)
            await ctx.send(' se puede reciclar.')
            return
    for i in basura:
        if i == palabra:
            time.sleep(1)
            await ctx.send(' debe ir a la basura.')
            return
    time.sleep(1)
    await ctx.send(' No estoy seguro. Consulta con tu centro de reciclaje local.')

@bot.command()
async def sugerencias(ctx):
    resultado = random.choice(lista_sugerencias)
    await ctx.send('¡Por supuesto!, te brindare una sugerencia para ser cada dia mas ecoambiental:')
    time.sleep(1)
    await ctx.send(resultado)

@bot.command()
async def retos(ctx):
    reto = random.choice(lista_retos)
    await ctx.send('Con que quieres un reto eh?')
    time.sleep(1)
    await ctx.send('Aqui va tu proximo reto ecologico!')
    time.sleep(1)
    await ctx.send(reto)
@bot.command()
async def info(ctx):
    await ctx.send('¡Hola que tal!, soy un bot diseñado para ayudarte a mejorar en tu ambito ecologico, te ayudare a clasificar objetos, en reciclabes o basura, tambien te dare sugerencias de como mejorar, te propondre algunos retos, que tendras que superar a diario e incluso puedo contarte chistes')

@bot.command()
async def chistes(ctx):
    await ctx.send('Aqui te va un chiste, ¡para relajar el ambiente!')
    time.sleep(1)
    await ctx.send(random.choice(lista_chistes))
    
bot.run('introduce tu token aqui!')
