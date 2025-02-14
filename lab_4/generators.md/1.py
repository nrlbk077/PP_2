def square_generator(n):
    for i in range(n + 1):
        yield i ** 2


for square in square_generator(5):
    print(square)
