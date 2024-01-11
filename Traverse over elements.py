# implimintation algorithm to find descending sorted triplets
def find_descending_sorted_triplet (arr):
    # Get the length of the array
    n = len(arr)
    # Initialize three variables as negative infinity
    first = second = third = float('-inf')
    # Traverse the array from right to left
    for l in range(n-1, -1, -1):
        # If the current element is greater than third
        if arr[l] > third:
            # Update first, second, and third accordingly
            first = second
            second = third
            third = arr[l]
        # If the current element is greater than the second but less than or equal to third
        elif arr[l] > second and arr[l] <= third:
            # Update the second and third accordingly
            first = second
            second = arr[l]
        # If the current element is greater than the first but less than or equal to second
        elif arr[l] > first and arr[l] <= second:
            # Update first accordingly
            first = arr[l]
        # Otherwise, continue to the next iteration
        else:
            continue
    # If a descending sorted triplet exists in the array, return it
    if first == float('-inf') or second == float('-inf') or third == float('-inf'):
        return None
    else:
        return (third, second, first)

# Test the function with an example array
arr = [10, 2, 7, 8, 4, 5, 6]
print(find_descending_sorted_triplet (arr))

