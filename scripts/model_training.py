import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "cleaned_data.csv"
MODEL_PATH = PROJECT_ROOT / "models" / "attrition_model.pkl"

df = pd.read_csv(DATA_PATH)

X = df[["Training_Hours", "Engagement_Score", "Competency_Score"]]
y = df["Performance_Category"]  # 0 = low, 1 = moderate, 2 = high

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

MODEL_PATH.parent.mkdir(exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")
