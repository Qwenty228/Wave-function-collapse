import random
from pyglet import image

image_0 = {'image':image.load('images/0.png'),
            'name':'C',
            'n': ['D', "C"],
            's': ['U', "C"],
            'e': ['L', "C"],
            'w': ['R', "C"]}
image_1 = {'image':image.load('images/1.png'),
            'name':'R',
            'n': ['U', 'L', 'R'],
            's': ['D', "L", "R"],
            'e': ['C', 'L'],
            'w': ['D', "R", 'U']
            }
image_2 = {'image':image.load('images/2.png'),
            'name':'D',
            'n': ['R', "L", "U"],
            's': ['C', 'U'],
            'e': ['U', "D", "R"],
            'w': ['R', 'U', "D"]}
image_3 = {'image':image.load('images/3.png'),
            'name':'L',
            'n': ['R', 'U', "L"],
            's': ['D', "R", "L"],
            'e': ['U', 'D', 'R'],
            'w': ['C', 'R']}
image_4 = {'image':image.load('images/4.png'),
            'name':'U',
            'n': ['C', 'D'],
            's': ['D', "R", 'L'],
            'e': ['R', 'D', 'U'],
            'w': ['L', "D", 'U']}

image_list = [image_0, image_1, image_2, image_3, image_4]
image_dict = {'C':image_0, 
                'R':image_1,
                'D': image_2,
                "L":image_3,
                "U": image_4}

def intersection(*l):
    lists = [i for i in l if i]
    if lists == []:
        return []

    its = lists[0]
    for lst in lists[1:]:
        its = [i for i in its if i in lst]
    return its


class Cell:
    def __init__(self) -> None:
        self.entropy = 9
        self.image = None
        self._images = []

    def collapse(self, image):
        self.image = image

        
    def __repr__(self) -> str:
        if self.image:
            return 'C' + self.image['name']
        return str(self.entropy)

class Map_gen:
    def __init__(self, dim) -> None:
        self.dim = dim
        self.array = [[Cell() for x in range(dim[0])] for y in range(dim[1])]
        self.array[0][0].collapse(random.choice([image_1, image_2]))


    def update(self):
        minimum = 9
        current_mins = []

        for y, col in enumerate(self.array):
            for x, row in enumerate(col):
               
                if not row.image:
                    n = s = e = w = []
                    # south of neighbor
                    if y > 0:
                        if (possible := self.array[y - 1][x].image):
                            s = possible['s']               
                    # north of neighbor
                    if y < self.dim[1] - 1:
                        if (possible := self.array[y + 1][x].image):
                            n = possible['n']
                    # west of neighbor
                    if x < self.dim[0] - 1:
                        if (possible := self.array[y][x+1].image):
                            w = possible['w']
                    # east of neighbor
                    if x > 0 :
                        if (possible := self.array[y][x-1].image):
                            e = possible['e']
                    l = intersection(n, s, e, w)
                    
                    if l:
                        row.entropy = len(l)
                        if row.entropy < minimum:
                            minimum = row.entropy
                            current_mins = [row]
                        elif row.entropy == minimum:
                            current_mins.append(row)

                        row._images = l
                        #row.image = image_dict[random.choice(l)]
        for cell in current_mins:
            cell.collapse(image_dict[random.choice(cell._images)])

        return self.array