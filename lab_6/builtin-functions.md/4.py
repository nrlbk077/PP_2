import time

num = int(input())        #25100 2123
delay = int(input())
time.sleep(delay / 1000)
result = pow(num,0.5)

print(f"Square root of {num} after {delay} milliseconds is {result}")