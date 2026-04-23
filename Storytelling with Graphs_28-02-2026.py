import matplotlib.pyplot as plt

data = [10, 20, 30, 40, 50]

# Bar Chart
plt.bar(["A","B","C","D","E"], data)
plt.title("Bar Chart")
plt.show()

# Pie Chart
plt.pie(data, labels=["A","B","C","D","E"], autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()

# Histogram
plt.hist(data)
plt.title("Histogram")
plt.show()