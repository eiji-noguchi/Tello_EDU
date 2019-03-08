'''未使用
from msvcrt import getch

def getCommand(getch):
    key = chr(ord(getch))
    if key == "\r":
        return "takeoff"
    elif key == " ":
        return "land"
    elif key == "q":
        return "up 20"
    elif key == "e":
        return "down 20"
    elif key == "w":
        return "forward 20"
    elif key == "a":
        return "left 20"
    elif key == "s":
        return "back 20"
    elif key == "d":
        return "right 20"
    elif key == "b":
        return "battery?"
    elif key == "c":
        return input("コマンドを入力してね( *´艸｀)\r\n")
    else:
        return key
'''