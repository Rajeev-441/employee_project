import streamlit as st
import plotly.express as px

def detect_anomalies(df):
    st.subheader("Anomaly Detection - Productivity Drops")
    fig = px.scatter(df, x="Training_Hours", y="ProductivityScore",
                     color=df["ProductivityScore"] < 65,
                     title="Productivity Anomalies (Training Hours)")
    st.plotly_chart(fig)

    anomalies = df[df["ProductivityScore"] < 65][["Employee_ID","Department","ProductivityScore","Training_Hours"]]
    st.table(anomalies)
