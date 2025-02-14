def generator(a,b):
    for i in range(a,b+1):
        if i**2 == i * i:
            yield i**2



x = int(input())
y = int(input())
print(",".join(map(str, generator(x,y))))