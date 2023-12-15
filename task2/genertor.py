import random
n = random.randint(1, 500)
m = random.randint(1, 500)
res = [[str(0) for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if random.random() > 0.5:
            res[i][j] = str(1)
with open("input.txt", mode="w") as file:
    for line in res:
        file.write(" ".join(line))
        file.write("\n")
