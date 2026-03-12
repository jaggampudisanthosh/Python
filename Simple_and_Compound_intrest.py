p = float(input())
r = float(input())
t = float(input())
si = (p * r * t) / 100
ci = p * (1 + r/100) ** t - p

print("Simple Interest =", si)
print("Compound Interest =", ci)
