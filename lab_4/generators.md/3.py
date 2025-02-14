def generator(n):
    for i in range(0,n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


x = int(input())
print(",".join(map(str, generator(x))))