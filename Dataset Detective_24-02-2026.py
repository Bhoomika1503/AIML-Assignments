# Dataset Detective (Simple Version)

data = [10, 20, 30, 40, None]

print("Data:", data)

# Find highest value
print("Highest value:", max([x for x in data if x is not None]))

# Count missing values
missing = data.count(None)
print("Missing values:", missing)