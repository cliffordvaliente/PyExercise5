import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# 1. Setup Database Connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="pagila_dwh",
            user="postgres",      
            password="postgres"
        )
        return conn
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

# 2. Page Configuration
st.set_page_config(page_title="Pagila DWH Reporting", layout="wide")
st.title("Pagila Data Warehouse Reports")

conn = get_db_connection()

if conn:
    # --- REPORT 1: Rentals by Film Category (Bar Chart)
    st.header("Report 1: Rentals by Film Category")
    
    # SQL Query from the exercise sheet 
    query1 = """
    SELECT film_category,
           COUNT(*) AS total_rentals,
           SUM(rental_amount) AS total_revenue
    FROM vw_rental_analysis
    GROUP BY film_category
    ORDER BY total_rentals DESC;
    """
    
    # Load data into Pandas
    df_category = pd.read_sql_query(query1, conn)
    
    # Display the Chart (Bar Chart required) 
    fig1 = px.bar(
        df_category, 
        x='film_category', 
        y='total_rentals', 
        title='Total Rentals by Category',
        color='total_revenue',
        labels={'film_category': 'Category', 'total_rentals': 'Number of Rentals'}
    )
    st.plotly_chart(fig1, use_container_width=True)

    # --- REPORT 2: Rental Trends Over Time (Line Chart)
    st.header("Report 2: Rental Trends Over Time")
    
    # SQL Query from the exercise sheet
    query2 = """
    SELECT year, month, month_name,
           COUNT(*) AS total_rentals,
           SUM(rental_amount) AS total_revenue
    FROM vw_rental_analysis
    GROUP BY year, month, month_name
    ORDER BY year, month;
    """
    
    df_trends = pd.read_sql_query(query2, conn)
    
    # Create a composite column for the X-axis (Year-Month)
    df_trends['date_label'] = df_trends['year'].astype(str) + '-' + df_trends['month'].astype(str).str.zfill(2)

    # Display the Chart (Line Chart required) [cite: 46]
    fig2 = px.line(
        df_trends, 
        x='date_label', 
        y='total_revenue', 
        title='Monthly Revenue Trends',
        markers=True,
        labels={'date_label': 'Time', 'total_revenue': 'Revenue'}
    )
    st.plotly_chart(fig2, use_container_width=True)

    conn.close()