# src/predict.py
import joblib
from src.preprocess import create_input_df

def predict_performance(student_data):
    """
    Predict Impact_on_Grades for a single student.
    
    Parameters:
        student_data (dict): Must contain all 14 feature keys.
    
    Returns:
        float: Predicted impact score (e.g., -2.3 or +4.1)
    """
    model = joblib.load("models/student_performance_model.pkl")
    input_df = create_input_df(student_data)
    prediction = model.predict(input_df)[0]
    return float(prediction)