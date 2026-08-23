from datetime import datetime

events = []

n = int(input("Enter number of events: "))

for i in range(n):
	name = input("Enter event name: ")
	date = input("Enter date (YYYY-MM-DD): ")
	date = datetime.strptime(date, "%Y-%m-%d")
	events.append((name, date))

# Sort by date
events.sort(key=lambda x: x[1])

print("\nSorted events:")
for name, date in events:
	print(name, date.strftime("%Y-%m-%d"))

# Earliest and latest
print("\nEarliest:", events[0][0])
print("Latest:", events[-1][0])

# Find events by month
month = int(input("\nEnter month: "))

print("Events in month", month, ":")
for name, date in events:
	if date.month == month:
		print(name, date.strftime("%Y-%m-%d"))
