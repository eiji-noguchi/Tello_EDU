import json
commands = json.load(open('pyCode\module\commands.json'))

def getCommand(getch):
    key = chr(ord(getch))
    if key == "c":
        return input("コマンドを入力してね( *´艸｀)\r\n")
    elif key in commands.keys():
        return commands[key]
    else:
        return key

