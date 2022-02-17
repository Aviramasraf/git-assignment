import random

X = "X"
O = "O"
EMPTY = "*"

# Bigger board sizes are less likely
RANDOM_SIZES = [3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]

# Type aliases
Player = str
Board = list[list]
Coords = tuple[int, int]


def create_board(size: int) -> Board:
    """
    Create an empty game board.

    :param size: the size of the board
    :return: the initialized board
    """
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(EMPTY)
        board.append(row)
    return board


def check_rows(board, player):
    for row in board:
        if row.count(player) == len(row):
            return True
    return False


def check_columns(board, player):
    for i, row in enumerate(board):
        marks = 0
        for j in range(len(row)):
            marks += board[j][i] == player
        if marks == len(row):
            return True
    return False


def won(player: Player, board: Board) -> bool:
    return check_rows(board, player) or check_columns(board, player)


def update_board(board: Board, player: Player, coords: Coords):
    """
    Updates a game board with a given player's move.

    :param board: the board to update
    :param player: the player that made the move
    :param coords: the coordinates (row, column) of the player's move
    """
    board[coords[0]][coords[1]] = player


def get_move(player: Player) -> Coords:
    """
    Asks a player for their next move.

    :param player: the player whose turn it is to play
    :return: the coordinates the player chose
    """
    row, col = input(f"{player}'s move: ").split()
    return int(row), int(col)


def show_board(board: Board):
    """
    Print the current state of the game board.

    :param board: the board to display
    """
    for row in board:
        print(" ".join(row))


def show_winner(player: Player):
    """
    Print an endgame message with the name of the winner.

    :param player: the player who won
    """
    print(f"\nAnd the WINNER is: .....\n!!!!!!!!!!!! {player} !!!!!!!!!!!!")


def switch_player(current_player: Player) -> Player:
    """
    Determine whose turn it is next.

    :param current_player: the player who played last
    :return: the player who will play next
    """
    return X if current_player == O else O


def play_game(board_size: int = None):
    """
    Play a game of Tic-Tac-Toe.

    :param board_size: the size of the game board. randomized by default.
    """
    if not board_size:
        board_size = random.choice(RANDOM_SIZES)
    board = create_board(board_size)
    current_player = X
    while not won(current_player, board):
        show_board(board)
        coordinates = get_move(current_player)
        update_board(board, current_player, coordinates)
        current_player = switch_player(current_player)
    show_winner(current_player)


if __name__ == '__main__':
    play_game()
