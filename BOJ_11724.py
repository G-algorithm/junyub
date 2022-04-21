import sys
sys.setrecursionlimit(10**9)

n, m = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    matrix[u][v] = matrix[v][u] = 1
#
# for i in range(len(matrix)):
#     print(f'{i} : {matrix[i]}')
# print('\n# # # # # # # # #\n')
answer = []

def dfs(matrix, x, visited):
    ans = []
    if visited[x] == 0:
        visited[x] = 1
        ans.append(x)
    for i in range(1, n+1):
        if matrix[x][i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(matrix, i, visited)
    if len(ans) > 0 and ans not in answer:
        answer.append(ans)
    return answer

visited = [0 for x in range(n+1)]

for i in range(1,n+1):
    result = dfs(matrix, i, visited)
print(len(result))
# print(dfs(matrix,1,visited))