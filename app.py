import streamlit as st
import pandas as pd
import numpy as np
import joblib


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Electricity Theft Detection",
    page_icon="⚡",
    layout="wide"
)


# --------------------------------------------------
# LOAD MODEL AND FEATURES
# --------------------------------------------------

model = joblib.load("random_forest_theft_model.pkl")
energy_features = joblib.load("energy_features.pkl")


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("⚡ Electricity Theft Detection")

# about the applictaion
with st.expander("ℹ️ About this application"):
    st.write("""
    This application detects possible electricity theft using a
    Random Forest machine learning model.

    The model analyses electricity consumption over 24 consecutive
    hours using 8 energy-related features. These patterns are
    classified as either:
     - Normal electricity consumption 
     - Electricity theft.

    To make a prediction, enter the consumption values for all
    24 hours and click "Detect Electricity Theft".
    """)

st.write(
    "This application uses a Random Forest model to classify "
    "24-hour electricity consumption patterns as Normal or Theft."
)

st.info(
    "Enter electricity consumption data for 24 consecutive hours "
    "using the 8 energy features."
)


# --------------------------------------------------
# FEATURE NAMES
# --------------------------------------------------

feature_names = list(energy_features)


# --------------------------------------------------
# INPUT DATA
# --------------------------------------------------

st.header("24-Hour Electricity Consumption")

input_data = pd.DataFrame(
    0.0,
    index=range(1, 25),
    columns=feature_names
)

input_data.index.name = "Hour"


edited_data = st.data_editor(
    input_data,
    use_container_width=True,
    num_rows="fixed"
)


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if st.button("🔍 Detect Electricity Theft", type="primary"):

    # Convert input to NumPy array
    sequence = edited_data.values.astype(float)

    # Check that the input is exactly 24 × 8
    if sequence.shape != (24, 8):
        st.error(
            "The model requires exactly 24 hours and 8 features."
        )
        st.stop()

    # Check for missing values
    if np.isnan(sequence).any():
        st.error("Please fill in all values before making a prediction.")
        st.stop()

    # Flatten 24 × 8 into 192 features
    sequence_flattened = sequence.reshape(1, -1)

    # Make prediction
    prediction = model.predict(sequence_flattened)[0]

    # Convert prediction to label
    if prediction == 1 or prediction == "Theft":
        prediction_label = "Theft"
    else:
        prediction_label = "Normal"


    # --------------------------------------------------
    # DISPLAY RESULT
    # --------------------------------------------------

    st.header("Prediction")

    if prediction_label == "Theft":
        st.error("⚠️ Electricity Theft Detected")

    else:
        st.success("✅ Normal Electricity Consumption")


    # --------------------------------------------------
    # THEFT PROBABILITY
    # --------------------------------------------------

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(
            sequence_flattened
        )[0]

        classes = model.classes_

        theft_probability = None

        for class_value, probability in zip(
            classes,
            probabilities
        ):

            if class_value == 1 or class_value == "Theft":
                theft_probability = probability
                break

        if theft_probability is not None:

            st.metric(
                "Theft Probability",
                f"{theft_probability * 100:.2f}%"
            )


    # --------------------------------------------------
    # INPUT SUMMARY
    # --------------------------------------------------

    st.subheader("24-Hour Consumption Summary")

    summary = pd.DataFrame({
        "Feature": feature_names,
        "Average": sequence.mean(axis=0),
        "Minimum": sequence.min(axis=0),
        "Maximum": sequence.max(axis=0)
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )