from time import time

def isPrime(n):
    isPrime = (n > 1)
    i = 2
    while isPrime and i <= (n // 2):
        isPrime = (n % i != 0)
        i += 1
    return isPrime

def primesMemory(n):
    primes = [2]
    aux = 3
    while len(primes) < n:
        isPrime = True
        i = 0
        while isPrime and primes[i] <= (aux // 2):
            isPrime = (aux % primes[i] != 0)
            i += 1
        if isPrime:
            primes.append(aux)
        aux += 1
    return primes

def primesCPU(n):
    primes = list()
    p = 2
    while len(primes) < n:
        if isPrime(p):
            primes.append(p)
        p += 1
    return primes

def yes_or_no(question):
    while "invalid answer":
        reply = input(question+' (y/n) ').lower().strip()
        if reply == "y" or reply == "yes" or reply == "":
            return True
        if reply == "n" or reply == "no":
            return False

if __name__ == "__main__":
    n = int(input("Number: "))
    # memory method
    t0 = time()
    primes = primesMemory(n)
    t = time() - t0
    print(f"Memory-demanding method: {t}s")
    # cpu method
    t0 = time()
    primes = primesCPU(n)
    t = time() - t0
    print(f"CPU-demanding method: {t}s")
    if yes_or_no("Print prime list?"):
        print(", ".join((str(p) for p in primes)))
