import json
commands = json.load(open('C:\Drone\Tello_EDU\TelloEDU\module\commands.json'))

def getCommand(getch):
    key = chr(ord(getch))
    if key in commands.keys():
        return commands[key]
    else:
        return key

