"""
print("hello")
st = "hello"
data = b"hello"
print(type(st))
print(st)
print(type(data))
print(data)
print(type(data.decode()))
print(data.decode())
inp = input()
print(type(inp))
print(type(inp.encode()))
"""


from msvcrt import getch
msg = chr(ord(getch()))
print(msg)

"""
def f(x=2):
    return x ** x

print(f())
print(f(4))
"""