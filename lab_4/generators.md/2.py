def generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


x = int(input())
print(",".join(map(str, generator(x))))