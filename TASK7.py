n = int(input())
arr = list(map(int, input().split()))
prefix = []
sum_val = 0

for x in arr:
    sum_val += x
    prefix.append(sum_val)

print(*prefix)
