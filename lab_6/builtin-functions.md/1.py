from functools import reduce

def to_multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)


nums = [2, 3, 4, 5]
result = to_multiply(nums)
print("Result of multiplying", result)
