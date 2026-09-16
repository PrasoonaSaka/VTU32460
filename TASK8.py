n = int(input())

nums = list(map(int, input().split()))

k = int(input())

result = []

for i in range(n - k + 1):
    window = nums[i:i + k]
    result.append(max(window))

print(*result)

