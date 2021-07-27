# Python script to find first non-repeating character in the string
from collections import defaultdict

# Creating a Dictionary and defaulting the values to 0
my_dict = {}
my_dict = defaultdict(lambda: 0, my_dict)
# Getting the input from  the user
my_string = input("Enter the string: ")
# Loop through the string character by character to calculate the number of occurrences
for each_char in my_string:
    my_dict[each_char] = my_dict[each_char] + 1
# Converting Default dictionary to normal dictionary
my_dict = dict(my_dict)
# Loop through the dictionary and break the loop when fist value is found
for each_key, each_value in my_dict.items():
    if each_value == 1:
        print("The first non repeating character in the string is: ", each_key)
        break
