from collections import defaultdict

my_dict = {}
my_dict = defaultdict(lambda: 0, my_dict)
my_string = input("Enter the string: ")
for each_char in my_string:
    my_dict[each_char] = my_dict[each_char] + 1

my_dict = dict(my_dict)

for each_key, each_value in my_dict.items():
    if each_value == 1:
        print("The first non repeating character in the string is: ", each_key)
        break
