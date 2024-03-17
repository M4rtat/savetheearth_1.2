import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$',intents=intents)

putin = False

@bot.event
async def on_ready():
    print('we have loged in as bot')
    print('введите команду help для далнейшего использования')
@bot.command()
async def peticya(ctx,daorno:str):
    await ctx.send('мы дожидаемся вашей подписи петиций на экономию мусора нишебродики, согласны?')
    if daorno == 'Да':
        await ctx.send('вы сказали да урааа')
        await ctx.send('КАК СПАСТИ ПРИРОДУ 8 ШАГОВ КОТОРЫЕ МОЖЕТ СДЕЛАТЬ КАЖДЫЙ: https://rusarctica.ru/blog/khoroshee-delo/kak-spasti-prirodu-8-shagov-kotorye-mozhet-sdelat-kazhdyy/ Не все герои носят плащи… но некоторые из них носят с собой термокружки, сдают вторсырье и сокращают используемый пластик. Начните с этих шагов, и природа тоже скажет вам «спасибо»!')
    if daorno == 'Нет':
        await ctx.send('вы сказали нет (')
@bot.command()
async def help(ctx):
  await ctx.send('пока что у меня есть только одна команда:peticya')
@bot.command()
async def help(ctx):
  await ctx.send('пока что я имею в себе
bot.run('токен')
