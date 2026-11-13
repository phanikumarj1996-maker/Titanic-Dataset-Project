import streamlit as st
import pandas as pd
import psycopg2

st.set_page_config(page_title="Titanic Dashboard", layout="wide")
st.title("🚢 Titanic Dataset Dashboard")

try:
   
    df = pd.read_sql(
        "SELECT * FROM titanic_project.passengers",
        conn
    )


    st.success("Database connected successfully!")

    st.success("Database connected successfully!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Passengers", len(df))
    col2.metric("survived", int(df["survived"].sum()))
    col3.metric("Not survived", int((df["survived"] == 0).sum()))

    st.subheader("Passenger Data")
    st.dataframe(df, use_container_width=True)

    st.subheader("Survival Distribution")
    st.bar_chart(df["survived"].value_counts())
    
    st.subheader("Survival Rate by Gender")
    gender_survival = df.groupby("sex")["survived"].mean()
    st.bar_chart(gender_survival)
    conn.close()

except Exception as e:
    st.error(f"Error: {e}")

  