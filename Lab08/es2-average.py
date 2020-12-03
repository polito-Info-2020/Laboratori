##
#  Compute the average of the neighbors in a table.
#

def main() :
   # Setup a sample table.
   table = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

   # Alternatively, setup a sample table using cycles
   # w, h = 4, 4
   # table = [[y + 1 for x in range(w)] for y in range(h)]

   print(table)

   # Demonstrate that neighborAverage works correctly.
   print("The average at (0,0) is", neighborAverage(table, 0, 0))
   print("The average at (1,2) is", neighborAverage(table, 1, 2))
   print("The average at (3,2) is", neighborAverage(table, 3, 2))

## Conpute the average of neighbors in a table, handling boundary conditions.
#  @param values the table of values to process
#  @param row the row of the element
#  @param column the column of the element
#  @return the average 
def neighborAverage(values, row, column) :
   count = 0
   total = 0
   for i in range(row - 1, row + 2) :
      for j in range(column - 1, column + 2) : 
         if i >= 0 and i < len(values) and j >= 0 and j < len(values[i]) :
            total = total + values[i][j]
            count = count + 1

   return total / count

# Call the main function.
main()

