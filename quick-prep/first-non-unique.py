def firstNonUnique(inputString: str):
    hashMap = {}
    
    for char in inputString:
        if char not in hashMap:
            hashMap[char] = 1
        else:
            hashMap[char] += 1
            
    for char in hashMap:
        if hashMap[char] == 1:
            first = char
            break

    return inputString.index(first) + 1
    
def main():
    inputString = 'statistics'
    print(firstNonUnique(inputString))
    
    
if __name__ == '__main__':
    main()