import streamlit as st
import pandas as pd

# loads the report
def load_data(file):
    """ Load CSV file into a pandas DataFrame"""
    try:
        data = pd.read_csv(file)
        
    
        return data
    except Exception as e:
        raise ValueError("Error loading data. Please ensure it's a valid CSV.")
    
    

def preprocess_data(data):
    """ Perform necessary data cleaning and retain all relevant columns """
    try:
        # Specify the columns to drop
        columns_to_drop = ['Transaction ID', 'Gender', 'Age', 'Customer ID', 'Quantity', 'Price per Unit']
        retained_columns = [col for col in data.columns if col not in columns_to_drop]

        # Ensure 'Date' is in datetime format
        data['Date'] = pd.to_datetime(data['Date']).dt.date

        # Group by 'Date' and aggregate Total Amount while keeping other columns
        data = data.groupby('Date', as_index=False).agg({
            **{col: 'first' for col in retained_columns if col != 'Total Amount'},  # Keep the first occurrence of other columns
            'Total Amount': 'sum'  # Sum for Total Amount
        })

        # Sort by date
        data = data.sort_values(by='Date').reset_index(drop=True)

        return data
    except Exception as e:
        raise ValueError(f"Error preprocessing data: {str(e)}")

    