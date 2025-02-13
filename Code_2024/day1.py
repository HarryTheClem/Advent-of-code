
##### Part 1 #####

# Create empty list to read the data into
input_list = []

# Open input file for day 1 and read data into list
with open("./Code_2024/inputs/day_1_input.txt") as f:
    for line in f:
        input_list.append(line)

# Create two separate lists for the numbers
left_list = []
right_list = []

# Split on the tab to put the numbers from one list into an empty list and the other list of numbers into the right list, remove the \n new line whitespace
for i in input_list:
    left_list.append(i.split("   ")[0])
    right_list.append(i.split("   ")[1].strip("\n"))

# Create empty lists to convert the characters into numbers
left_integer_list = []
right_integer_list = []

# Convert to integers
for i, j in zip(left_list, right_list):
    left_integer_list.append(int(i))
    right_integer_list.append(int(j))

# Sort both of the lists to get the differences for each
sorted_left_list = sorted(left_integer_list)
sorted_right_list = sorted(right_integer_list)

# Create an empty list and get the differences between the numbers
difference_list = []

for i, j in zip(sorted_left_list, sorted_right_list):
    difference_list.append(abs(i - j))

# Find the sum of the absolute to get the puzzle solution
sum(difference_list)


##### Part 2 #####

# Create a list to get the numbers that appear multiple times
similarity_list = []

# Check to see if the number in the right list appears in the left and if so, add it to the list
for i in sorted_left_list:
    for j in sorted_right_list:
        if i == j:
            similarity_list.append(i)

# Because the numbers appear multiple times, you can just sum to get the multiples of each
sum(similarity_list)






