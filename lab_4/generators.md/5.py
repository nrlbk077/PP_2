def generator(n):
    for i in range(x,-1,-1):
        yield i


x = int(input())
print(",".join(map(str, generator(x))))