class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


n = int(input("Enter number of persons: "))
p = []

for i in range(n):
	name = input("Enter name: ")
	age = int(input("Enter age: "))
	p.append(Person(name, age))

# Sort by name
p.sort(key=lambda x: x.name)
print("\nSorted:")
for x in p:
	print(x.name, x.age)

# Filter by age
limit = int(input("Enter age limit: "))
print("\nOlder persons:")
for x in p:
	if x.age > limit:
		print(x.name, x.age)

# Uppercase names
print("\nUppercase names:")
for x in p:
	print(x.name.upper())
