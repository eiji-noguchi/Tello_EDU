import json
commands = json.load(open('C:\Drone\Tello_EDU\TelloEDU\module\commands.json'))

def getCommand(getch):
    key = chr(ord(getch))
    if key in commands.keys():
        # コマンドが設定されている場合
        return commands[key]
    else:
        # コマンドが設定されていない場合、入力されてたものをそのまま返す
        return key

