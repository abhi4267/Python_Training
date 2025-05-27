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

   # choose the greater number
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