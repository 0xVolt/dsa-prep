def solution(cards, start, target):
    targetIndex = cards.index(target)
    
    if start == targetIndex:
        return 0
    elif abs(targetIndex - start) == 1:
        return 1
    else:
        forwardDistance = abs(targetIndex - start)
        backwardDistance = abs(start + ((len(cards) - 1) - targetIndex) + 1)

        return forwardDistance if forwardDistance < backwardDistance else backwardDistance 

def main():
    cards = ['black', 'grey', 'brown', 'red', 'blue']    
    
    start = 3
    target = 'black'
    
    print(solution(cards, start, target))
    
    
if __name__ == '__main__':
    main()