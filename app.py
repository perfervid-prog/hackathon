import streamlit as st
from modules.data_processing import load_data
from modules.visualizations import plot_sales_over_time, plot_category_distribution
import pandas as pd

st.set_page_config(page_title="Shopping Sales Dashboard", layout="wide")

#Sidebar Navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["📊 Dashboard", "🔮 Predictions", "💡 Recommendations", "📝 Insights"])

# Main Section
st.title("Sales Report Analysis")
st.text("Analyze your sales report to gain insights and make informed decisions.")


#File Upload Section
st.subheader("Upload Your Sales Report")
uploaded_file = st.file_uploader("Upload your sales report (format = .csv)", type=["csv"])

clicked = st.button("Generate Report")

if clicked:

    st.divider()

    if uploaded_file:
        data = load_data(uploaded_file)
        
        st.subheader("Dataset summary")
        st.write(f"Total rows: {data.shape[0]}, Total columns: {data.shape[1]}")

        st.subheader("Preview of the data")
        st.write(data.head())

        st.divider()
        
        if options == "📊 Dashboard":
            st.subheader("Sales Dashboard 📊")
            st.write("Explore your uploaded data.")
            plot_sales_over_time(data)
            plot_category_distribution(data)
            
        elif options == "🔮 Predictions":
            st.title("Predictions")
            st.write("Make predictions based on your data.")
            
        elif options == "💡 Recommendations":
            st.title("Personalized Recommendations")
            st.write("Here are some suggestions:")
            
        elif options == "📝 Insights":
            st.title("AI-Generated Insights")
            st.write("Insights based on your data.")

    else:
        st.write("Please upload a dataset to proceed.")