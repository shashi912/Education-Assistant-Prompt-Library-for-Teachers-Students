# src/inference.py
import joblib
import pandas as pd
import os

MODEL_PATH = os.path.join("outputs", "rf_usefulness_model.joblib")

def load_model(path=MODEL_PATH):
    return joblib.load(path)

def make_example():
    return pd.DataFrame([{
        "prompt_text": "Create a 5-question quiz about fractions for grade 4",
        "prompt_type": "quiz",
        "subject": "Math",
        "grade": 4,
        "audience": "student",
        "prompt_length": len("Create a 5-question quiz about fractions for grade 4"),
        "engagement_score": 0.60
    }])

if __name__ == "__main__":
    model = load_model()
    examples = make_example()
    preds = model.predict(examples)
    print("Predicted usefulness:", preds[0])
