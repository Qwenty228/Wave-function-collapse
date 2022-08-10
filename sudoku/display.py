from sudoku import board, entropy_check
import pyglet as pg

def grid(window, batch):
    step_x = window.width/9
    step_y = window.height/9
    for i, x in enumerate(range(0, window.width, int(step_x))):
        color = (0, 255, 255, 255, 0, 0)
        if (i) % 3 == 0: color = (0, 255, 0)*2
        batch.add(2, pg.gl.GL_LINES, None, ('v2f', (x, 0, x, window.height)), ('c3B', color))

    for i, y in enumerate(range(0, window.width, int(step_y))):
        color = (0, 255, 255, 255, 0, 0)
        if (i) % 3 == 0: color = (0, 255, 0)*2
        batch.add(2, pg.gl.GL_LINES, None, ('v2f', (0, y, window.width, y)), ('c3B', color))
    return (step_x, step_y)


class Win(pg.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.board = board
        self.batch = pg.graphics.Batch()
        self.tile_size = grid(self, self.batch)

        pg.clock.schedule_interval(self.update, 1/10)
        
    def update(self, dt):
        try:
            self.board, new_number = entropy_check(self.board)
        except IndexError:
            new_number = None
        fontsize = min(self.tile_size)//1.5
        for y, col in enumerate(reversed(self.board)):
            for x, number in enumerate(col):
                if number == 0: continue
                color = (255, 255, 255, 255)
                if [abs(len(self.board) - y - 1), x] == new_number: color = (0, 255, 25, 255)
                n = pg.text.Label(str(number), font_size=fontsize, batch=self.batch)
                n.x = x*self.tile_size[0] + fontsize/4
                n.y = y*self.tile_size[1] + fontsize/10
                n.color = color
                
                
        

    def on_draw(self):
        self.clear()
        self.batch.draw()



if __name__ == '__main__':
    Win(500, 500, caption='Wave function sudoku')
    pg.app.run()