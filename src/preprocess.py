# src/preprocess.py
import pandas as pd

def create_input_df(student_data):
    """
    Convert raw input dict to DataFrame with correct column order.
    """
    expected_columns = [
        'College_Name', 'Stream', 'Year_of_Study', 'AI_Tools_Used',
        'Daily_Usage_Hours', 'Use_Cases', 'Trust_in_AI_Tools',
        'Do_Professors_Allow_Use', 'Preferred_AI_Tool', 'Awareness_Level',
        'Willing_to_Pay_for_Access', 'State', 'Device_Used', 'Internet_Access'
    ]
    return pd.DataFrame([student_data], columns=expected_columns)