'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    placeholder = [x for x in arr if x is 0]
    new_arr = [x for x in arr if x != 0]
    new_arr.extend(placeholder)
    return new_arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")