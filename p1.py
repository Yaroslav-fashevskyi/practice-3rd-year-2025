import math
A = 0
B = math.pi / 2
M = 20
H = (B - A) / M
print("  x\t\tf(x) = sin(x) - cos(x)")
print("-" * 35)
for i in range(0, M + 1):
   x = A + i * H
   fx = math.sin(x) - math.cos(x)
   print(f"{x:.5f}\t{fx:.5f}")