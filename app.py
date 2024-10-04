import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data = pd.read_csv("ProductInfo.csv")  # Replace with your actual dataset

# Title and description
st.title("Demand Forecasting")
st.write("Demand Overview for Top 10 Products")

# Sample dropdown for stock codes or product codes
stock_codes = data['StockCode'].unique()
selected_stock = st.selectbox("Select a Stock Code:", stock_codes)

# Filter data for selected stock code
filtered_data = data[data['StockCode'] == selected_stock]

# Generate dummy data for the forecast and actual values
# Replace this with your actual forecasting model's output
dates = pd.date_range(start='2023-01-01', periods=len(filtered_data), freq='W')
actual_demand = np.random.randint(50, 150, size=len(filtered_data))  # Replace with actual demand data
predicted_demand_train = actual_demand + np.random.normal(0, 10, size=len(filtered_data))  # Replace with your model's predictions
predicted_demand_test = actual_demand + np.random.normal(0, 15, size=len(filtered_data))  # Replace with your test predictions

# Line chart: Actual vs Predicted Demand
st.write(f"Demand Overview for {selected_stock}")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, actual_demand, label='Actual Demand', color='blue', marker='o')
ax.plot(dates, predicted_demand_train, label='Train Predicted Demand', color='green', linestyle='--', marker='x')
ax.plot(dates, predicted_demand_test, label='Test Predicted Demand', color='red', linestyle='--', marker='x')
ax.legend()
ax.set_xlabel("Date")
ax.set_ylabel("Demand")
st.pyplot(fig)

# Histograms for error distributions
train_error = actual_demand - predicted_demand_train
test_error = actual_demand - predicted_demand_test

# Training Error Distribution
st.write("Training Error Distribution")
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(train_error, bins=20, color='green', alpha=0.7)
ax.set_xlabel("Error")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Testing Error Distribution
st.write("Testing Error Distribution")
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(test_error, bins=20, color='red', alpha=0.7)
ax.set_xlabel("Error")
ax.set_ylabel("Frequency")
st.pyplot(fig)
