import math

def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

def compute_lcm(x, y):

   if x > y:
        greater = x
   else:
        greater = y

   while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

   return lcm

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))

def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)
    
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
    
def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2,end = '')

def name():
    return "Arthur","Ethan","Peter"

def cosine_of_angle(degrees):
    radians = math.radians(degrees)
    cos_value = math.cos(radians)
    return cos_value

