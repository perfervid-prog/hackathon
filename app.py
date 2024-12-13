import streamlit as st
import pandas as pd
from modules.data_processing import load_data, preprocess_data
from modules.visualizations import plot_sales_over_time, plot_category_distribution

st.set_page_config(page_title="Shopping Sales Dashboard", layout="wide")

st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Dashboard", "📊 Predictions", "⭐ Recommendations", "💡 Insights"])

st.title("Sales Report Analysis")
st.text("Analyze your sales report to gain insights and make informed decisions.")

# Initialize Session State
if 'start_date' not in st.session_state:
   st.session_state.start_date = pd.to_datetime('2023-01-01')
if 'end_date' not in st.session_state:
   st.session_state.end_date = pd.to_datetime('2024-01-01')
if 'data' not in st.session_state:
  st.session_state.data = None
if 'uploaded_file_key' not in st.session_state:
    st.session_state.uploaded_file_key = None
if 'report_generated' not in st.session_state:
    st.session_state.report_generated = False  # Track if report is generated
    
st.subheader("Upload Your Sales Report")
uploaded_file = st.file_uploader("Upload your sales report (format = .csv)", type=["csv"], key="file_uploader")

if uploaded_file is not None and st.session_state.uploaded_file_key != uploaded_file.name:

    st.session_state.uploaded_file_key = uploaded_file.name
    
    data = load_data(uploaded_file)
    required_columns = ['Transaction ID', 'Date', 'Customer ID', 'Gender', 'Age', 'Product Category', 'Quantity', 'Price per Unit', 'Total Amount']
    missing_columns = [col for col in required_columns if col not in data.columns]

    if missing_columns:

        st.error(f"Missing columns: {', '.join(missing_columns)}")

    else:
      
      st.session_state.data = preprocess_data(data)




elif uploaded_file is None:
  st.session_state.data = None
  st.session_state.uploaded_file_key = None

clicked = st.button("Generate Report")

if clicked and st.session_state.data is not None:
    st.session_state.report_generated = True
    data = st.session_state.data
    st.divider()
    st.subheader("Dataset summary")
    st.write("Rows:", data.shape[0])
    st.write("Columns:", data.shape[1])
    
    st.subheader("Preview of the data")
    st.dataframe(data.head(), use_container_width=True)

    st.divider()

if options == "Dashboard" and st.session_state.report_generated and st.session_state.data is not None:
    st.subheader("Sales Dashboard")
    st.write("Explore your uploaded data.")
    if st.session_state.data is not None:
      col1, col2 = st.columns(2)
      with col1:
        start_date_input = st.date_input("Start Date", value=st.session_state.start_date, format="YYYY-MM-DD")
      with col2:
        end_date_input = st.date_input("End Date", value=st.session_state.end_date, format="YYYY-MM-DD")

      if start_date_input != st.session_state.start_date or end_date_input != st.session_state.end_date:
            st.session_state.start_date = start_date_input
            st.session_state.end_date = end_date_input
            
      filtered_data = st.session_state.data[(st.session_state.data['Date'] >= st.session_state.start_date) & (st.session_state.data['Date'] <= st.session_state.end_date)]

      st.write("Date range selected from: ", st.session_state.start_date, " to: ", st.session_state.end_date)
      plot_sales_over_time(filtered_data)
      plot_category_distribution(filtered_data)

elif options == "📊 Predictions":
    st.title("Predictions")
    st.write("Make predictions based on your data.")
elif options == "⭐ Recommendations":
    st.title("Personalized Recommendations")
    st.write("Here are some suggestions:")
elif options == "💡 Insights":
    st.title("AI-Generated Insights")
    st.write("Insights based on your data.")