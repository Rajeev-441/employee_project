import os
import pandas as pd

def clean_data(path="data/Enterprise_HRM_Categorical_Target.csv"):
    # Load dataset
    df = pd.read_csv(path)

    # Handle missing values
    df = df.fillna("Unknown")

    # Encode categorical target (Performance Category)
    df['Performance_Category'] = df['Performance_Category'].map({
        'Low': 0, 'Moderate': 1, 'High': 2
    })

    # Derived metrics
    df['ProductivityScore'] = df['Productivity_Score']

    # Work-life balance example: based on absenteeism and workload
    df['WorkLifeBalance'] = (10 - (df['Absenteeism_Rate'] + df['Workload_Index'])).clip(lower=0)

    # Save cleaned dataset
    output_path = os.path.join("data", "cleaned_data.csv")
    df.to_csv(output_path, index=False)

    print(f"✅ Cleaned dataset saved to {output_path} with {len(df)} rows.")
    return df

if __name__ == "__main__":
    clean_data()
