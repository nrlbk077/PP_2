def trapezoid_area(h, a, b):
    area = (a + b) * h/ 2
    return area

h = int(input())
a = int(input())
b  =int(input())

area = trapezoid_area(h,a,b)
print(area)
