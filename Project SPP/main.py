import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


data = pd.read_csv("student_performance_dataset.csv")

print("Dataset Preview:\n")
print(data.head())


data = data.drop(["Student_ID", "Pass_Fail", "Gender", "Parental_Education_Level"], axis=1)


data["Internet_Access_at_Home"] = data["Internet_Access_at_Home"].map({"Yes": 1, "No": 0})
data["Extracurricular_Activities"] = data["Extracurricular_Activities"].map({"Yes": 1, "No": 0})


X = data.drop("Final_Exam_Score", axis=1)
y = data["Final_Exam_Score"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("\nModel Evaluation:\n")
print("Mean Absolute Error (MAE):", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


plt.scatter(y_test, y_pred)
plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs Predicted Scores")
plt.show()


print("\n=== Test Your Own Input ===")

hours = float(input("Enter Study Hours per Week: "))
attendance = float(input("Enter Attendance Rate (%): "))
previous = float(input("Enter Past Exam Score: "))
internet = int(input("Internet Access (1=Yes, 0=No): "))
extra = int(input("Extracurricular Activities (1=Yes, 0=No): "))

# Create DataFrame (to avoid warning)
input_data = pd.DataFrame(
    [[hours, attendance, previous, internet, extra]],
    columns=X.columns
)

result = model.predict(input_data)

print("\nPredicted Final Exam Score:", round(result[0], 2))