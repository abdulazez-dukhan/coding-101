
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Retrieval Review Dashboard", layout="wide")

# TODO 1:
# Create a cached function load_chunks() using @st.cache_data.
# It should return a pandas DataFrame with columns:
# - chunk_id
# - source
# - text
# - score

@st.cache_data
def load_chunks():
    data = {
        "chunk_id": [1,2,3],
        "Source": ["Video", "Audio", "OCR"],
        "Text": ["This is text1", "This is text2", "This is text3"],
        "Score": [0.7, 0.8, 0.6]
    }
    return pd.DataFrame(data=data)


# TODO 2:
# Initialize st.session_state["history"] as an empty list if it does not exist.
# if not (st.session_state["history"]):
#     st.session_state["history"] = []

if "history" not in st.session_state:
    st.session_state["history"] = []
    
# TODO 3:
# Load the chunks dataframe.
df = load_chunks()

# TODO 4:
# Add a title and short explanation.
st.title("Sessions")
st.markdown("""
            This streamlit exercise is about experimenting with sessions.
            """)

# TODO 5:
# Add a sidebar selectbox to filter by source.
# Include an "All" option.
selection = st.sidebar.selectbox("Sidebar options", ["Video", "Audio", "OCR", "All"])

# TODO 6:
# Display the filtered dataframe.
filter_df = df[df["Source"] == selection] if (selection != "All") else df
st.dataframe(filter_df, use_container_width=True)

container = st.container()

# TODO 7:
# Add a question text input.
with container:
    question_input = st.text_input("Ask away")



# TODO 8:
# Add a button called "Save question".
# When clicked, append the question to st.session_state["history"].
if st.button("Save question"):
    st.session_state["history"].append(question_input)

    
# TODO 9:
# Display the search/question history.
for item in st.session_state["history"]:
    st.write(item)
