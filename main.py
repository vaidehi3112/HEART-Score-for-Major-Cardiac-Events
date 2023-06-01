import streamlit as st

# Set app title and header
st.set_page_config(page_title="HEART Score Calculator", page_icon=":pill:", layout="wide")
st.title("HEART Score Calculator")

# Get input values from user
history_selected = st.selectbox("History", ("Slightly suspicious", "Moderately suspicious", "Highly suspicious"))
history_labels = ["Slightly suspicious", "Moderately suspicious", "Highly suspicious"]
history_values = [0, 1, 2]
history = history_values[history_labels.index(history_selected)]

ecg_selected = st.selectbox("ECG", ("Normal", "Non-specific repolarization", "Significant ST-depression"))
ecg_labels = ["Normal", "Non-specific repolarization", "Significant ST-depression"]
ecg_values = [0, 1, 2]
ecg = ecg_values[ecg_labels.index(ecg_selected)]

age = st.number_input("Age", value=0, min_value=0)

# Determine age bucket based on the provided criteria
if age < 45:
    age_bucket = 0
elif age <= 64:
    age_bucket = 1
else:
    age_bucket = 2

risk_selected = st.selectbox("Risk Factors", ("None", "1-2 risk factors", ">=3 risk factors"))
risk_labels = ["None", "1-2 risk factors", ">=3 risk factors"]
risk_values = [0, 1, 2]
risk = risk_values[risk_labels.index(risk_selected)]

troponin_options = ["≤ Normal Limit", "1-3× Normal Limit", "> 3× Normal Limit"]
troponin_selected = st.selectbox("Troponin", troponin_options)
troponin_values = [0, 1, 2]
troponin = troponin_values[troponin_options.index(troponin_selected)]

heart_score = history + ecg + age_bucket + risk + troponin

# Display the HEART Score classification
classification = ""
if heart_score <= 3:
    classification = "Low Score: 0-3 points\nRisk of MACE of 0.9-1.7%."
elif heart_score <= 6:
    classification = "Moderate Score: 4-6 points\nRisk of MACE of 12-16.6%."
else:
    classification = "High Score: 7+ points\nRisk of MACE of 50-65%."

st.subheader("HEART Score Calculation Result")
st.markdown(classification.split("\n")[0])
st.markdown(classification.split("\n")[1])
