from .cell import Cell
class Board (object):
    def __init__ (self, cells):
        self.cells = set(cells)

    def cell_on_board(self, cell):
        if cell in self.cells:
            return 1
        else:
            return 0

    def live_neigbour_count(self, cell):
        return sum([self.cell_on_board(n) for n in cell.neighbours()])

    def survivors(self):
        cells_and_neighbour_counts = [(c, self.live_neigbour_count(c)) for c in self.cells]
        return [cc[0] for cc in cells_and_neighbour_counts if cc[1]==3 or cc[1]==2]

    def new_cells(self):
        candidates = [(n,self.live_neigbour_count(n)) for c in self.cells for n in c.neighbours()]
        return [c[0] for c in candidates if c[1]==3]


    def next_generation(self):
        spawned = self.new_cells()
        survivors = self.survivors()
        return Board(spawned+survivors)
        

