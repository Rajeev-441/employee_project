import streamlit as st

def bias_detection(df):
    st.subheader("Bias Detection")

    # Example: check attrition risk by Department
    bias_check = df.groupby("Department")["Attrition_Risk"].mean().reset_index()
    st.table(bias_check)

    # Optional: also check by Performance Category
    perf_bias = df.groupby("Performance_Category")["Attrition_Risk"].mean().reset_index()
    st.table(perf_bias)
