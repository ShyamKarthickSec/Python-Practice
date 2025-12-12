class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return self.x < other.x
    
l = [Point(3, 4), Point(1, 2), Point(5, 0), Point(2, 3)]
l.sort()
for p in l:
    print(f"({p.x}, {p.y})")