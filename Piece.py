
class Piece:

    def __init__(self):
        pass

    def move(self):
        pass

    def get_legal_moves(self, location, gamestate):
        pass

class Pawn(Piece):

class Rook(Piece):

class Knight(Piece):

class Bishop(Piece):

class Queen(Piece):

class King(Piece):

    def get_legal_moves(self, location, gamestate):
        candidates = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if !(i==0 and j==0):
                    candidate=location.location_with_displacement(i, j)
                    if ()




