import random


class Cell:
    def __init__(self) -> None:
        self.entropy = 9
        self._collapse = False

    def collapse(self):
        


    def __repr__(self) -> str:
        if self._collapse:
            return 'C'
        return str(self.entropy)

class Map_gen:
    def __init__(self, dim) -> None:
        self.array = [[Cell() for x in range(dim[0])] for y in range(dim[1])]
       


    def update(self):
    
        return self.array