class GameState:

    def __init__(self, white_player, black_player):
        self.white_pieces = {}
        self.black_pieces = {}
        self.white_player = white_player
        self.black_player = black_player
        self.current_player = white_player

    def display(self):
        pass

    def get_legal_moves(self, player):
        moves = []
        if player == self.white_player:
            for piece in self.white_pieces.keys():
                moves.append(piece.get_legal_moves(self.white_pieces[piece], self))
        else:
            for piece in self.black_pieces.keys():
                moves.append(piece.get_legal_moves(self.black_pieces[piece],self))
        return moves

    def get_current_players_pieces(self):
        pass

    def get_opposing_players_pieces(self):
        pass



