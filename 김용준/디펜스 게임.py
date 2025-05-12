import heapq

def solution(n, k, enemy):
    ks = []
    rounds = len(enemy)
    
    for i in range(rounds):
        current = enemy[i]
        
        if len(ks) < k:
            heapq.heappush(ks, current)
        elif k > 0 and ks and current > ks[0]:
            n -= heapq.heappop(ks)
            heapq.heappush(ks, current)
        else:
            n -= current
        
        if n < 0:
            return i
    
    return rounds
