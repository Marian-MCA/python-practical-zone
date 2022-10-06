#!/usr/bin/evn python3

# Reading comma-separtated value from console
cs_value = input()

# Return the string split according to comma ',' 
# stored in a new place
split_string = cs_value.split(',')

# Print the strings
print("List : {0}".format(list(split_string)))
print("Tuple : {0}".format(tuple(split_string)))


