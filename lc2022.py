original = [1,2,3,4]
m = 2
n = 2

# Empty list to hold the final output
output = []

# Iterate over m (number of desired rows)
for i in range(m):
    # Print current iteration value
    print("Iteration:", i)    
    # Compute start and end indices for slicing
    start_index = i * n
    end_index = (i + 1) * n
    # Print start and end indices
    print("Start index:", start_index)
    print("End index:", end_index)
    # Extract the slice from original list and append to output
    slice = original[start_index:end_index]    
    # Print the slice
    print("Slice:", slice)
    # Append the slice to the output list
    output.append(slice)
    # Print the output list at current stage
    print("Current output:", output, "\n")

print("Final output:", output)

print(output)