import streamlit as st
import plotly.express as px

def hybrid_work_chart(df):
    st.subheader("Hybrid Work Comparison")
    department_chart = df.groupby("Department")["ProductivityScore"].mean().reset_index()
    fig = px.bar(department_chart, x="Department", y="ProductivityScore",
                 title="Department Productivity", color="Department")
    st.plotly_chart(fig)

def gamification_chart(df):
    st.subheader("Gamification & Engagement Insights")
    fig = px.scatter(df, x="Training_Hours", y="ProductivityScore",
                     size="Competency_Score", color="Engagement_Score",
                     hover_data=["Department"],
                     title="Training vs Productivity (Bubble = Competency)")
    st.plotly_chart(fig)

def leaderboard_chart(df):
    st.subheader("Top 5 Engaged Employees")
    leaderboard = df.sort_values("Engagement_Score", ascending=False).head(5)
    st.table(leaderboard[["Employee_ID","Department","Engagement_Score","ProductivityScore"]])

def wellbeing_chart(df):
    st.subheader("Hybrid Work & Well-Being Metrics")

    # Use the WorkLifeBalance column created during data cleaning
    fig = px.histogram(df, x="WorkLifeBalance", nbins=20,
                       title="Distribution of Work-Life Balance Scores",
                       color="Department")
    st.plotly_chart(fig)
