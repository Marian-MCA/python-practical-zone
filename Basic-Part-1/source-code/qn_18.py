""""
Question is here
Write a Python program to count the number 4 in a given list.
""""

def count_num_4(list):
    count = 0
    for ele in list:
        if ele == 4:
            count = count + 1
    return count
    
print(count_num_4([3, 4, 54, 6, 1, 5, 5,]))
print(count_num_4([3, 4, 54, 6, 4, 5, 4,]))
