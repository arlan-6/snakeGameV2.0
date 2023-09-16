class Apples:
    def __init__(self,apples):
        self.apples = apples

    def place(self,board):
        b = board
        for i in self.apples:
            b = i.place(b)
        return b

    def checkApple(self,board):
        b = board
        for i in self.apples:
            b = i.checkApple(b)
        return b