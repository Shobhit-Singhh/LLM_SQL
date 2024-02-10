import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

def get_gemini_response(question, prompt):
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048
        }
    model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config)
    response = model.generate_content([prompt[0],prompt[1], question])
    return response.text    

def read_sql_query(sql, conn):
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    st.table(rows)

def print_table_overview(database, table_name):
    cursor = database.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()

    st.subheader(f"Columns in {table_name}:")
    for column in columns:
        st.write(f"- {column[1]} ({column[2]})")

def detail_prompt(database):
    cursor = database.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    prompt = "Database Information: "
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        prompt += f"Table: {table_name} - Columns: "
        for column in columns:
            prompt += f"{column[1]} ({column[2]}), "
        prompt += " "
    st.text(prompt)
    return prompt

def print_database_overview(database):
    if not isinstance(database, sqlite3.Connection):
        st.error("Invalid database connection.")
        return

    # Get a list of tables in the database
    cursor = database.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    st.header("Overview of Database:")
    st.markdown("---------------------")

    if not tables:
        st.warning("No tables found in the database.")
    else:
        st.subheader("List of Tables:")
        for table in tables:
            table_name = table[0]
            expander = st.expander(f"{table_name} Table")
            with expander:
                print_table_overview(database, table_name)

def sidebar():
    with st.sidebar:
        st.warning("Only upload files that are SQLite-type databases.")
        uploaded_file = st.file_uploader("Upload SQL Database", type=[".db"])
        if uploaded_file is not None:
            try:
                database = sqlite3.connect(':memory:')  # Use in-memory database for checking
                database.executescript(uploaded_file.read())
                st.success("File uploaded successfully as SQLite-type database.")
            except sqlite3.DatabaseError:
                st.error("Invalid SQLite-type database file. Please upload a valid .db file.")
                st.stop()
        else:
            st.warning("Using default database")
            database = sqlite3.connect(os.path.join('data', "chinook.db"))

        print_database_overview(database)
        return database

def main(database):
    st.title("I can Retrieve Any SQL query")
    question = st.text_input("Input: ", key="input")
    submit = st.button("Ask the question") 
    prompt = ""
    prompt +="""
    You are an expert in converting English questions to SQL query!
    Give me the SQL query for the following question in text format.
    in responce please remove the 'sql' word and triple backtick (```) in beginning or end of the query 
    in responce please remove the 'sql' word and triple backtick (```) in beginning or end of the query 
    in responce please remove the 'sql' word and triple backtick (```) in beginning or end of the query 
    in responce please remove the 'sql' word and triple backtick (```) in beginning or end of the query 
    give me the sql command of following question
    """
    prompt += question
    
    if submit:
        response = get_gemini_response(question, prompt)
        st.text(response)
        read_sql_query(response, database)

def app():
    
    database = sidebar()
    main(database)

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    genai.configure(api_key="GOOGLE_API_KEY")
    app()
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #f1f1f1;
                padding: 2px;
                text-align: center;
                font-size: 14px;
                color: #555;
            }
            .linkedin {
                color: #0077b5;
            }
        </style>
        <div class="footer">
            Data Science App Tutorial by Shobhit Singh, 
            <a class="linkedin" href="https://www.linkedin.com/in/your-linkedin-profile" target="_blank">LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )
