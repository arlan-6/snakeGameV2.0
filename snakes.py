import random
class SnakeSnake():
    def __init__(self,count,snakes):
        self.count = count
        assert isinstance(snakes, list)
        self.snakes = snakes
        self.snake = self.snakes[0]
        if self.count >= 2:
            self.snake1 = self.snakes[1]
        if self.count >= 3:
            self.snake2 = self.snakes[2]

    def movingGeneral(self,board):

        for i in range(self.count):

            if self.snakes[i].SNAKE_LEN < len(self.snakes[i].snake_pos) + 1:
                board[self.snakes[i].snake_pos[-1][0]][self.snakes[i].snake_pos[-1][1]] = None
                self.snakes[i].snake_pos.pop(-1)

            self.snakes[i].snake_pos = self.snakes[i].snake_pos[::-1]
            self.snakes[i].snake_pos.append([self.snakes[i].pos_y, self.snakes[i].pos_x])
            self.snakes[i].snake_pos = self.snakes[i].snake_pos[::-1]

        return board

    def checkCollision(self):
        if self.count >= 2:

            if [self.snake.pos_y,self.snake.pos_x] in self.snake1.snake_pos:
                self.snake.loosed = True

            if [self.snake1.pos_y,self.snake1.pos_x] in self.snake.snake_pos:
                self.snake1.loosed = True
        if self.count >= 3:

            if [self.snake.pos_y,self.snake.pos_x] in self.snake2.snake_pos:
                self.snake.loosed = True

            if [self.snake1.pos_y,self.snake1.pos_x] in self.snake2.snake_pos:
                self.snake1.loosed = True

            if [self.snake2.pos_y,self.snake2.pos_x] in self.snake1.snake_pos:
                self.snake2.loosed = True

            if [self.snake2.pos_y,self.snake2.pos_x] in self.snake.snake_pos:
                self.snake2.loosed = True

    def keyDown(self,key):

        for i in range(self.count):

            if key == self.snakes[i].up and self.snakes[i].move_side != 'down':
                self.snakes[i].move_side = 'up'
            elif key == self.snakes[i].down and self.snakes[i].move_side != 'up':
                self.snakes[i].move_side = 'down'
            elif key == self.snakes[i].left and self.snakes[i].move_side != 'right':
                self.snakes[i].move_side = 'left'
            elif key == self.snakes[i].right and self.snakes[i].move_side != 'left':
                self.snakes[i].move_side = 'right'

    def snakesMove(self,board,apple):

        board1 = ''
        maxY = 40
        maxX = 39

        for i in range(self.count):

            if self.snakes[i].move_side == 'start':
                board[self.snakes[i].pos_y][self.snakes[i].pos_x] = None

            if self.snakes[i].move_side == 'up' and not self.snakes[i].pos_y == -1:
                self.snakes[i].pos_y = maxY if self.snakes[i].pos_y == 0 else self.snakes[i].pos_y
                self.snakes[i].pos_y -= 1

            elif self.snakes[i].move_side == 'down' and not self.snakes[i].pos_y == -1:
                self.snakes[i].pos_y = -1 if self.snakes[i].pos_y == maxX else self.snakes[i].pos_y
                self.snakes[i].pos_y += 1

            elif self.snakes[i].move_side == 'left' and not self.snakes[i].pos_y == -1:
                self.snakes[i].pos_x = maxY if self.snakes[i].pos_x == 0 else self.snakes[i].pos_x
                self.snakes[i].pos_x -= 1

            elif self.snakes[i].move_side == 'right' and not self.snakes[i].pos_y == -1:
                self.snakes[i].pos_x = -1 if self.snakes[i].pos_x == maxX + 1 else self.snakes[i].pos_x
                self.snakes[i].pos_x += 1

            board[self.snakes[i].pos_y][self.snakes[i].pos_x] = self.snakes[i].name

            if self.snakes[i].checkLose():
                self.snakes[i].loosed = True

            if self.snakes[i].eat([apple.apple_pos_x, apple.apple_pos_y, ],apple.utility):
                apple.place(board)

            board1 = self.snakes[i].snake_draw(board)

        return  board1

    def color(self,back_color, j,apple_color):
        color = back_color
        for i in range(self.count):
            if j == self.snakes[i].name:
                if i == 0:
                    color = self.snakes[i].color2
                else:
                    color = self.snakes[i].color

        if j == 'apple':
            color = apple_color
        return  color

    def placeSnakes(self,board):
        board1 = board
        for i in range(self.count):
            board1 = self.snakes[i].place(board1)
        return board1

    def reset(self):
        for i in range(self.count):
            self.snakes[i].reset()