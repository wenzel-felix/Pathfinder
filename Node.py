import colors


class Node:

    start_node = False
    end_node = False
    is_wall = False
    curr_height = 1
    size = 9
    path_predecessor = []
    exhausted = False
    best_path = False
    step = 1000

    def __init__(self, x_cord_input, y_cord_input):
        self.x_cord = x_cord_input * 10
        self.y_cord = y_cord_input * 10

    def get_color(self):
        if self.end_node:
            return colors.end
        elif self.start_node:
            return colors.start
        elif self.is_wall:
            return colors.wall
        elif self.best_path:
            return colors.best_path
        else:
            return colors.node_color_list[self.curr_height]

    def increase_curr_height(self):
        if self.curr_height < 6:
            self.curr_height += 1

    def decrease_curr_height(self):
        if self.curr_height > 0:
            self.curr_height -= 1

    def do_wall(self):
        self.is_wall = True

    def un_do_wall(self):
        self.is_wall = False
