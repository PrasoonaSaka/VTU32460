numbers = list(map(int, input("Enter numbers: ").split()))
unique = sorted(set(numbers), reverse=True)

if len(unique) < 2:
	print(-1)
else:
	print("Second highest:", unique[1])
