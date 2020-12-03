##
#  Merge two sorted lists into a single sorted list.
#

def main() :
   # Set up two sample lists.
   a = [1, 4, 9, 16]
   b = [4, 7, 9, 9, 11]

   # Demonstrate that mergeSorted works correctly.
   print("List a is", a)
   print("List b is", b)
   merged = mergeSorted(a, b)
   print("The merged list is", merged)


## Merge two sorted lists into a single sorted list.
#  @param a the first sorted list to merge
#  @param b the second sorted list to merge
#
def mergeSorted(a, b) :
   a_pos = 0
   b_pos = 0
   result = []

   # As long as there is an unprocessed element in either list.  
   while a_pos < len(a) or b_pos < len(b) :
      # If there are elements in both lists then take an element from the
      # list that starts with the smaller element.
      if a_pos < len(a) and b_pos < len(b) :
         if a[a_pos] <= b[b_pos] :
            result.append(a[a_pos])
            a_pos = a_pos + 1
         else :
            result.append(b[b_pos])
            b_pos = b_pos + 1
      # If only list a has elements then process the first element.
      elif a_pos < len(a) :
         result.append(a[a_pos])
         a_pos = a_pos + 1
      # If only list b has elements then process the first element.
      else :
         result.append(b[b_pos])
         b_pos = b_pos + 1

   return result
            
# Call the main function.
main()

