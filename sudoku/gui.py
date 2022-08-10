import imgui
from imgui.integrations.pyglet import PygletRenderer

class UI:
    def __init__(self, window):
        # initialize library
        imgui.create_context()
        # get window to draw on
        self.impl = PygletRenderer(window)
        # choose font
        io = imgui.get_io()
        self.font = io.fonts.add_font_from_file_ttf("C:/Windows/Fonts/verdana.ttf",  20)
        self.impl.refresh_font_texture()


        # Window variables
        self.array = []

    def render(self):
        imgui.new_frame()

        imgui.push_font(self.font)
        self.frame_command()
        imgui.pop_font()

        imgui.render()
        self.impl.render(imgui.get_draw_data())

    def frame_command(self):
        imgui.begin('entropy window') 
        for x in self.array:
            imgui.text(str(x))
        imgui.end()