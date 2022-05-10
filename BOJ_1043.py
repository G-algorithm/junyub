import sys

n, m = map(int, sys.stdin.readline().split())
lst = [int(x) for x in sys.stdin.readline().split()]

st = set()
if 0 in lst:
    pass
else:
    st = st | set(lst[1:])

array = []
for i in range(m):
    arr = [int(x) for x in sys.stdin.readline().split()]
    array.append(arr[1:])

while True:
    length = len(st)
    for i in array:
        if set(i) & st:
            st = st | set(i)
    if len(st) == length:
        break

count = 0
for i in array:
    if not set(i) & st:
        count += 1

print(count)