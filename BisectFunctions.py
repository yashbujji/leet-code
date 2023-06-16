import bisect

# Our sorted list
nums = [1, 3, 4, 4, 6, 7]

# Using bisect
pos = bisect.bisect(nums, 4)
print(f'Position to insert using bisect: {pos}')  # prints 5

# Using bisect_left
pos_left = bisect.bisect_left(nums, 4)
print(f'Position to insert using bisect_left: {pos_left}')  # prints 2

# Using bisect_right
pos_right = bisect.bisect_right(nums, 4)
print(f'Position to insert using bisect_right: {pos_right}') 

# Using insort
nums_insort = nums.copy()  # copy the list to avoid modifying the original
bisect.insort(nums_insort, 5)
print(f'List after inserting with insort: {nums_insort}')  # prints [1, 3, 4, 4, 5, 6, 7]

# Using insort_left
nums_insort_left = nums.copy()
bisect.insort_left(nums_insort_left, 4)
print(f'List after inserting with insort_left: {nums_insort_left}')  # prints [1, 3, 4, 4, 4, 6, 7]


nums_insort_right = nums.copy()
bisect.insort_right(nums_insort_right, 4)
print(f'List after inserting with insort_right: {nums_insort_right}')  # prints [1, 3, 4, 4, 4, 6, 7]
