matrix = []
with open("input.txt") as file:
    for line in file.readlines():
        matrix.append(list(map(int, line.split())))


def dfs(x, y, used, graph, res):
    if not (0 <= x < len(graph) and 0 <= y < len(graph[0])):
        return False
    if used[x][y] or graph[x][y] == 0:
        return False
    used[x][y] = True
    graph[x][y] += res
    dfs(x + 1, y, used, graph, res)
    dfs(x - 1, y, used, graph, res)
    dfs(x, y + 1, used, graph, res)
    dfs(x, y - 1, used, graph, res)
    return True

used = [[False for _ in range(len(matrix[i]))] for i in range(len(matrix))]
res = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        res += dfs(i, j, used, matrix, res)

print(res)
for rows in matrix:
    print(*rows, sep=" ")
if len(matrix) == 0:
    print()
