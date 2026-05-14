
import streamlit as st

st.set_page_config(page_title="AI Search UI", layout="centered")

# TODO 1:
# Add a title for the app.
st.title("AI search UI")

# TODO 2:
# Add a short markdown description explaining that this is a fake AI search interface.
st.markdown("""
            ### 🔍 :red[This is a fake AI search tool].
            used for the purpose of learning.
            It simulates real-time data retrieval to help students understand backend API integrations. 
            By testing queries in this controlled environment, you can safely explore how search 
            parameters alter model outputs without incurring high infrastructure costs.""")


# TODO 4:
# Add a slider for top_k from 1 to 10 with default 3.
slider = st.slider("Top-k", 1,10,3)

# TODO 5:
# Add a selectbox for search mode:
# ["semantic", "keyword", "hybrid"]
search_mode = st.selectbox("Search mode selection", ["semantic", "keyword", "hybrid"])

# TODO 3:
# Add a text input for a user question.
# Example label: "Ask a question"
conainter = st.container()

# TODO 6:
# Add a button called "Search".

# TODO 7:
# When the button is clicked:
# - display the question
# - display top_k
# - display search mode
# - show a fake success message    

with conainter:
    question = st.chat_input("Ask a question")
    if question:
        st.write(f'Top-k selected: {slider}')
        st.write(f'Search mode: {search_mode}')
        st.write(f'Succeeded')
        st.write(question)
