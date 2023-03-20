import discord
import os
import json
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv
from wakeonlan import send_magic_packet
from ping3 import ping

load_dotenv()
playerUrl = "https://api.clashofclans.com/v1/players/%23"
# getHeader = {"authorization": "Bearer "+os.getenv("TOKEN-COC")}
# clan = "#VYUPLPP8"


# def jugador(idd):
#     responsee = requests.get(playerUrl+idd, headers=getHeader)
#     print(responsee)
#     return responsee.json()

def configCreate(lista1, lista2):
    return {lista1:lista2 for (lista1,lista2) in zip(lista1,lista2)}

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!!', intents=intents)
listaNombres=os.getenv("MACHINENAMES").split(",")
macs=configCreate(os.getenv("MACHINENAMES").split(","),os.getenv("MACS").split(","))
ips=configCreate(os.getenv("MACHINENAMES").split(","),os.getenv("IPS").split(","))

@bot.event
async def on_ready():
    print("Logueado")



# @bot.command()
# async def register(ctx, arg):
#     # intenta cambiar el rol del usuario segun el api de coc
#     naame = ""+arg
#     if naame.startswith("#"):
#         pro = jugador(naame[1:])
#     else:
#         pro = jugador(naame)
#     print("Asignando Usuario")
#     if pro["role"] == "leader":
#         rolee = get(ctx.guild.roles, name="Líder")
#         await ctx.author.add_roles(rolee)
#         await ctx.send(ctx.author.name+" ahora es de rango "+"Líder")


# @bot.command()
# async def player(ctx, arg):
#     print("se esta probando el jugador "+arg)
#     name = ""+arg
#     if name.startswith("#"):
#         pro = jugador(name[1:])
#     else:
#         pro = jugador(name)
#     await ctx.send("Nombre: "+pro["name"]+"\n"+"THlvl: "+str(pro["townHallLevel"])+"\n"+"BHlvl: "+str(pro["builderHallLevel"])+"\n"+"XPlvl: "+str(pro["expLevel"])+"\n")
#     pass


@bot.command()
async def status(ctx, arg):
    print(arg)
    print(ips[arg])
    if ping(ips[arg]) == None:
        await ctx.send(arg+" no esta disponible ⛔⛔⛔")
    elif ping(ips[arg]) == False:
        await ctx.send(arg+" no esta disponible ⛔⛔")
    else:
        await ctx.send(arg+" esta disponible ✅✅")

@bot.command()
async def machineNames(ctx):
    await ctx.send(listaNombres)


#despierta la maquina segun el nombre
@bot.command()
async def wol(ctx, arg):
    print(arg)
    print(macs[arg])
    send_magic_packet(macs[arg])
    await ctx.send("Orden Enviada, recomiendo revisar el status en un par de minutos")
    

bot.run(os.getenv("TOKEN"))