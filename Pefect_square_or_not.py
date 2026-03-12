import math

n = int(input())

s = int(math.sqrt(n))

if s * s == n:
    print("Perfect Square")
else:
    print("Not Perfect Square")
