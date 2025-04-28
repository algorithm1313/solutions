def dfs(n, computers, idx, visited):
    visited[idx] = True
    for next in range(n):
        if not visited[next] and computers[idx][next] == 1:
            dfs(n,computers, next, visited)


def solution(n, computers):
    visited = [False] * n
    answer = 0

    for idx in range(n):
        if visited[idx] == False:
            dfs(n,computers,idx,visited)
            answer += 1
    return answer