# Retail Sales Analysis Dashboard

## Overview
The **Retail Sales Analysis Dashboard** is an interactive tool built with **Streamlit** to help businesses analyze sales data, generate insights, predict future trends, and provide actionable recommendations. This project was designed for a hackathon to showcase innovative solutions for retail data analytics.

### Features
- **Data Upload**: Upload retail sales reports in CSV format.
- **Data Insights**: Visualize sales trends, top-performing categories, and customer demographics.
- **Sales Forecasting**: Predict future sales using advanced machine learning models.
- **Recommendations**: Generate actionable suggestions for inventory management and marketing strategies.
- **Exportable Reports**: Download processed data and insights for further analysis.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/perfervid-prog/hackathon.git
   cd hackathon
   ```
2. **Create a virtual enviroment**

    ```bash
    python -m venv hacacode
    source hacacode/bin/activate    # For Linux/macOS
    hacacode\Scripts\activate       # For Windows
    ```

3. **Install Dependencies**<br>
    Use the provided `requirements.txt` file to install the necessary python packages.

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**<br>

    Now, there you go. Launch the Streamlit app:

    ```bash
    streamlit run app.py
    ```
---

## Project Structure

```bash
hackathon/
│
├── app.py                     # Main Streamlit app
├── data/                      # Example and uploaded datasets
│   ├── retail_sales_dataset.csv      # Sample dataset for testing
│
├── modules/                   # Core functionalities
│   ├── data_processing.py      # Handles file uploads and preprocessing
│   ├── visualizations.py       # Handles dynamic plots and graphs
│   ├── predictive_model.py     # Contains ML model training and predictions
│   ├── recommendations.py      # Generates personalized recommendations
│   └── insights.py             # AI-driven insights (e.g., GPT-based summaries)
│
├── requirements.txt           # Required Python packages
├── README.md                  # Project documentation
```
