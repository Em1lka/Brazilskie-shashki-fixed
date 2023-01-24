from copy import deepcopy

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = min(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = max(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_valid_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        k1 = (0, 0)
        k2 = (0, 0)
        v1 = []
        v2 = []
        counter = 0
        for k in valid_moves:
            if counter == 0:
                k1 = k
                v1 = valid_moves[k1]
                counter += 1
            else:
                k2 = k
                v2 = valid_moves[k2]

        if len(v1) == len(v2):
            valid_moves = valid_moves
        if len(v1) < len(v2):
            valid_moves = {k2: v2}
        if len(v1) > len(v2):
            valid_moves = {k1: v1}
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

