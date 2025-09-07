import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved model (Preprocess + RandomForest)
Preprocess, model = joblib.load("model.pkl")

st.header("🎬 YouTube Content Monetization Modeler")
st.write("Predict **YouTube Ad Revenue** based on video performance and other details.")

# Sidebar for user inputs
st.sidebar.header("Enter Video Details")

# Input fields
views = st.sidebar.number_input("Views", min_value=0, max_value=10000000, value=10000, step=100)
likes = st.sidebar.number_input("Likes", min_value=0, value=500, step=10)
comments = st.sidebar.number_input("Comments", min_value=0, value=50, step=1)
watch_time_minutes = st.sidebar.number_input("Watch Time (minutes)", min_value=0, value=1000, step=10)
video_length_minutes = st.sidebar.number_input("Video Length (minutes)", min_value=1, value=10, step=1)
subscribers = st.sidebar.number_input("Channel Subscribers", min_value=0, max_value=10000000, value=100000, step=1000)

category = st.sidebar.selectbox("Category", ["Gaming", "Music", "Education", "Vlog", "Tech"])
device = st.sidebar.selectbox("Device", ["Mobile", "Desktop", "Tablet", "TV"])
country = st.sidebar.selectbox("Country", ["US", "IN", "UK", "CA", "Others"])

# Feature engineering (same as training pipeline)
engagement_rate = (likes + comments) / views if views > 0 else 0
watch_time_ratio = watch_time_minutes / video_length_minutes if video_length_minutes > 0 else 0
views_per_min = views / video_length_minutes if video_length_minutes > 0 else 0

# Create DataFrame for prediction
input_df = pd.DataFrame({
    "views": [views],
    "likes": [likes],
    "comments": [comments],
    "watch_time_minutes": [watch_time_minutes],
    "video_length_minutes": [video_length_minutes],
    "subscribers": [subscribers],
    "category": [category],
    "device": [device],
    "country": [country],
    "engagement_rate": [engagement_rate],
    "watch_time_ratio": [watch_time_ratio],
    "views_per_min": [views_per_min]
})

# Preprocess input
X_transformed = Preprocess.transform(input_df)

# Predict
if st.sidebar.button("Predict Revenue"):
    if views == 0 or video_length_minutes == 0:
        st.warning("Views and Video Length must be greater than 0 for a valid prediction.")
    else:
        prediction = model.predict(X_transformed)[0]
        st.success(f"💰 Estimated Ad Revenue: **${prediction:,.2f} USD**")

# ---- Input Summary ----
        st.subheader("🔎 Input Summary")
        st.dataframe(input_df.round(2))

        # ---- Simple Metrics Visualization ----
        st.subheader("📊 Key Metrics Visualization")
        metrics_df = input_df[["views", "likes", "comments", "subscribers"]].T
        metrics_df.columns = ["Count"]
        st.bar_chart(metrics_df)
