import plotly.express as px
import streamlit as st


def plot_sales_over_time(data):
    """Plot sales trends over time."""
    fig = px.line(data, x="Date", y="Total Amount", title="Sales Over Time")
    st.plotly_chart(fig)


def plot_category_distribution(data):
    """Show category distribution."""
    fig = px.bar(data, x="Product Category", y="Total Amount", color="Gender", title="Category Distribution")
    st.plotly_chart(fig)