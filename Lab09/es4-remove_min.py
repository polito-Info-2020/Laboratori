##
#  Remove the minimum value from a list.
#
from random import randint

def main() :
   # Create a list of random values.
   randomValues = []
   for i in range(0, 10) :
      randomValues.append(randint(0, 10))

   # Demonstrate that removeMin functions correctly.
   print("The original list is: ", randomValues)
   randomValues = removeMin(randomValues)
   print("With the minimum removed: ", randomValues)


## Remove the minimum value from a list.
#  @param data the list of values to process
#  @return a new copy of the list with the minumum element removed
#
def removeMin(data) :
   smallest = data[0]
   smallest_pos = 0

   for i in range(1, len(data)) :
      if data[i] < smallest :
         smallest = data[i]
         smallest_pos = i

   return data[0 : smallest_pos] + data[smallest_pos + 1 : len(data)]

# Call the main function.
main()

