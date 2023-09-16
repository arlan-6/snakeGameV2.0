import pygame
from board import Board
from snake import SnakePlayer
from apple import Apple
from snakes import SnakeSnake
# from apples import Apples

pygame.font.init()

control = [pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT]
control2 = [pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a]
control3 = [pygame.K_i,pygame.K_k,pygame.K_l,pygame.K_j]

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)
LIGHT_GRAY = (192, 192, 192)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BROWN = (165, 42, 42)
TURQUOISE = (64, 224, 208)
GOLD = (255, 215, 0)
NAVY_BLUE = (0, 0, 128)
OLIVE_GREEN = (128, 128, 0)
SKY_BLUE = (135, 206, 235)
SALMON = (250, 128, 114)

Font=pygame.font.SysFont('arial', 30)

class SnakeGame:

    def __init__(self):

        self.WIDTH, self.HIGH = 600, 600
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HIGH))

        self.FPS = 10

        self.run = True

        self.boar = Board(41)
        self.board = self.boar.rtrboard()

        self.apple = Apple()

        # self.apples = []
        # self.apple_count = 3
        #
        # for i in range(self.apple_count):
        #     a = Apple()
        #     self.apples.append(a)
        #
        # self.apple = Apples(self.apples)

        self.snake = [
                      SnakePlayer(*control, GREEN,GOLD, 'arlan'),
                      # SnakePlayer(*control2, CYAN,SALMON, 'adiya'),
                      # SnakePlayer(*control, , 'name'),
                      ]

        self.snakes = SnakeSnake(len(self.snake),self.snake)


    def play(self):

        clock = pygame.time.Clock()

        self.board = self.apple.place(self.board)

        self.board = self.snakes.placeSnakes(self.board)

        while self.run:

            clock.tick(self.FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.run = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_g:

                        self.board = self.boar.rtrboard()
                        self.snakes.reset()
                        self.play()

                    self.snakes.keyDown(event.key)

            self.draw_window()

        pygame.quit()


    def draw_window(self):

        self.board = self.apple.checkApple(self.board)

        self.snake_move()

        self.draw_board()

        pygame.display.update()


    def draw_board(self):

        back_color = GRAY
        step = self.WIDTH/self.boar.widh
        height = 0

        for i in self.board:

            width = 0

            for j in i:

                color = self.snakes.color(back_color,j,self.apple.corrent_color)

                rect = pygame.Rect(width, height, width + step, height + step)
                pygame.draw.rect(self.WIN, color, rect)

                width += step

            height += step


    def snake_move(self):

        self.board = self.snakes.snakesMove(self.board, self.apple)

        self.snakes.movingGeneral(self.board)

        self.snakes.checkCollision()


g = SnakeGame()
g.play()