#!/usr/bin/env python3

def testing_duplicate(data):
	if len(data) == len(set(data)):
		return True
	else:
		return False

print(testing_duplicate([1, 3, 55, 8, 4, 3]))
print(testing_duplicate([1, 33, 8, 4, 3]))
