import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.title("Sales Dashboard with LLM Insights")

# Input Section
st.subheader("Manual Data Entry")
data = st.text_area("Enter CSV data (e.g., customer,sales)", "customer1,100\ncustomer2,200")
if data:
    from io import StringIO
    df = pd.read_csv(StringIO(data))
    st.dataframe(df)

    # Chart
    st.subheader("Sales Chart")
    fig = px.bar(df, x='customer', y='sales', title="Customer-wise Sales")
    st.plotly_chart(fig)

    # LLM Analysis
    st.subheader("Ask LLM a question about this data")
    user_question = st.text_input("Your Question", "Who is the top customer?")
    if st.button("Ask LLM"):
        response = requests.post("http://localhost:5000/ask", json={
            "question": user_question,
            "data": df.to_json()
        })
        if response.ok:
            st.success(response.json()['answer'])
        else:
            st.error("Failed to connect to LLM API")