import random

class SnakePlayer:
    def __init__(self,up,down,right,left,color,color2,name):
        self.SNAKE_LEN = 1
        self.move_side = 'start'
        self.pos_y = random.randrange(0, 20)
        self.pos_x = random.randrange(0, 20)
        self.snake_pos = [[self.pos_y, self.pos_x]]
        self.loosed = False
        self.color = color
        self.color2 = color2
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.name = name

    def moving(self,board):

        if self.SNAKE_LEN < len(self.snake_pos) + 1:
            board[self.snake_pos[-1][0]][self.snake_pos[-1][1]] = None
            self.snake_pos.pop(-1)

        if self.move_side == 'start':
            self.snake_pos = self.snake_pos[::-1]
            self.snake_pos.append([self.pos_y, self.pos_x])
            self.snake_pos = self.snake_pos[::-1]

        return board

    def eat(self,apple_pos,utility):
        apple_pos_x,apple_pos_y = apple_pos
        if [apple_pos_x, apple_pos_y] == [self.pos_x, self.pos_y]:
            self.SNAKE_LEN += utility
            return True
        return False

    def place(self,board):
        a = True
        while a:
            self.pos_y = random.randrange(0, 20)
            self.pos_x = random.randrange(0, 20)
            if board[self.pos_y][self.pos_x] == None:
                break
        board[self.pos_y][self.pos_x] = self.name
        return  board

    def snake_draw(self,board):

        print(self.name,self.SNAKE_LEN)
        if not self.loosed:
            for i in self.snake_pos:
                board[i[0]][i[1]] = self.name
        return board

    def checkLose(self):
        self.died()
        return [self.pos_y, self.pos_x] in self.snake_pos and self.SNAKE_LEN > 4

    def died(self):
        if self.loosed:
            self.SNAKE_LEN = 0
            self.snake_pos = [[-1,-1]]
            self.pos_y = -1
            self.pos_x = -1
            self.move_side = ''

    def reset(self):
        self.SNAKE_LEN = 1
        self.move_side = 'start'
        self.pos_y = random.randrange(0, 20)
        self.pos_x = random.randrange(0, 20)
        self.snake_pos = [[self.pos_y, self.pos_x]]
        self.loosed = False