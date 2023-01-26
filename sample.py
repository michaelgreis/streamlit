import streamlit as st

#Title
st.title("Hello World")

upload_file = st.file_uploader("Choose a file")
if upload_file is not None:
    st.text("File uploaded")


@st.experimental_singleton()
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True #issues with **st.secrets. Wrong syntax
    )

conn = init_connection()
print("Successful connection")