def hanoi(n, source, helper, target):
    if n > 0:
        hanoi(n - 1, source, target, helper)    #moving tower of size n - 1 to helper:
        #moving disk from source peg to target peg
        if source:    #checks whether source is empty or not
            target.append(source.pop())    #appends the last disc from source, to target
        hanoi(n - 1, helper, source, target)    #moving tower of size n-1 from helper to target
        
source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print(source, helper, target)
