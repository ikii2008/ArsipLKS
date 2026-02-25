from math import gcd
m = 1000

x1 = 134
x2 = 321
x3 = 500
x4 = 543

d1 = (x2 - x1) % m
d2 = (x3 - x2) % m
d3 = (x4 - x3) % m

g = gcd(d1, m)

d12 = d1 // g
d22 = d2 // g
d32 = d3 // g
m2 = m // g

inv = pow(d1, -1, m)
a = (d2 * inv) % m

c = (x2 - a*x1) % m

x5 = (a * x4 + c) % m
print(x5)
