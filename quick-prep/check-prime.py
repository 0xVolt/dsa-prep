def checkPrime(x):
    """
    First check if the number is less than 2. Then, check if the number is divisible by
    any number from 2 to sqrt(number) inclusive to determine whether it's prime.
    """
    if x < 2:
        return "Not Prime"
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return "Not Prime"
        
    return "Prime"

x = int(input())

print(checkPrime(x))