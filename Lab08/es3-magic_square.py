##
#  Determine if numbers for a magic square.
#


# Read the values from the user into a 2D board.
def input_board():
    row = -1
    board = []
    for i in range(0, 16):
        # The % operator is used to determine if a new row must be added
        if i % 4 == 0:
            column = 0
            row = row + 1
            board.append([])
        board[row].append(int(input(f"Enter a value (position {row + 1},{column + 1}): ")))
        column = column + 1

    return board


def display_board(board):
    """
    Display the board

    :param board: board to be displayed
    :return: None
    """
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            print(f'{board[row][col]:3}', end=" ")
        print()


def check_magic(board):
    # Determine the target total by summing the first row.
    target = sum(board[0])

    # Assume it is a magic square.  Change isMagicSquare to False if we find
    # evidence that it is not.
    isMagicSquare = True

    # Check that all of the numbers are present.
    for i in range(1, 17):
        if i not in board[0] and i not in board[1] and \
                i not in board[2] and i not in board[3]:
            isMagicSquare = False

    # Check the rows.
    for i in range(1, len(board)):
        if sum(board[i]) != target:
            isMagicSquare = False

    # Check the columns.
    for j in range(0, 3):
        if board[0][j] + board[1][j] + board[2][j] + board[3][j] != target:
            isMagicSquare = False

    # Check the diagonals.
    if board[0][0] + board[1][1] + board[2][2] + board[3][3] != target:
        isMagicSquare = False
    if board[0][3] + board[1][2] + board[2][1] + board[3][0] != target:
        isMagicSquare = False

    # Alternative way to check the diagonals using loops
    sum_diag = 0
    for i in range(len(board)):
        sum_diag = sum_diag + board[i][i]
    if sum_diag != target:
        isMagicSquare = False

    sum_diag = 0
    for i in range(len(board)):
        sum_diag = sum_diag + board[i][len(board) - 1 - i]
    if sum_diag != target:
        isMagicSquare = False

    return isMagicSquare


def main():
    board = input_board()
    display_board(board)
    isMagicSquare = check_magic(board)
    # Display the result.
    if isMagicSquare:
        print("It is a magic square.")
    else:
        print("It is not a magic square.")


# run the program
main()
