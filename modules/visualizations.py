import plotly.express as px
import pandas as pd
import streamlit as st


def plot_category_distribution(data):
    """Plot sales distribution by category."""
    fig = px.bar(data, x='Product Category', y='Total Amount', color='Product Category',
                 title='Sales by Product Category')
    st.plotly_chart(fig)

def plot_sales_over_time(data):
    """Plot sales over time."""
    st.subheader('Filter by Date Range')
    start_date = st.date_input("Start Date", value='2023-12-18')
    end_date = st.date_input("End Date", value=data['Date'].max())

    if start_date > end_date:
        st.error("Start date cannot be greater than end date.")
    else:
        filtered_data = data[(data['Date'] >= pd.Timestamp(start_date)) & (data['Date'] <= pd.Timestamp(end_date))]
        st.write(f"Showing data from {start_date} to {end_date}.")
        st.dataframe(filtered_data)
    """Visualize sales trends over time."""
    # fig = px.line(data, x='Date', y='Total Amount', title='Sales Trends Over Time')
    st.bar_chart(filtered_data, x = 'Date', y = 'Total Amount', x_label='Date', y_label='Total Amount')
