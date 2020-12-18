##
#  Count how many times each word occurs in a file and display the top 100
#  words.
#

# Read the file name from the user and open the file.
filename = input("Enter the name of a file: ")
inf = open(filename, "r")

# Create a new empty dictionary.
counts = {}

# Count the words in the file.
for line in inf :
   words = line.split()
   for word in words :
      if word in counts :
         counts[word] = counts[word] + 1
      else :
         counts[word] = 1

# Close the file.
inf.close()

# Find the count for the 100th word.
sorted_counts = sorted(counts.values())
if len(sorted_counts) < 100 :
   count_100 = 1
else :
   count_100 = sorted_counts[len(sorted_counts) - 100]

# Display the counts of all words with frequencies about the 100th word.
count = 0
for word in sorted(counts):
   if counts[word] > count_100 : 
      print("%s: %d" % (word, counts[word]))
      count = count + 1

# Display enough words with frequency equal to the 100th word so that a total
# of 100 words are displayed.
for word in sorted(counts):
   if counts[word] == count_100 and count < 100 : 
      print("%s: %d" % (word, counts[word]))
      count = count + 1

