def solution(n, computers):
    visited = [False] * n  

    def dfs(x):
        visited[x] = True
        for i, v in enumerate(computers[x]):
            if v and not visited[i]:
                dfs(i)

    answer = 0
    for i in range(n):
        if not visited[i]:  
            dfs(i)
            answer += 1

    return answer