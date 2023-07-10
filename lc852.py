def find_max_index(array):
    max_value = max(array)
    max_index = array.index(max_value)
    return max_index

# Testing the function
arr = [1, 3, 7, 9, 2, 8]
print(find_max_index(arr))  # Output: 3
