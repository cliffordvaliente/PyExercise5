# Pagila DWH Reporting - Python Exercise

## Overview
This project is a Python reporting application using Streamlit to visualize data from the Pagila Data Warehouse (PostgreSQL). It was created as part of the DMAR Winter Term 2025/26 exercise on "Vibe Coding".

## Technology Stack
* **Language:** Python 3
* **Framework:** Streamlit
* **Database:** PostgreSQL (Pagila DWH)
* **Visualization:** Plotly Express

## AI Assistance Documentation
As per the exercise guidelines, this project was built using AI-assisted programming ("Vibe Coding").

* **AI Tool Used:** Gemini 3 Pro.
* **Main Prompts:**
    1.  "Help me create a Streamlit app connecting to the Pagila Postgres database to show a bar chart of rentals by category and a line chart of trends."
    2.  "Write a SQL query to select film category, total rentals, and revenue from the view `vw_rental_analysis`."
    3.  "Troubleshoot PostgreSQL connection errors in Python."

## Learnings & Challenges
* **What worked well:** Everything went well, I followed the introctions from Exercise5 folder and also I used some information for debugging for pgAdmin 4 in the exercise 3 OLAP folder from moddle.
* **Challenges:** Regarding the challenges, I am familiar with python, git and github from before. The small challenge I had was setting up the database which took about 15-30min setting up the dataset and server. Else went well.

## How to Run
1.  Install dependencies:
    ```bash
    pip install streamlit pandas psycopg2-binary plotly
    ```
2.  Run the app:
    ```bash
    streamlit run app.py
    ```