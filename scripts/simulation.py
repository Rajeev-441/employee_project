import streamlit as st

def simulate_intervention(df):
    st.subheader("Scenario Simulation")

    meetings = st.slider("Reduce Meetings (%)", 0, 50, 10)
    training = st.slider("Increase Training Hours (%)", 0, 50, 10)

    df["Simulated_Productivity"] = df["ProductivityScore"] + (training*0.1) - (meetings*0.05)
    st.line_chart(df[["ProductivityScore","Simulated_Productivity"]])
