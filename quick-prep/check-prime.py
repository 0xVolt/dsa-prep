def checkPrime(x):
    if x < 2:
        return "Not Prime"
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return "Not Prime"
        
    return "Prime"

x = int(input())

print(checkPrime(x))