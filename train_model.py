# train_model.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# Ensure models directory exists
os.makedirs("models", exist_ok=True)

# Load data
df = pd.read_excel("data/Students.xlsx")

# Drop Student_Name (leakage risk)
df = df.drop(columns=["Student_Name"], errors="ignore")

# Remove rows with missing target
df = df.dropna(subset=["Impact_on_Grades"])

# Define features and target
features = [
    'College_Name', 'Stream', 'Year_of_Study', 'AI_Tools_Used',
    'Daily_Usage_Hours', 'Use_Cases', 'Trust_in_AI_Tools',
    'Do_Professors_Allow_Use', 'Preferred_AI_Tool', 'Awareness_Level',
    'Willing_to_Pay_for_Access', 'State', 'Device_Used', 'Internet_Access'
]
X = df[features]
y = df['Impact_on_Grades']

# Identify column types
categorical_features = X.select_dtypes(include=['object']).columns.tolist()
numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()

# Preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
    ]
)

# Pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(
        n_estimators=200,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    ))
])

# Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"✅ Model Trained!\nMAE: {mae:.3f} | R²: {r2:.3f}")

# Save model
joblib.dump(pipeline, "models/student_performance_model.pkl")
print("📦 Model saved to models/student_performance_model.pkl")