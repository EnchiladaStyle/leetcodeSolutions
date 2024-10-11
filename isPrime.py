def isPrime(num):

    if num == 2:
        return "prime"
    if num%2 == 0:
        return "not prime"
    
    i = 2

    while i < num**.5:
        if num%i == 0:
            return "not prime"
        i+=1
    return "prime"

print(isPrime(15))