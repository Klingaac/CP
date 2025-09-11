import math

def isPrime(n: int):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

for k in range(2,100):
    ns = [6*k-1, 6*k+1]
    for n in ns:
        if isPrime(n):
            print(f"{n}: ✅")
        else:
            print(f"{n}: ❌")