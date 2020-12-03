##
#  Merge two sorted lists, with alternating elements from each list.
#

def main() :
   # Set up sample lists.
   a = [1, 4, 9, 16]
   b = [9, 7, 4, 9, 11]

   # Demonstrate that merge works correctly.
   print("List a is", a)
   print("List b is", b)
   result = merge(a, b)
   print("The merged list is", result)

## Merge two lists, alternating elements from each.
#  @param a the first list to take elements from
#  @param b the second list to take elements from
#  @return the merged list
#
def merge(a, b) :
   result = []

   # Merge elements from both lists as long as there are elements in both.
   lenShorter = min(len(a), len(b))
   for i in range(0, lenShorter) :
      result.append(a[i])
      result.append(b[i])

   # Add the remaining elements from whichever list was longer.
   for i in range(lenShorter, len(a)) :
      result.append(a[i])
   for i in range(lenShorter, len(b)) :
      result.append(b[i])

   return result

# Call the main function.
main()

