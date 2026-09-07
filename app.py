import streamlit as st
import pandas as pd
import joblib
from charts import hybrid_work_chart, gamification_chart, wellbeing_chart, leaderboard_chart
from anomaly import detect_anomalies
from scripts.bias_detection import bias_detection
from scripts.simulation import simulate_intervention

df = pd.read_csv("data/cleaned_data.csv")

st.title("📊 Workforce Analytics Dashboard")

# Metrics
st.metric("Average Productivity", round(df['ProductivityScore'].mean(),2))
st.metric("Average Engagement", round(df['Engagement_Score'].mean(),2))

# Charts
hybrid_work_chart(df)
gamification_chart(df)
leaderboard_chart(df)
wellbeing_chart(df)

# Anomaly detection
detect_anomalies(df)

# Attrition predictions
model = joblib.load("models/attrition_model.pkl")
df["Attrition_Risk"] = model.predict_proba(df[["Training_Hours","Engagement_Score","Competency_Score"]])[:,1]
st.subheader("Attrition Risk Predictions")
st.table(df[["Employee_ID","Department","Attrition_Risk"]].head(10))



# Bias detection
bias_detection(df)

# Scenario simulation
simulate_intervention(df)
