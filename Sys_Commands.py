import discord
import random
from discord.ext import commands


class Sys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def logout(self, ctx):
        client = self.client

        await ctx.send(f'{client.user.name} is leaving Discord!')
        await client.change_presence(status=discord.Status.offline)
        await client.close()

    @commands.command()
    async def purge(self, ctx, limit: int):
        if limit < 0:
            await ctx.send(f'Không thể nhập số âm {limit}!')
        else:
            await ctx.message.delete()
            await ctx.channel.purge(limit=limit)

            mess = await ctx.send(f'` {ctx.author.name} ` đã dùng lệnh để xóa {limit} tin nhắn.')
            await mess.delete(delay=2)

    @commands.command()
    async def bans(self, ctx):
        usrs = await ctx.guild.bans()
        if not usrs:
            await ctx.send('Chưa có ai bị ban cả.')
        else:
            lst = '\n'.join([f'   - Tên:  `{str(usr.user)}`\n   - Lý do ban:  `{str(usr.reason)}`' for usr in usrs])
            await ctx.send(f'Danh sách các users bị ban:\n{lst}')

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, mem: discord.Member = None, *, reason='thích vậy á chịu hong =]'):
        if mem is None:
            await ctx.send('Vui lòng nhập tên người muốn ban.')
        elif mem == ctx.author:
            await ctx.send('Bạn có thể sử dụng lệnh .kickme để tự out sever.')
        else:
            await ctx.guild.ban(user=mem, reason=reason)
            await ctx.send(content=f'{mem.name} đã bị ban khỏi sever vì {"".join(list(reason))}.')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def uban(self, ctx, *, mem=None):
        tmp = None
        if mem is None:
            await ctx.send('Vui lòng nhập tên người muốn unban.')
        else:
            usrs = await ctx.guild.bans()
            for usr in usrs:
                if mem == str(usr.user):
                    tmp = True
                    await ctx.guild.unban(user=usr.user)
                    await ctx.send(content=f'Gỡ ban {mem} thành công.')
                    break
                else:
                    tmp = False
        if tmp is False:
            await ctx.send(f'Đã ban {mem} đâu mà gỡ.')

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, mem: discord.Member = None, *, reason='thích vậy á chịu hong =]'):
        if mem is None:
            await ctx.send('Vui lòng nhập tên người muốn kick.')
        elif mem == ctx.author:
            await ctx.send('Bạn có thể sử dụng lệnh .kickme để tự out sever.')
        else:
            await mem.kick(reason=reason)
            await ctx.send(content=f'{mem.name} đã bị kick khỏi sever vì {"".join(list(reason))}.')

    # @commands.command()
    # async def mute(self, ctx, mem: discord.Member = None, time):

    # 	await ctx.send(f'{mem.name} đã bị khóa mõm trong vòng {time}.')

    @commands.command()
    async def info(self, ctx, mem: discord.Member = None):
        if mem is None:
            mem = ctx.author

        colors = [
            [148, 0, 211], [75, 0, 130],
            [0, 0, 255], [0, 255, 0],
            [255, 255, 0], [255, 127, 0], [255, 0, 0]
        ]
        rdColor = colors[random.randint(0, len(colors))]
        icon_url = "https://i.ibb.co/GPncKM2/IMG_20210223_134209_439.jpg"
        img_url = "https://i.ibb.co/JmycZFd/now.gif"
        thumbnail_url = mem.avatar_url

        if mem.status == discord.Status.online:
            stt = 'Đang online.'
        elif mem.status == discord.Status.offline:
            stt = 'Đang offline.'
        elif mem.status == discord.Status.dns:
            stt = 'Đừng làm phiền.'
        elif mem.status == discord.Status.idle:
            stt = 'Đang đợi crush tỏ tình.'
        elif mem.status == discord.Status.streaming:
            stt = 'Đang xem pỏn.'
        elif mem.status == discord.Status.invisible:
            stt = 'Đang ẩn thân.'
        else:
            stt = f'Đang {mem.status}'

        description = """
Trạng thái: {}
-------------------------------------------------------
""".format(stt)
        emb = discord.Embed(
            title=f"__{mem.name}__",
            description=description,
            color=discord.Color.from_rgb(rdColor[0], rdColor[1], rdColor[2])
        )
        emb.set_image(url=img_url)
        emb.set_footer(text=f"Copyrights by Phong Jocker\nCreated by {ctx.author}", icon_url=icon_url)
        emb.set_thumbnail(url=thumbnail_url)

        emb.add_field(name='【 Biệt danh 】', value=f'ㅤ∟ `{mem.display_name}`')
        emb.add_field(name='【 Tag 】', value=f'ㅤ∟ `{mem.discriminator}`')
        emb.add_field(name='【 Thiết bị 】', value=f'ㅤ∟ `{"Mobile" if mem.is_on_mobile() else "Pc"}`')
        emb.add_field(name='【 Robot 】', value=f'ㅤ∟ `{"Bot" if mem.bot else "Người"}`')
        emb.add_field(name='【 Nitro 】', value=f'ㅤ∟ `{"Không" if mem.premium_since is None else "Có"}`')
        emb.add_field(name='【 Avatar 】', value=f'ㅤ∟〚 __[Link]({mem.avatar_url})__ 〛')
        emb.add_field(name='【 ID 】', value=f'ㅤ∟〚` {mem.id} `〛', inline=False)
        emb.add_field(name='【 Vai trò 】', value=' | '.join([role.mention for role in mem.roles]), inline=False)
        emb.add_field(name='【 Quyền hạn 】', value='```{}```'.format(' | '.join([''.join(per[0]) for per in mem.guild_permissions if per[1]])), inline=False)
        emb.add_field(name='【 Tạo tài khoản 】', value=f"ㅤ∟  `{mem.created_at.strftime('%d-%m-%Y %H:%M')}`", inline=False)
        emb.add_field(name=f'【 Tham gia sever〚**`{mem.guild}`**〛】', value=f"ㅤ∟  `{mem.joined_at.strftime('%d-%m-%Y %H:%M')}`", inline=False)
        await ctx.send(embed=emb)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Nhập thiếu số lượng!')


def setup(client):
    client.add_cog(Sys(client))
