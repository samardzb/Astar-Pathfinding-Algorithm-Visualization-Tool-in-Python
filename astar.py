# By Boris Samardzic
import pygame
import math
from queue import PriorityQueue


pygame.display.set_caption("A* algorithm path finder user interface")
WIDTH = 1000
WIN = pygame.display.set_mode((WIDTH,WIDTH))

#COLOR CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165,0)


class Node:                                                                                         # Creating a class node that will represent each node.
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.bordering_nodes = []
        self.width = width
        self.total_rows = total_rows

    def get_position(self):
        return self.row, self.col
    
    def is_barrier(self):                                                                           # checks if a square is a barrier
        return self.color == BLACK

    def reset(self):
        self.color = WHITE

    def set_start(self):                                                                            # making the starting node an orange colour
        self.color = ORANGE

    def set_closed(self):
        self.color = RED

    def set_possible_pathnode(self):                                                                # making a node part of the set that contains squares that could be a possible pathway for the shortest path being calculated
        self.color = GREEN

    def set_barrier(self):
        self.color = BLACK

    def set_end(self):                                                                              # making the ending node an blue colour
        self.color = BLUE

    def set_shortest_path(self):
        self.color = PURPLE 

    def draw(self, win):                                                                            # called in order to draw a square on the screen
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_bordering_nodes(self, grid):                                                         # updates the bordering nodes of the current node
        self.bordering_nodes = []
        
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():        # Checking for a bordering node on the RIGHT
            self.bordering_nodes.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():                          # Checking for a bordering node on the  LEFT
            self.bordering_nodes.append(grid[self.row][self.col - 1])
        
        
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():        # Checking for a bordering node BELOW
            self.bordering_nodes.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():                          # Checking for a bordering node ABOVE
            self.bordering_nodes.append(grid[self.row - 1][self.col])




def h_fxn(coord1, coord2):                                                                          #defining the Heuristic (H) function using Manhattan  distance (aka L distance)
    x1, y1= coord1
    x2, y2 =coord2
    return abs(x1-x2) + abs(y1-y2)

def make_shortest_path(previous_node, current, draw):
	while current in previous_node:
		current = previous_node[current]
		current.set_shortest_path()
		draw()

def algorithm(draw, grid, start, end):
    count=0                                                                                           #used to see when a node was inserted into the queue
    possible_pathnode_set = PriorityQueue()                                                           #queue will store the possible pathnodes
    possible_pathnode_set.put((0, count, start))                                                      #initializing the queue with the f(n) function of the beginning node which is just zero
    previous_node = {}
    g_fxn = {node: float("inf") for row in grid for node in row} 
    g_fxn[start] = 0
    f_fxn = {node: float("inf") for row in grid for node in row}
    f_fxn[start] = h_fxn(start.get_position(), end.get_position())

    possible_pathnode_set_hash = {start}                                                               # using a hash that has the same data as the queue, in order to check if something is in the queue
    while not possible_pathnode_set.empty():                                                           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = possible_pathnode_set.get()[2]                                                       # popping node out of priority queue and accoridngly deleting in hash
        possible_pathnode_set_hash.remove(current)

        if current == end:
            make_shortest_path(previous_node, end, draw)
            end.set_end()
            return True

        for bordering_node in current.bordering_nodes:
            temp_g_fxn = g_fxn[current] + 1

            if temp_g_fxn < g_fxn[bordering_node]:                                                  # if a better path has been found using the bordering node, store this new better path that uses that bordering node
                previous_node[bordering_node] = current
                g_fxn[bordering_node] = temp_g_fxn
                f_fxn[bordering_node] = temp_g_fxn + h_fxn(bordering_node.get_position(), end.get_position())
                if bordering_node not in possible_pathnode_set_hash:
                    count += 1
                    possible_pathnode_set.put((f_fxn[bordering_node], count, bordering_node))      # adding a bordering node to the queue and hash
                    possible_pathnode_set_hash.add(bordering_node)
                    bordering_node.set_possible_pathnode()

        draw()

        if current != start:
            current.set_closed()
    return False

def fill_nodes(rows, width):                                                                        #2D list that contains instances of Node object filling up the grid
    grid = []
    individual_square_width = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,individual_square_width, rows)
            grid[i].append(node)
    return grid

def draw_gridlines(win, rows, width):                                                               #draws the gridlines
    individual_square_width = width//rows
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i*individual_square_width), (width, i*individual_square_width)) #drawing horizontal lines
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j*individual_square_width,0), (j*individual_square_width,width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_gridlines(win, rows, width)
    pygame.display.update()

def get_position_click(pos, rows, width):
    individual_square_width = width// rows
    y, x = pos
    row = y//individual_square_width
    col = x//individual_square_width
    return row, col

def main(win, width):
    ROWS=40
    grid = fill_nodes(ROWS, width)

    # start and end position
    start_pos = None
    end_pos = None

    run_program = True #running main loop
    

    while run_program:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_program = False

            if pygame.mouse.get_pressed()[0]:                                                           # Checking for left mouse click. If clicked it will either set the start, end or barrier accordingly
                pos = pygame.mouse.get_pos()
                row, col = get_position_click(pos, ROWS, width)
                node = grid [row][col]
                if not start_pos and node != end_pos:
                    start_pos = node
                    start_pos.set_start()

                elif not end_pos and node != start_pos:
                    end_pos = node
                    end_pos.set_end()
                elif node != end_pos  and node != start_pos:
                    node.set_barrier()

            elif pygame.mouse.get_pressed()[2]:                                                     # Checking for right mouse click. If clicked it will either reset the start, end or barrier square back to a white square
                pos = pygame.mouse.get_pos()
                row, col = get_position_click(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start_pos:
                    start_pos = None
                elif node == end_pos:
                    end_pos = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start_pos and end_pos:                           #runs algorith if user presses space bar
                    for row in grid:
                        for node in row:
                            node.update_bordering_nodes(grid)
                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start_pos , end_pos)      #anonymous function draw used within algorithm

                if event.key == pygame.K_c:                                                         #clears everything is user presses c
                    start_pos = None
                    end_pos = None
                    grid = fill_nodes(ROWS, width)
    pygame.quit()
main(WIN, WIDTH)