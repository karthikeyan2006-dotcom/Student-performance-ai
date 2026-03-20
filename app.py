# app.py
from src.predict import predict_performance

def main():
    print("🎓 Student Performance AI Predictor")
    print("Enter student details (press Enter for defaults where noted):\n")

    student = {
        "College_Name": input("College Name: ") or "National Institute of Technology",
        "Stream": input("Stream (e.g., Engineering, Arts): ") or "Engineering",
        "Year_of_Study": int(input("Year of Study (1-4): ") or 2),
        "AI_Tools_Used": input("AI Tools Used (comma-separated, e.g., ChatGPT, Copilot): ") or "ChatGPT",
        "Daily_Usage_Hours": float(input("Daily Usage Hours (0.5–5): ") or 2.0),
        "Use_Cases": input("Use Cases (comma-separated, e.g., Exam Prep, Coding Help): ") or "Assignments, Coding Help",
        "Trust_in_AI_Tools": int(input("Trust in AI Tools (1–5): ") or 3),
        "Do_Professors_Allow_Use": input("Do Professors Allow Use? (Yes/No): ") or "Yes",
        "Preferred_AI_Tool": input("Preferred AI Tool: ") or "ChatGPT",
        "Awareness_Level": int(input("Awareness Level (1–10): ") or 7),
        "Willing_to_Pay_for_Access": input("Willing to Pay? (Yes/No): ") or "No",
        "State": input("State (e.g., Tamil Nadu, Delhi): ") or "Karnataka",
        "Device_Used": input("Device Used (Laptop/Mobile/Tablet): ") or "Laptop",
        "Internet_Access": input("Internet Access (Poor/Medium/High): ") or "Medium"
    }

    try:
        impact = predict_performance(student)
        print(f"\n✅ Predicted Impact on Grades: {impact:.2f}")
        if impact > 2:
            print("🟢 Strong positive impact expected!")
        elif impact < -2:
            print("🔴 Risk of negative academic impact.")
        else:
            print("🟡 Moderate or neutral impact.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()