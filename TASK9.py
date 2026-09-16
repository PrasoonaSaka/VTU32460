nums = list(map(int, input("Enter sorted array elements: ").split()))

k = 1

for i in range(1, len(nums)):
	if nums[i] != nums[k - 1]:
		nums[k] = nums[i]
		k += 1

print("Number of unique elements:", k)
print("Array after removing duplicates:", nums[:k])
