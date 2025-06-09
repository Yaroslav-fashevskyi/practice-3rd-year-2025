import math

a = 20.3
x = 0.5

print("   x\t\tf(x)")
print("-" * 25)

while x <= 2.0 + 1e-10:  # додано epsilon, щоб включити 2.0
   if x > 1:
       fx = math.log10(x + 1)
   else:
       sqrt_val = math.sqrt(abs(a * x))
       sin_val = math.sin(sqrt_val)
       fx = 1 / (sin_val ** 2) if sin_val != 0 else float('inf')
   print(f"{x:.1f}\t{fx:.5f}")
   x += 0.1