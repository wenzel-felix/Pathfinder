from Node import Node
import pygame
import colors
from additional_windows import Collector
import time


class Board:
    board_x_size = 0
    board_y_size = 0

    def __init__(self, x_size=80, y_size=60):
        if x_size > 80:
            x_size = 80
        elif x_size < 10:
            x_size = 10
        if y_size > 60:
            y_size = 60
        elif y_size < 8:
            y_size = 8
        self.board_x_size = x_size
        self.board_y_size = y_size
        self.nodes = [[Node(i, j) for i in range(x_size)]for j in range(y_size)]
        C = Collector()
        self.run_pygame(C.start_x, C.start_y, C.end_x, C.end_y)

    def run_pygame(self, start_x, start_y, end_x, end_y):
        r = 3
        self.nodes[start_y][start_x].start_node = True
        self.nodes[end_y][end_x].end_node = True

        run = True
        self.window = pygame.display.set_mode((self.board_x_size*10, self.board_y_size*10))
        pygame.display.set_caption("Pathfinder")
        while run:

            self.window.fill(colors.background)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if r > 1:
                            r -= 1
                    elif event.button == 5:
                        if r < 10:
                            r += 1
                if pygame.mouse.get_pressed()[0]:
                    try:
                        pos = pygame.mouse.get_pos()
                        for i in range(-r, r+1, 1):
                            for j in range(-r, r+1, 1):
                                if (i*i)+(j*j) < r*r:
                                    try:
                                        if self.nodes[pos[1] // 10+i][pos[0] // 10+j].curr_height < 7:
                                            self.nodes[pos[1] // 10+i][pos[0] // 10+j].curr_height += 1
                                    except IndexError:
                                        pass
                    except AttributeError:
                        pass
                elif pygame.mouse.get_pressed()[1]:
                    try:
                        pos = pygame.mouse.get_pos()
                        for i in range(-r, r+1, 1):
                            for j in range(-r, r+1, 1):
                                if (i*i)+(j*j) < r*r:
                                    try:
                                        self.nodes[pos[1] // 10+i][pos[0] // 10+j].is_wall = True
                                    except IndexError:
                                        pass
                    except AttributeError:
                        pass
                elif pygame.mouse.get_pressed()[2]:
                    try:
                        pos = pygame.mouse.get_pos()
                        for i in range(-r, r+1, 1):
                            for j in range(-r, r+1, 1):
                                if (i*i)+(j*j) < r*r:
                                    try:
                                        self.nodes[pos[1] // 10+i][pos[0] // 10+j].is_wall = False
                                        if self.nodes[pos[1] // 10+i][pos[0] // 10+j].curr_height > 1:
                                            self.nodes[pos[1] // 10+i][pos[0] // 10+j].curr_height -= 1
                                    except IndexError:
                                        pass
                    except AttributeError:
                        pass
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.find_best_path(self.nodes[start_y][start_x], self.nodes[end_y][end_x])

            self.draw_rectangles(self.window)

            pygame.display.update()
        pygame.quit()

    def get_neighbours(self, x, y):
        neighbours = []
        if self.nodes[y][x].curr_height == 0:
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if i == 0 or j == 0:
                        if 0 <= i + y < 60 and 0 <= j + x < 80:
                            neighbours.append(self.nodes[y+i][x+j])
        return neighbours

    def draw_rectangles(self, window):
        for row in self.nodes:
            for node in row:
                pygame.draw.rect(window, node.get_color(), (node.x_cord, node.y_cord, node.size, node.size))

    def undo_exhausted(self):
        for row in self.nodes:
            for node in row:
                node.exhausted = False

    def find_best_path(self, start_node, end_node):
        start_node.curr_height = 0
        start_node.step = 0
        run = True
        best_path_steps = []
        neighbour_list = []

        step = 1
        #durch while ersetzen
        while run:

            self.undo_exhausted()

            for y in range(self.board_y_size):
                for x in range(self.board_x_size):
                    if not self.nodes[y][x].step + 8 < step:
                        if not self.nodes[y][x].exhausted:
                            neighbours = self.get_neighbours(x, y)
                            for neighbour in neighbours:
                                if not neighbour.is_wall:
                                    if neighbour.curr_height > 0:
                                        neighbour.curr_height -= 1
                                        neighbour.exhausted = True
                                        neighbour.step = step
                    if self.nodes[y][x] == end_node:
                        neighbours = self.get_neighbours(x, y)
                        for neighbour in neighbours:
                            if self.nodes[y][x].step - 1 == neighbour.step:
                                if neighbour.step not in best_path_steps:
                                    neighbour.best_path = True
                                    best_path_steps.append(neighbour.step)
                    if self.nodes[y][x].best_path:
                        neighbours = self.get_neighbours(x, y)
                        for neighbour in neighbours:
                            neighbour_list.append(neighbour.step)
                            lowest_neighbour_step = min(neighbour_list)
                        for neighbour in neighbours:
                            if neighbour.step not in best_path_steps and neighbour.step == lowest_neighbour_step:
                                neighbour.best_path = True
                                best_path_steps.append(neighbour.step)
                    if start_node.best_path:
                        run = False

            self.draw_rectangles(self.window)
            pygame.display.update()
            step += 1


b = Board()
