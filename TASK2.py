def isOdd():
	return lambda n: n % 2 != 0


def isPrime():
	return lambda n: n > 1 and all(
		n % i != 0 for i in range(2, int(n ** 0.5) + 1)
	)


def isPalindrome():
	return lambda n: str(n) == str(n)[::-1]


# Example
odd = isOdd()
prime = isPrime()
palindrome = isPalindrome()

n = int(input("Enter a number: "))

print("Odd:", odd(n))
print("Prime:", prime(n))
print("Palindrome:", palindrome(n))
