class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def keyFun(point):
    return point.x

points = [Point(3, 4), Point(1, 2), Point(5, 0), Point(2, 3)]
points.sort(key=keyFun)
for p in points:
    print(f"({p.x}, {p.y})")
points.sort(key=keyFun, reverse=True)
for p in points:    
    print(f"({p.x}, {p.y})")