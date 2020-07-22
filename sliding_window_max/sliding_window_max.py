'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    start = 0
    end = k
    placeholder = []

    for x in nums:
        window = nums[start:end]
        maxed = max(window)
        placeholder.append(maxed)
        
        if end < len(nums):
            start += 1
            end += 1
            
        else: 
            pass
        
    return placeholder

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
