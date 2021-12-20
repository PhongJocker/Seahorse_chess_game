# import discord
import os
import random
from discord.ext import commands

prefix = ['#', '*', '>', '!', '.', '-', '%', 'pj.']  # Tập hợp tất cả dấu nhắc lệnh
client = commands.Bot(command_prefix=prefix)
client.load_extension('Sys_Commands')  # gọi các lệnh từ file Sys_Commands.py
client.load_extension('Features.Games.Seahorse_chess.Seahorse_chess')

colors = [
    [148, 0, 211], [75, 0, 130],
    [0, 0, 255], [0, 255, 0],
    [255, 255, 0], [255, 127, 0], [255, 0, 0]
]
rdColor = colors[random.randint(0, len(colors) - 1)]
icon_url = "https://i.ibb.co/GPncKM2/IMG_20210223_134209_439.jpg"
img_url = "https://i.ibb.co/JmycZFd/now.gif"


@client.event
async def on_ready():
    print(f'{client.user.name} has joined Discord sever!')


@client.command()
@commands.has_permissions(administrator=True)
async def upg(ctx, extension):
    new_dir = extension.replace('/', '.')

    if extension.isnumeric():
        await ctx.send('Tên file không thể là số!')

    elif not os.path.isfile(f'./Features/{extension}.py'):
        await ctx.send('File không tồn tại!')

    else:
        client.load_extension(f'Features.{new_dir}')
        await ctx.send('Success!')


@client.command()
@commands.has_permissions(administrator=True)
async def deg(ctx, extension):
    new_dir = extension.replace('/', '.')

    if extension.isnumeric():
        await ctx.send('Tên file không thể là số!')

    elif not os.path.isfile(f'./Features/{extension}.py'):
        await ctx.send('File không tồn tại!')

    else:
        client.unload_extension(f'Features.{new_dir}')
        await ctx.send('Success!')


@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    new_dir = extension.replace('/', '.')

    if extension.isnumeric():
        await ctx.send('Tên file không thể là số!')

    elif not os.path.isfile(f'./Features/{extension}.py'):
        await ctx.send('File không tồn tại!')

    else:
        client.unload_extension(f'Features.{new_dir}')
        client.load_extension(f'Features.{new_dir}')
        await ctx.send('Success!')


# Xử lí các lỗi khi nhập lệnh
# cú pháp bắt lỗi từng lệnh là <tên lệnh>.error
@upg.error
async def upg_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Nhập thiếu đường dẫn file!")


@deg.error
async def deg_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Nhập thiếu đường dẫn file!")


@reload.error
async def reload_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Nhập thiếu đường dẫn file!")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'Không có lệnh "{ctx.message.content}" !\nDùng !help để xem tất cả lệnh hiện có.')

client.run("token-bot")
