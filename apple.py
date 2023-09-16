import random

class Apple:
    def __init__(self):
        self.apples = [
            [(255, 0, 0),1],
            [(255, 255, 0),2],
            [(255, 165, 0),2],
            [(128, 0, 128),5],
        ]
        self.utility = self.apples[0][1]

        self.corrent_color = self.apples[0][0]
        self.apple_pos_y = 0
        self.apple_pos_x = 0

    def place(self,board):

        self.choiceApple()
        a = True

        while a:

            self.apple_pos_y = random.randrange(0, 20)
            self.apple_pos_x = random.randrange(0, 20)

            if board[self.apple_pos_y][self.apple_pos_x] == None:

                break

        board[self.apple_pos_y][self.apple_pos_x] = 'apple'

        return  board

    def checkApple(self,board):
        for i in board:
            if 'apple' in i:
                return board
        board1 =  self.place(board)
        return board1

    def choiceApple(self):
        a = random.choice(self.apples)
        self.corrent_color = a[0]
        self.utility = a[1]
