import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv("student_performance_dataset.csv")

data = data.drop(["Student_ID", "Pass_Fail", "Gender", "Parental_Education_Level"], axis=1)

data["Internet_Access_at_Home"] = data["Internet_Access_at_Home"].map({"Yes": 1, "No": 0})
data["Extracurricular_Activities"] = data["Extracurricular_Activities"].map({"Yes": 1, "No": 0})


X = data.drop("Final_Exam_Score", axis=1)
y = data["Final_Exam_Score"]

model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
model.fit(X, y)


st.title("🎓 Student Performance Prediction")

st.write("Enter student details:")

hours = st.slider("Study Hours per Week", 0, 50, 20)
attendance = st.slider("Attendance (%)", 0, 100, 75)
previous = st.slider("Past Exam Score", 0, 100, 70)
internet = st.selectbox("Internet Access at Home", ["Yes", "No"])
extra = st.selectbox("Extracurricular Activities", ["Yes", "No"])


internet = 1 if internet == "Yes" else 0
extra = 1 if extra == "Yes" else 0


if st.button("Predict Score"):
    input_data = pd.DataFrame(
        [[hours, attendance, previous, internet, extra]],
        columns=X.columns
    )

    result = model.predict(input_data)

    st.success(f"Predicted Final Exam Score: {result[0]:.2f}")

    # Grade
    if result[0] >= 80:
        st.success("Grade: A 🎉")
    elif result[0] >= 60:
        st.info("Grade: B 👍")
    else:
        st.warning("Grade: C ⚠️")                                   