import plotly.express as px
import pandas as pd
import streamlit as st


def plot_category_distribution(data):
    """Plot sales distribution by category."""
    fig = px.bar(data, x='Product Category', y='Total Amount', color='Product Category',
                 title='Sales by Product Category')
    st.plotly_chart(fig)


def plot_sales_over_time(data):
    try:
        """Plot sales over time."""

        st.subheader('Filter by Date Range')

        # Initialize session state for dates
        if 'start_date' not in st.session_state:
            st.session_state['start_date'] = min(data['Date'])  # Default start date
        if 'end_date' not in st.session_state:
            st.session_state['end_date'] = max(data['Date'])  # Default end date

        # Create columns for Start and End Date Pickers
        col1, col2 = st.columns(2)

        with col1:
            start_date = st.date_input(
                "Start Date", 
                value=st.session_state['start_date'], 
                key="start_date_input",  # Use unique keys
                format="YYYY-MM-DD"
            )
        with col2:
            end_date = st.date_input(
                "End Date", 
                value=st.session_state['end_date'], 
                key="end_date_input",  # Use unique keys
                format="YYYY-MM-DD"
            )

        # Convert to datetime.date for comparison
        start_date = pd.to_datetime(start_date).date()
        end_date = pd.to_datetime(end_date).date()

        # Update session state with the new dates
        st.session_state['start_date'] = start_date
        st.session_state['end_date'] = end_date

        # Validate the date range
        if start_date > end_date:
            st.error("Start date cannot be greater than end date.")
        else:
            # Filter data by the selected date range
            filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]

            st.write(f"Showing data from {start_date} to {end_date}.")
            st.dataframe(filtered_data, use_container_width=True)

            """Visualize sales trends over time."""
            st.bar_chart(filtered_data, x='Date', y='Total Amount', x_label='Date', y_label='Total Amount')

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
