'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    placeholder = []
    
    # Can use enumerate to both loop through the array, but also increase the index(i)
    for i, x in enumerate(arr):
        result = 1
        everything_else = arr[:i] + arr[i + 1:]
        
        for a in everything_else:
            result *= a
            
        placeholder.append(result)
         
    return placeholder


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
