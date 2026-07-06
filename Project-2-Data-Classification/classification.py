# ==========================================
# Project 2 - Data Classification Using AI
# Decode Labs Internship
# Author: Yamini
# ==========================================

# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
data = pd.read_csv("student_data.csv")

print("📊 Dataset Loaded Successfully!\n")
print(data)

# -----------------------------
# Step 2: Separate Features and Target
# -----------------------------
# Features (Input)
X = data[["Hours_Studied", "Attendance"]]

# Target (Output)
y = data["Passed"]

# -----------------------------
# Step 3: Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n✅ Data Split Completed")
print("Training Records :", len(X_train))
print("Testing Records  :", len(X_test))

# -----------------------------
# Step 4: Create Model
# -----------------------------
model = DecisionTreeClassifier(random_state=42)

# -----------------------------
# Step 5: Train Model
# -----------------------------
model.fit(X_train, y_train)

print("\n🤖 Model Trained Successfully!")

# -----------------------------
# Step 6: Test Model
# -----------------------------
predictions = model.predict(X_test)

# -----------------------------
# Step 7: Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, predictions)

print(f"\n🎯 Model Accuracy : {accuracy * 100:.2f}%")

# -----------------------------
# Step 8: Predict New Student
# -----------------------------
print("\n========== Student Prediction ==========")

hours = float(input("Enter Hours Studied: "))
attendance = float(input("Enter Attendance (%): "))

new_student = [[hours, attendance]]

prediction = model.predict(new_student)

print("\nPrediction Result")

if prediction[0] == 1:
    print("✅ The student is likely to PASS.")
else:
    print("❌ The student is likely to FAIL.")

print("\n✨ Thank you for using the Student Performance Predictor!")