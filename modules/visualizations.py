import plotly.express as px
import streamlit as st

def plot_category_distribution(data):
    """Plots sales distribution by category."""
    fig = px.bar(data, x='Product Category', y='Total Amount', color='Product Category')
    fig.update_layout(title_text="Sales by Product Category")
    st.plotly_chart(fig, use_container_width=True)

def plot_sales_over_time(data):
    """Plots sales over time."""
    fig = px.bar(data, x='Date', y='Total Amount', labels={'Total Amount':'Sales Amount'})
    fig.update_layout(title_text="Sales Trends Over Time")
    st.plotly_chart(fig, use_container_width=True)