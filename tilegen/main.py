from gui import UI
from map_gen import Map_gen
import pyglet as pg





def make_grid(window, batch, grid_size=50) -> None:
    for x in range(0, window.width, grid_size):
        batch.add(2, pg.gl.GL_LINES, None, ('v2f', (x, 0, x, window.height)), ('c3B', (255, 0, 255, 255, 0, 0)))
    for y in range(0, window.height, grid_size):
        batch.add(2, pg.gl.GL_LINES, None, ('v2f', (0, y, window.width, y)), ('c3B', (255, 0, 255, 255, 0, 0)))
    return [window.width//grid_size, window.height//grid_size]
    

class Win(pg.window.Window):
    cell_size = 50
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.batch = pg.graphics.Batch()
        self.ui = UI(self)
        array_size = make_grid(self, self.batch, self.cell_size)
        self.map = Map_gen(array_size)
        self.ui.array = self.map.array
        self.start = False

        pg.clock.schedule(self.update)

    def on_key_press(self, symbol, modifiers):
        if symbol == pg.window.key.S:
            self.start = True

    def update(self, dt):
        if self.start:
            self.ui.array = self.map.update()
 


    def on_draw(self):
        self.clear()
        self.batch.draw()
        for j, y in enumerate(reversed(self.ui.array)):
            for i, c in enumerate(y):
                if c.image:
                    c.image['image'].blit(i*self.cell_size, j*self.cell_size)

        #self.ui.render()




if __name__ == '__main__':
    Win(500, 500)
    pg.app.run()
