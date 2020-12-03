##
#  Determine if numbers for a magic square.
#

# Read the values from the user into a 2D board.
row = -1
board = []
for i in range(0, 16) :
   # The % operator is used to determine if a new row must be added
   if i % 4 == 0 :
      column = 0
      row = row + 1
      board.append([])
   board[row].append(float(input("Enter a value: ")))

# Display the board.
for row in range(0, len(board)) :
   for col in range(0, len(board[row])) :
      print(board[row][col], end=" ")
   print()

# Determine the target total by summing the first row.
target = sum(board[0])

# Assume it is a magic square.  Change isMagicSquare to False if we find
# evidence that it is not.
isMagicSquare = True

# Check that all of the numbers are present.
for i in range(1, 17) :
   if i not in board[0] and i not in board[1] and \
      i not in board[2] and i not in board[3] :
         isMagicSquare = False

# Check the rows.
for i in range(1, len(board)) :
   if sum(board[i]) != target :
      isMagicSquare = False

# Check the columns.
for i in range(0, 3) :
   if board[0][i] + board[1][i] + board[2][i] + board[3][i] != target :
      isMagicSquare = False

# Check the diagonals.
if board[0][0] + board[1][1] + board[2][2] + board[3][3] != target :
   isMagicSquare = False
if board[0][3] + board[1][2] + board[2][1] + board[3][0] != target :
   isMagicSquare = False

# Alternative way to check the diagonals using cycles
somma = 0
for i in range(len(board)):
   somma = somma + board[i][i]
if somma != target:
   isMagicSquare = False
somma = 0
for i in range(len(board)):
   somma = somma + board[i][len(board)-1-i]
if somma != target:
   isMagicSquare = False

# Display the result.
if isMagicSquare :
   print("It is a magic square.")
else :
   print("It is not a magic square.")

