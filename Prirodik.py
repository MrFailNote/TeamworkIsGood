import discord, os, requests
import random as r
from discord.ext import commands

from Gen_logic import *
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def decay(ctx):
    item = r.randint(1,9)
    if item == 1:
        with open(f'EnviPics/1.jpeg', 'rb') as f:
            picture = discord.File(f)
        infotext = '''Электрические батарейки:
    Разлагаются в течении: около 200 лет
    Вред для природы: тяжёлые металлы в батарейках крайне ядовиты для почвы и не только!'''
    elif item == 2:
        with open(f'EnviPics/2.jpg', 'rb') as f:
            picture = discord.File(f)
        infotext = '''Жевательная резинка:
    Разлагается в течении: до 30 лет
    Вред для природы: может вредить жизни многих животных, преимущественно мелких'''
    elif item == 3:
        with open(f'EnviPics/3.jpg', 'rb') as f:
            picture = discord.File(f)
        infotext = '''Фольга:
    Разлагается в течении: в среднем до 100 лет
    Вред для природы: почти минимален'''
    elif item == 4:
        with open(f'EnviPics/4.jpg', 'rb') as f:
            picture = discord.File(f)
        infotext = '''Книги:
    Разлагаются в течении: 1 - 3 месяцев
    Вред для природы: сами по себе безопасны, однако краска может быть токсична'''
    elif item == 5:
        with open(f'EnviPics/5.jpg', 'rb') as f:
            picture = discord.File(f)
        infotext = '''Газеты:
    Разлагаются в течении: порядка 1 - 3 месяцев 
    Вред для природы: Краска содержитв себе токсичные материалы'''
    elif item == 6:
        with open(f'EnviPics/6.jpg', 'rb') as f:
            picture = discord.File(f)
        infotext = '''Рыболовная леска:
    Разлагается в течении: около 600 лет
    Вред для природы: содержит ядовитые вещества, может вредить животным.'''
    elif item == 7:
        with open(f'EnviPics/7.jpg', 'rb') as f:
            picture = discord.File(f)
        infotext = '''Стекло:
    Разлагается в течении: Более 1000 лет 
    Вред для природы: Почти не разлагаясь могут ранить животных и человека'''
    elif item == 8:
        with open(f'EnviPics/8.jpg', 'rb') as f:
            picture = discord.File(f)
        infotext = '''Огрызки фруктов:
    Разлагаются в течении: до 2 месяцев
    Вред для природы: нет, могут работать как естественный компост'''
    elif item == 9:
        with open(f'EnviPics/9.png', 'rb') as f:
            picture = discord.File(f)
        infotext = '''Туалетная бумага:
    Разлагается в течении: 2 - 4 дней 
    Вред для природы: нет'''
        
    await ctx.send(infotext)
    await ctx.send(file=picture)
    
bot.run("vstavish")
