import sys
n = int(sys.stdin.readline())
lst = [int(x) for x in (sys.stdin.readline().split())]
lst = sorted(lst)

lst2 = [0 for x in range(n)]

for i in range(n):
    if i == 0:
        lst2[i] = lst[i]
    else:
        lst2[i] = lst2[i-1] + lst[i]

print(sum(lst2))