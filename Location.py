class Location:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def location_with_displacement(self, dx, dy):
        return Location(self.x+dx, self.y+dy)

    def __eq__(self, other):
        return isinstance(other, Location) and self.x == other.x and self.y == other.y
