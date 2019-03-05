class Test:
    print("class")

    def __init__(self,ini):
        print("init:",ini)
        self.ini = ini
        print("self.m",self.ini)

    def classMethod(self,cla):
        print("method",cla)
        self.hoge = cla
        print("self.hoge",self.hoge)

#test = Test("インスタンスの生成")
#test.classMethod("メソッド呼び出し")
