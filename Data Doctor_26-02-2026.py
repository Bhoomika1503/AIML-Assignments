# Data Doctor

data = ["Apple", "Banana", "", "Apple", "Mango", "banana"]

# Remove missing values
data = [x for x in data if x != ""]

# Remove duplicates
data = list(set(data))

# Standardize text (lowercase)
data = [x.lower() for x in data]

print("Cleaned Data:", data)