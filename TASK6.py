N = int(input("Enter number of sales records: "))

sales = {}
order = []

for i in range(N):
	category, item, amount = input("Enter category, item name and sales amount: ").split()
	amount = int(amount)

	if category not in sales:
		sales[category] = {
			"total": 0,
			"max_amount": amount,
			"max_item": item
		}
		order.append(category)

	sales[category]["total"] += amount

	if amount > sales[category]["max_amount"]:
		sales[category]["max_amount"] = amount
		sales[category]["max_item"] = item

for category in order:
	print(category, sales[category]["total"], sales[category]["max_item"])
