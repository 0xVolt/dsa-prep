def processorTime(processors, tasks):
    processors = sorted(processors)
    tasks = sorted(tasks, reverse=True)    
    
    # nProcessors = len(processors)
    # nTasks = len(tasks)

    result = 0

    for i, processor in enumerate(processors):
        maxTime = 0
        upper = (i + 1) * 4
        lower = upper - 4

        for task in tasks[lower : upper]:
            processTime = processor + task
            if maxTime < processTime:
                maxTime = processTime

        if maxTime > result:
            result = maxTime
            
    print(result)

def main():
    P = [5, 11]
    T = [3, 1, 8, 7, 4, 2, 5, 2]
    
    processorTime(P, T)

    
if __name__ == '__main__':
    main()