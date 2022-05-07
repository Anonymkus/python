import math

a = float(input())
b = float(input())
c = float(input())
print(f"{a}x^2 {b}x {c}")

D = b ** 2 - 4 * a * c

if D > 0:
	x1 = (-b - math.sqrt(D)) / (2 * a)
	x2 = (-b + math.sqrt(D)) / (2 * a)
	print(x1, x2)
elif D == 0:
	x1 = -b / (2 * a)
	print(x1)
else:
	print("корней нет")

