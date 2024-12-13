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
    """ Perform any necessary data cleaning """
    try:
        # removing the customer ID, and so on
        data = data.drop(['Transaction ID', 'Customer ID', 'Quantity', 'Price per Unit'], axis=1)
        # convert date column to datetime
        data['Date'] = pd.to_datetime(data['Date'])
        data = data.sort_values(by='Date')

        # Calculate the total amount if not present
        if 'Total Amount' not in data.columns:
            data['Total Amount'] = data['Quantity'] * data['Price per Unit']

        # Extract the month and year for analysis
        # data['Month'] = data['Date'].dt.month
        # data['Year'] = data['Date'].dt.year

        return data
    except Exception as e:
        raise ValueError("Error preprocessing data.")
    