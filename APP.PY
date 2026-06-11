import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(
    page_title="AI SQL Analytics Assistant",
    page_icon="📊",
    layout="wide"
)

conn = sqlite3.connect("database.db")

def ask_database(question):

    question = question.lower()

    if "top customers" in question:
        query = """
        SELECT "Customer Name",
        SUM(Sales) AS TotalSales
        FROM sales
        GROUP BY "Customer Name"
        ORDER BY TotalSales DESC
        LIMIT 5;
        """

    elif "highest category" in question:
        query = """
        SELECT Category,
        SUM(Sales) AS TotalSales
        FROM sales
        GROUP BY Category
        ORDER BY TotalSales DESC
        LIMIT 1;
        """

    elif "sales by region" in question:
        query = """
        SELECT Region,
        SUM(Sales) AS TotalSales
        FROM sales
        GROUP BY Region
        ORDER BY TotalSales DESC;
        """

    else:
        return None

    return pd.read_sql(query, conn)

st.title("📊 AI SQL Analytics Assistant")

question = st.text_input(
    "Ask a business question",
    placeholder="Top customers by sales"
)

if st.button("Ask"):

    result = ask_database(question)

    if result is not None:
        st.dataframe(result, use_container_width=True)
    else:
        st.error("Question not supported yet")