def solution(n, w, num):
    stacks = [[] for _ in range(w)]
    
    current = 1
    row = 0
    
    while current <= n:
        # 짝수 행은 왼쪽에서 오른쪽으로
        if row % 2 == 0:
            for col in range(w):
                stacks[col].append(current)
                current += 1
                if current > n:
                    break
        # 홀수 행은 오른쪽에서 왼쪽으로
        else:
            for col in range(w-1, -1, -1):
                stacks[col].append(current)
                current += 1
                if current > n:
                    break
        
        # 다음 행으로 이동
        row += 1
    
    for stack_idx, stack in enumerate(stacks):
        if num in stack:
            num_idx = stack.index(num)
            return len(stack) - num_idx
