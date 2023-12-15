n, t = list(map(int, input().split()))
people = list(map(int, input().split()))
people.sort()
res = p = 0
while p <= n - 1 and t >= people[p]:
    t -= people[p]
    res += 1
    p += 1
print(res)
