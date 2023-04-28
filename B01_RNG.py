import time

m = 9
a = 3
c = 5

seed = 5

# print(seed)

def RNG(m,a,c,seed):
    if seed == 0 :
        return 1
    else:
        return ((a*(RNG(m,a,c,seed-1))) +c ) % m

for i in range (10):
    
    print(RNG(m,a,c,i))