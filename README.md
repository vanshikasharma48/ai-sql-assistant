# AI SQL Analytics Assistant

## Overview

AI SQL Analytics Assistant is a data analytics application that allows users to query a sales database using business-oriented questions and retrieve insights through SQL-powered analytics.

The project combines Python, SQLite, Pandas, and Streamlit to create an interactive analytics dashboard capable of answering common business questions such as:

* Top customers by sales
* Highest-performing product category
* Sales by region
* Revenue analysis

This project demonstrates database management, SQL querying, data analysis, and web application development.

---

## Features

* Interactive Streamlit web application
* SQLite database integration
* Automated business analytics queries
* Customer sales analysis
* Category-wise revenue analysis
* Regional sales insights
* Clean and user-friendly interface

---

## Tech Stack

### Programming Language

* Python

### Database

* SQLite

### Data Processing

* Pandas

### Web Application

* Streamlit

### Dataset

* Superstore Sales Dataset

---

## Project Structure

```text
AI-SQL-ASSISTANT/
│
├── app.py
├── database.db
├── data/
│   └── train.csv
├── notebooks/
│   └── analysis.ipynb
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI-SQL-ASSISTANT
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python -m streamlit run app.py
```

The application will open automatically in your browser.

---

## Example Queries

### Top Customers

```text
top customers
```

### Highest Sales Category

```text
highest category
```

### Regional Sales Analysis

```text
sales by region
```

---

## Sample Output

| Customer Name | Total Sales |
| ------------- | ----------: |
| Sean Miller   |    25043.05 |
| Tamara Chand  |    19052.22 |
| Raymond Buch  |    15117.34 |

---

## Learning Outcomes

Through this project, I learned:

* SQL query design and optimization
* Database creation using SQLite
* Data analysis using Pandas
* Building interactive applications with Streamlit
* Converting business requirements into analytical queries
* End-to-end project development workflow

---

## Future Enhancements

* Natural Language to SQL using Gemini/OpenAI
* AI-generated business insights
* Interactive visualizations
* Chat-based analytics assistant
* RAG-powered enterprise analytics
* Multi-database support

---

## Author

Vanshika Sharma

Data Science | Machine Learning | AI Enthusiast
