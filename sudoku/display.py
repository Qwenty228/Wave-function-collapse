from sudoku import entropy_check
import pyglet as pg
from gui import UI

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
        self.reset()
        self.ui = UI(self)
        pg.clock.schedule(self.update)
        
        

    def reset(self):
        self.board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                        [6, 0, 0, 1, 9, 5 ,0 ,0 ,0],
                        [0, 9, 8, 0, 0, 0, 0, 6, 0],
                        [8, 0, 0, 0, 6, 0, 0, 0, 3],
                        [4, 0, 0, 8, 0, 3, 0, 0, 1],
                        [7, 0, 0, 0, 2, 0, 0, 0, 6],
                        [0, 6, 0, 0, 0, 0, 2, 8 ,0],
                        [0, 0, 0 ,4, 1 ,9, 0, 0, 5],
                        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
        
        self.batch = pg.graphics.Batch()
        self.tile_size = grid(self, self.batch)
       

    def update(self, dt):
        try:
            self.board, new_number, entropy_board = entropy_check(self.board)
            self.ui.array = entropy_board
            done = False
    
        except IndexError:
            new_number = None


            for c in self.board:
                if 0 in  c:
                    self.reset()
                    break
            else:
                done = True
                print('Done')
                  
          
        if not done:
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
        self.ui.render()



if __name__ == '__main__':

    Win(1000, 800, caption='Wave function sudoku')
    pg.app.run()