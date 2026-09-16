
pattern = input("Enter the pattern: ")
text = input("Enter the text: ")

m = len(pattern)
count = 0

for i in range(len(text) - m + 1):
	window = text[i:i + m]

	if sorted(window) == sorted(pattern):
		count += 1

print("Count of anagram substrings:", count)
