##
#  Implement and demonstrate a collection of list functions.
#

# Define constant variables.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def main() :
   print("The original data for all functions is: ", ONE_TEN)

   # Demonstrate swapping the first and last element.
   data = list(ONE_TEN)
   swapFirstLast(data)
   print("After swapping first and last: ", data)

   # Demonstrate shifting to the right.
   data = list(ONE_TEN)
   shiftRight(data)
   print("After shifting right: ", data)

   # Demonstrate replacing even elements with zero.
   data = list(ONE_TEN)
   replaceEven(data)
   print("After replacing even elements: ", data)

   # Demonstrate replacing values with the larger of their neighbors.
   data = list(ONE_TEN)
   replaceNeighbors(data)
   print("After replacing with neighbors: ", data)

   # Demonstrate removing the middle element.
   data = list(ONE_TEN)
   removeMiddle(data)
   print("After removing the middle element(s): ", data)

   # Demonstrate moving even elements to the front of the list.
   data = list(ONE_TEN)
   evenToFront(data)
   print("After moving even elements: ", data)

   # Demonstrate finding the second largest value.
   print("The second largest value is: ", secondLargest(ONE_TEN))

   # Demonstrate testing if the list is in increasing order.
   print("The list is in increasing order: ", isIncreasing(ONE_TEN))

   # Demonstrate testing if the list contains adjacent duplicates.
   print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN))

   # Demonstrate testing if the list contains duplicates.
   print("The list has duplicates: ", hasDuplicate(ONE_TEN))

## Swap the first and last element in a list.
#  @param data the list of values to process
#
def swapFirstLast(data) :
   if len(data) == 0 :
      return 

   temp = data[0]
   data[0] = data[len(data) - 1]
   data[len(data) - 1] = temp

## Shift the elements to the right.
#  @param data the list of values to process
#
def shiftRight(data) :
   if len(data) == 0 :
      return

   last = data[len(data) - 1]
   # Iteration starting from the last element in the list and ending at the second one (i = 1)
   for i in range(len(data) - 1, 0, -1) :
      data[i] = data[i-1]
   data[0] = last

## Replace all even elements in the list with 0.
#  @param data the list of values to process
#
def replaceEven(data) :
   for i in range(0, len(data)) :
      if data[i] % 2 == 0 :
         data[i] = 0

## Replace each value with the larger of its neighbors.
#  @param data the list of values to process
#
def replaceNeighbors(data) :
   # Make a copy of the list 
   old_values = list(data)
   for i in range(1, len(data) - 1) :
      data[i] = max(data[i - 1], data[i + 1])

## Remove the middle element or elements from a list.
#  @param data the list of values to process
#
def removeMiddle(data) :
   if len(data) == 0 :
      return

   if len(data) % 2 == 1 :
      data.pop(len(data) // 2)
   else :
      data.pop(len(data) // 2)
      data.pop(len(data) // 2)

## Move even elements to the front of the list.
#  @param data the list of values to process
#
def evenToFront(data) :
   evenPos = 0
   pos = 0
   while pos < len(data) :
      if data[pos] % 2 == 0 :
         temp = data.pop(pos)
         data.insert(evenPos, temp)
         evenPos = evenPos + 1
      pos = pos + 1

## Identify the second largest value in a list.
#  @param data the list of values to process
#  @return the second largest value in the list
#
def secondLargest(data) :
   largest = max(data)
   secondLargest = min(data)
   for value in data :
      if value > secondLargest and value != largest :
         secondLargest = value
   return secondLargest
   
## Determine whether or not the list is in increasing order.
#  @param data the list of values to process
#  @return True if the list is in increasing order, False otherwise
#
def isIncreasing(data) :
   for i in range(0, len(data) - 1) :
      if data[i] > data[i + 1] :
         return False
   return True

## Determine if the list contains adjacent duplicate elements.
#  @param data the list of values to process
#  @return True if the list contains adjacent duplicates, False otherwise
#
def hasAdjacentDuplicate(data) :
   for i in range(0, len(data) - 1) :
      if data[i] == data[i + 1] :
         return True
   return False

## Determine if the lost contains duplicate elements.
#  @param data the list of values to process
#  @return True if the list contains duplicates, False otherwise
#
def hasDuplicate(data) :
   for i in range(0, len(data) - 1) :
      for j in range(i + 1, len(data)) :
         if data[i] == data[j] :
            return True
   return False

# Call the main function.
main()

