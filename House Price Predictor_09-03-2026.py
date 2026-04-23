# House Price Predictor (Simple Linear Regression)

from sklearn.linear_model import LinearRegression

# Dataset
size = [[500], [1000], [1500], [2000]]   # House size (sq ft)
price = [100, 200, 300, 400]             # Price

# Create model
model = LinearRegression()

# Train model
model.fit(size, price)

# Predict price for new house
new_size = [[1200]]
predicted_price = model.predict(new_size)

print("Predicted Price:", predicted_price)