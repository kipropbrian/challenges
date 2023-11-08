# get list of contiguous integers sum up to 2
def solution(l, t):
    total = 0
    start = 0
    
    for end, val in enumerate(l):
        total += val

        while(total > t):
            total -= l[start]
            start +=1
        
        if(total == t):
            return [start, end]
    return [-1, -1]

print(solution([4, 3, 10, 2, 8], 12))
