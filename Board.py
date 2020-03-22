from Node import Node
import pygame
import colors
from additional_windows import Collector
import copy


class Board:
    board_x_size = 0
    board_y_size = 0

    def __init__(self, x_size=100, y_size=80):
        if x_size > 100:
            x_size = 100
        elif x_size < 10:
            x_size = 10
        if y_size > 80:
            y_size = 80
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
        window = pygame.display.set_mode((self.board_x_size*10, self.board_y_size*10))
        pygame.display.set_caption("Pathfinder")
        while run:

            window.fill(colors.background)
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
                elif pygame.mouse.get_pressed()[2]:
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.find_best_path(self.nodes[start_y][start_x], self.nodes[end_y][end_x])

            for row in self.nodes:
                for node in row:
                    pygame.draw.rect(window, node.get_color(), (node.x_cord, node.y_cord, node.size, node.size))

            pygame.display.update()
        pygame.quit()

    def find_best_path(self, start_node, end_node):
        start_node.curr_height = 0
        start_node.step = 0

        step = 1
        #durch while ersetzen
        for c in range(2):
            for row in self.nodes:
                for node in row:
                    node.exhausted = False

            for row in self.nodes:
                for node in row:
                    if node.curr_height == 0 and not node.exhausted:
                        node.exhausted = True
                        try:
                            for i in range(-1, 2, 1):
                                for j in range(-1, 2, 1):
                                    if node.y_cord+i >= 0 and node.x_cord+j >= 0:
                                        temp_node = self.nodes[node.y_cord//10 + i][node.x_cord//10 + j]
                                        if not temp_node.is_wall:
                                            if temp_node.curr_height > 0:
                                                temp_node.curr_height -= 1
                                                temp_node.exhausted = True
                                                if temp_node.curr_height == 0:
                                                    temp_node.step = step
                                            if temp_node.step > step:
                                                temp_node.step = step
                                                temp_node.path_predecessor.clear()
                                                for x in node.path_predecessor:
                                                    temp_node.path_predecessor.append(x)
                                            temp_node.path_predecessor.append(node)
                                            if temp_node == end_node:
                                                for nodes in temp_node.path_predecessor:
                                                    nodes.best_path = True

                        except IndexError:
                            pass
            pygame.display.update()
            step += 1


b = Board()
