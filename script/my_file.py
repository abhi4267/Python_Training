import math

from lib.commons import add,compute_hcf,compute_lcm,multiply, subtract,divide, print_factors,recur_fibo, recur_sum,cosine_of_angle

result = add(5,3)
print("Result:", result)

print(compute_hcf(45,36))

print(compute_lcm(45,180))

print(multiply(4,5))

print(subtract(100,50))

print(divide(20,10))

print( print_factors(20),end=" ")

print(recur_fibo(7))

print(recur_sum(10))

angle = 60
result = cosine_of_angle(angle)
print(f"cos({angle}°) = {result:.4f}")