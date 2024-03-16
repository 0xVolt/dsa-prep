def get(inputString):
    freq = {}
    
    for char in inputString:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
        
    for char in freq:
        if freq[char] == 1:
            unique = char 
            break
        
    return inputString.index(unique) + 1 
    
print(get("statistics"))