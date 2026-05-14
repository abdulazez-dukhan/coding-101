
import streamlit as st

st.set_page_config(page_title="Minimal Streamlit App", layout="centered")

st.title("Minimal Streamlit App")
st.write("This is a tiny Streamlit app generated from a notebook.")

name = st.text_input("What is your name?", value="AI Engineer")
top_k = st.slider("Choose top_k", min_value=1, max_value=10, value=3)

if st.button("Run"):
    st.success(f"Hello, {name}!")
    st.write(f"You selected top_k = {top_k}")

st.caption("Run with: streamlit run streamlit_exercises/minimal_app.py")
