array_nums = [1, 7, 22, 23, 28, 38, 45, 56]
print("Original arrays:")
print(array_nums)
nums = len(list(filter(lambda x: (x%7 == 0 or x%11 == 0) , array_nums)))
print("\nNumber of numbers divisible by 7 or 11 in the above array: ", nums)
