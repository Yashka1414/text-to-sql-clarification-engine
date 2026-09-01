import streamlit as st
from groq import Groq
from pydantic import BaseModel, Field

st.set_page_config(page_title="Text-to-SQL Engine", page_icon="🗄️", layout="wide")
st.title("🗄️ Text-to-SQL System with Clarification Engine")

api_key = st.sidebar.text_input("Enter Groq API Key:", type="password")
if not api_key:
    st.info("Please enter your Groq API Key in the sidebar to start.")
    st.stop()

client = Groq(api_key=api_key)

# Sample Database Schema
DEFAULT_SCHEMA = """
TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    signup_date DATE
);

TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES users(user_id),
    amount DECIMAL(10, 2),
    order_date DATE,
    status VARCHAR(20) -- 'completed', 'pending', 'cancelled'
);
"""

schema_input = st.text_area("Database Schema (DDL):", value=DEFAULT_SCHEMA, height=160)
user_query = st.text_input("Ask a question about the database:", placeholder="e.g., Show top 5 users by total order spending")

if st.button("Generate SQL") and user_query:
    system_prompt = f"""
    You are an expert SQL Engineer and Database Agent. 
    Analyze the following database schema and the user's natural language question.
    
    Database Schema:
    {schema_input}
    
    Tasks:
    1. Check if the user query is ambiguous or missing column/table details.
    2. If clear, generate valid ANSI SQL code.
    3. If ambiguous, provide a specific clarification question and a safe default SQL query assumption.
    
    Output Format:
    SQL Query: <SQL_HERE>
    Clarification Required: <YES/NO>
    Explanation/Questions: <REASONING_OR_CLARIFICATION_PROMPT>
    """

    with st.spinner("Analyzing schema & mapping query to SQL..."):
        try:
            clean_query = user_query.encode("utf-8", errors="ignore").decode("utf-8")
            res = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": clean_query}
                ],
                temperature=0.1
            )
            
            output = res.choices[0].message.content
            st.success("SQL Mapping Complete!")
            st.markdown("### 📋 Generated SQL & Clarification Analysis")
            st.markdown(output)
        except Exception as e:
            st.error(f"Error processing SQL generation: {e}")
