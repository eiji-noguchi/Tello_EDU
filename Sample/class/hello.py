print("最初のhello")

#このファイルから実行されているかの判断
if __name__ == "__main__":
    print("次のhello")

def aisatsu(h):
    print("引数の"+h)
    print("最後のhello")

def test(a, b):
    sum = a + b
    sub = a - b
    return sum,sub

