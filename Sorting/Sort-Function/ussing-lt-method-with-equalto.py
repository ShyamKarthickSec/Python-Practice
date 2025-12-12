class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y 
        else:
            return self.x < other.x
    
l = [Point(3, 4), Point(1, 2), Point(5, 0), Point(1, 3)]
l.sort()
for p in l:
    print(f"({p.x}, {p.y})")