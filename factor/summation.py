
def summation(numbers: list[int]) -> int:
    """
    summation() is a function which accepts a list of integers
    and returns the sum of all numbers found within the list.
    ex: [2, 1, 3, 1, 0] -> 7
    """

    result = 0

    
    i = 0
    while i < len(numbers):
        result += numbers[i]
        i += 1
    
    return result 



