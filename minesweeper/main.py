import pyglet as pg
import random


ROWS, COLS = 15, 15
MINES = 15

NUM_FONT = 'comicsans'
NUM_COLORS = {1: (0, 0, 0, 255),
              2: (0, 255, 0, 255),
              3: (255, 0, 0, 255),
              4: (255, 120, 0, 255),
              5: (255, 255, 0, 255),
              6: (255, 0, 255, 255),
              7: (0, 0, 255, 255),
              8: (255, 200, 200, 255)}

def get_neighbors(row, col, rows, cols):
    neighbors = []
    if row > 0: # up
        neighbors.append((row - 1, col))
    if row < rows - 1: # down
        neighbors.append((row + 1, col))
    if col > 0: # left
        neighbors.append((row, col - 1))
    if col < cols - 1: # right
        neighbors.append((row, col + 1))

    if row > 0 and col > 0: 
        neighbors.append((row - 1, col - 1))
    if row < rows - 1 and col < cols - 1: 
        neighbors.append((row + 1, col + 1))
    if row > 0 and col < cols - 1: 
        neighbors.append((row - 1, col + 1))
    if row < rows - 1 and col > 0: 
        neighbors.append((row + 1, col - 1))

    return neighbors




def create_mine_field(rows, cols, mines):
    field = [[0  for _ in range(cols)] for _ in range(rows)]
    mines_positions = set()

    while len(mines_positions) < mines:
        row = random.randrange(0, rows)
        col = random.randrange(0, cols)
        pos = row, col

        if pos in mines_positions:
            continue
        mines_positions.add(pos)
        field[row][col] = -1
    for mine in mines_positions:
        for r, c in get_neighbors(*mine, rows, cols):
            field[r][c] += 1
    return field


class Win(pg.window.Window):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pg.graphics.Batch()
        self.size = int(self.width / ROWS)
        self.field = create_mine_field(ROWS, COLS, MINES)
        self.cover_field = [[0  for _ in range(COLS)] for _ in range(ROWS)]
        self._initialize_field()
        for line in self.field:
            print(line)

    def _initialize_field(self):
        
        for i, row in enumerate(reversed(self.field)):
            y = self.size * i
            for j, value in enumerate(row):
                x = j * self.size

                if not self.cover_field[i][j]:
                    value = 0

                background = pg.graphics.OrderedGroup(0)
                foreground = pg.graphics.OrderedGroup(1)
                
                color = (0, 0, 0) if value != -1 else (255, 0, 0)
                self.batch.add(4, pg.gl.GL_QUADS, background, ('v2f', (x, y, 
                                                                 x + self.size, y, 
                                                                 x + self.size, y + self.size,
                                                                 x, y + self.size)), ('c3B', color*4))
                if color[0] == 0:                                                
                    self.batch.add(4, pg.gl.GL_QUADS, background, ('v2f', (x + 2, y + 2, 
                                                                x + self.size - 2, y + 2, 
                                                                x + self.size - 2, y + self.size - 2, 
                                                                x + 2, y + self.size - 2)), ('c3B', (155, 155, 155)*4))
                
                if value in [0,-1]: continue
                text = pg.text.Label(str(value), font_name=NUM_FONT, font_size=20, batch=self.batch, color=NUM_COLORS[value], group=foreground)
                text.x = x + self.size//2
                text.y = y + self.size//2
                text.anchor_x = 'center'
                text.anchor_y = 'center'
            

    def on_draw(self):
        pg.gl.glClearColor(1, 1, 1, 1)
        self.clear()
        self.batch.draw()

        

        

    def on_mouse_press(self, x, y, button, modifiers):
        self.cover_field[y//self.size][x//self.size] == 1

if __name__ == '__main__':
    Win(700, 700, 'minesweeper')
    pg.app.run()