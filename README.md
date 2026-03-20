# Student Performance AI Predictor

A machine learning-based tool that predicts the impact of AI tool usage on student academic performance. This project helps educators and students understand how AI adoption affects grades across different usage patterns, demographics, and educational contexts.

## Overview

This predictive system analyzes 14 key factors including college name, study stream, AI tool preferences, usage hours, and institutional policies to forecast the impact on student grades. Built using Random Forest regression, the model provides actionable insights into AI-assisted learning outcomes.

## Features

- **Interactive CLI Interface**: Easy-to-use command-line tool for predictions
- **Comprehensive Analysis**: Evaluates 14 distinct student and AI usage parameters
- **Trained Model**: Pre-trained Random Forest model with strong predictive accuracy
- **Real-time Predictions**: Instant grade impact forecasts
- **Visual Feedback**: Color-coded results indicating positive, neutral, or negative impacts

## Project Structure

```
Student-performance-ai/
├── app.py                  # Main CLI application
├── train_model.py          # Model training script
├── requirements.txt        # Python dependencies
├── data/
│   └── Students.xlsx       # Training dataset
├── models/
│   └── student_performance_model.pkl  # Trained model
└── src/
    ├── predict.py          # Prediction logic
    └── preprocess.py       # Data preprocessing utilities
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Student-performance-ai.git
   cd Student-performance-ai
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Making Predictions

Run the interactive CLI application:

```bash
python app.py
```

You'll be prompted to enter student details. Press Enter to use default values:

```
College Name: National Institute of Technology
Stream: Engineering
Year of Study: 2
AI Tools Used: ChatGPT, Copilot
Daily Usage Hours: 2.5
Use Cases: Assignments, Coding Help
Trust in AI Tools (1-5): 4
Do Professors Allow Use? Yes
Preferred AI Tool: ChatGPT
Awareness Level (1-10): 8
Willing to Pay? No
State: Karnataka
Device Used: Laptop
Internet Access: High
```

**Sample Output:**
```
✅ Predicted Impact on Grades: 3.45
🟢 Strong positive impact expected!
```

### Training the Model

To retrain the model with updated data:

```bash
python train_model.py
```

This will:
- Load data from `data/Students.xlsx`
- Preprocess features and handle categorical variables
- Train a Random Forest regressor
- Evaluate model performance (MAE and R² scores)
- Save the trained model to `models/student_performance_model.pkl`

## Input Features

The model analyzes the following 14 features:

| Feature | Type | Description | Example Values |
|---------|------|-------------|----------------|
| College_Name | Text | Institution name | "National Institute of Technology" |
| Stream | Text | Academic discipline | "Engineering", "Arts", "Commerce" |
| Year_of_Study | Numeric | Current year (1-4) | 1, 2, 3, 4 |
| AI_Tools_Used | Text | Tools being utilized | "ChatGPT, Copilot" |
| Daily_Usage_Hours | Numeric | Hours per day (0.5-5) | 2.5 |
| Use_Cases | Text | Application scenarios | "Assignments, Exam Prep" |
| Trust_in_AI_Tools | Numeric | Confidence level (1-5) | 4 |
| Do_Professors_Allow_Use | Text | Institutional policy | "Yes", "No" |
| Preferred_AI_Tool | Text | Most-used tool | "ChatGPT", "Gemini" |
| Awareness_Level | Numeric | AI literacy (1-10) | 7 |
| Willing_to_Pay_for_Access | Text | Payment readiness | "Yes", "No" |
| State | Text | Geographic location | "Karnataka", "Tamil Nadu" |
| Device_Used | Text | Primary device | "Laptop", "Mobile", "Tablet" |
| Internet_Access | Text | Connection quality | "Poor", "Medium", "High" |

## Model Details

- **Algorithm**: Random Forest Regressor
- **Estimators**: 200 trees
- **Max Depth**: 15
- **Features**: 14 input variables
- **Target**: Impact_on_Grades (continuous scale)
- **Preprocessing**: One-Hot Encoding for categorical variables

### Performance Metrics

The model is evaluated using:
- **Mean Absolute Error (MAE)**: Measures average prediction error
- **R² Score**: Indicates model fit quality (closer to 1.0 is better)

## Output Interpretation

The model outputs a numeric score representing the predicted impact on grades:

- **> +2.0**: Strong positive impact expected (🟢)
- **-2.0 to +2.0**: Moderate or neutral impact (🟡)
- **< -2.0**: Risk of negative academic impact (🔴)

## Requirements

- Python 3.8+
- pandas 2.0.3
- numpy 1.24.3
- scikit-learn 1.3.0
- openpyxl 3.1.2
- joblib 1.3.2

## Dataset

The training data (`data/Students.xlsx`) should contain the 14 feature columns plus the target column `Impact_on_Grades`. Each row represents a student's profile and observed academic outcome.

## Use Cases

- **Academic Advisors**: Identify students at risk from improper AI usage
- **Institutions**: Develop evidence-based AI adoption policies
- **Students**: Optimize AI tool usage for better academic outcomes
- **Researchers**: Study correlations between AI usage patterns and performance

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- Dataset contributors and student participants
- Scikit-learn community for machine learning tools
- Educational institutions supporting AI research



---

**Note**: This tool provides predictive insights and should be used alongside professional academic counseling. Individual results may vary based on learning styles, subject difficulty, and personal factors not captured in the model.
