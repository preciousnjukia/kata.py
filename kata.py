def find_unsorted_subarray(arr):
    # Step 1: Find the leftmost index where the array is not sorted
    m = 0
    while m < len(arr) - 1 and arr[m] <= arr[m + 1]:
        m += 1

    # If the entire array is sorted, return [0, 0]
    if m == len(arr) - 1:
        return [0, 0]

    # Step 2: Find the rightmost index where the array is not sorted
    n = len(arr) - 1
    while n > 0 and arr[n] >= arr[n - 1]:
        n -= 1

    # Step 3: Find the minimum and maximum values in the unsorted subarray
    min_val = min(arr[m:n + 1])
    max_val = max(arr[m:n + 1])

    # Step 4: Extend the unsorted subarray to include any additional elements
    while m > 0 and arr[m - 1] > min_val:
        m -= 1
    while n < len(arr) - 1 and arr[n + 1] < max_val:
        n += 1

    # Step 5: Return the result
    return [m, n]

# Example usage:
arr = [1, 2, 3, 6, 4, 4]
result = find_unsorted_subarray(arr)
print(result)  # Output: [3, 5]
