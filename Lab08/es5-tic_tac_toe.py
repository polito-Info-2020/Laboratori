##
#  Play tic-tac-toe with two players.
#

def main() :
   # Construct a new empty board.
   board = [[" "] * 3, [" "] * 3, [" "] * 3]

   # Keep making moves until a player has won.
   turn = "X"
   gameOver = False
   while not gameOver :
      if turn == "X" :
         turn = "O"
      else:
         turn = "X"
      takeTurn(board, turn)
      gameOver = gameWon(board, turn) or isFull(board)
   
   # Display the final game board and the winner.
   drawBoard(board)
   if gameWon(board, turn) :
      print("Player", turn, "won!")
   else :
      print("It was a tie.")

## Process the turn for one player.
#  @param board the game board to work with
#  @param mark the symbol used for the player
#
def takeTurn(board, mark) :
   # Display the board.
   drawBoard(board)

   # Read the user's move, ensuring that it is legal.
   print("Player %s, make your move: " % mark)
   row = int(input("  row: "))
   col = int(input("  col: "))
   while board[row][col] != " " :
      print("That wasn't a valid move, try again: ")
      row = int(input("  row: "))
      col = int(input("  col: "))

   # Update the board with the mark.
   board[row][col] = mark 

## Draw the game board.
#  @param board the game board to display
#
def drawBoard(board) :
   for i in range(0, 2) :
      print(" %-2s| %-2s| %-2s" % (board[i][0], board[i][1], board[i][2]))
      print("---+---+---")
   print(" %-2s| %-2s| %-2s" % (board[2][0], board[2][1], board[2][2]))

## Determine if a player has won the game.
#  @param board the board to check for a winner
#  @param mark the mark to check for winning
#  @return True if the game was won with the given mark, False otherwise
#
def gameWon(board, mark) :
   # Check the rows and columns for a winner.
   for i in range(0, 3) :
      if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark :
         return True
      if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark :
         return True
   # Check the diagonals for a winner.
   if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark :
      return True
   if board[2][0] == mark and board[1][1] == mark and board[0][2] == mark :
      return True
   return False

## Determine if the board is full.
#  @param board the board to check
#  @return True if the board is full, False otherwise
#
def isFull(board) :
   for i in range(0, 3) :
      for j in range(0, 3) :
         if board[i][j] == " " :
            return False
   return True

# Call the main function.
main()

