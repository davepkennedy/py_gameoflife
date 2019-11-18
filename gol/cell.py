class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Cell({self.x},{self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Cell):
            return ((self.x == other.x) and (self.y == other.y))
        return False

    def __hash__ (self):
        return hash(repr(self))

    def neighbours(self):
        offsets = [-1,0,1]
        for (x,y) in [(x,y) for x in offsets 
            for y in offsets  
            if not (x==0 and y==0)]:
            yield Cell(self.x+x, self.y+y)