def isPrime(num):
    if num == 2:
        return True
    if num == 1:
        return True
    
    i = 2
    while i <= num**.5:
        if num%i == 0:
            return False
        i += 1
    return True

print(isPrime(11))