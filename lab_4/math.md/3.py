import math

def polygon(s,l):
    area = (s * l**2) / (4 * math.tan(math.pi / s)) 
    return area



side = int(input())
len = int(input())
area = polygon(side,len)
print(area)