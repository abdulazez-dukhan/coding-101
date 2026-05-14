
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mini RAG Playground", layout="wide")

# TODO:
# Build a mini RAG playground with:
# - title
# - sidebar top_k slider
# - sidebar retrieval mode selectbox
# - sidebar show_debug checkbox
# - question text area
# - generate answer button
# - fake retrieved chunks
# - fake answer
# - optional debug table

st.title("RAG Playground")

st.sidebar.selectbox("top_K selection", (["x","y","z"]))
st.sidebar.selectbox("Retrieval mode selection", (["x","y","z"]))
st.sidebar.selectbox("Shwo_debug selection", (["x","y","z"]))