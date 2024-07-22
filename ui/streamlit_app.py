import requests
import streamlit as st

LOCAL_API_URL = "http://localhost:7860"
HF_SPACES_API_URL = "https://krstakis-prompt-search-engine.hf.space"

st.title("Prompt Search Engine")

api_server = st.radio(
    "Choose the API server:",
    ('Local', 'Hugging Face Spaces'),
    index=1
)

if api_server == 'Local':
    API_URL = LOCAL_API_URL
else:
    API_URL = HF_SPACES_API_URL

prompt = st.text_input("Enter a prompt")
n = st.slider("Number of results", 1, 20, 5)

if st.button("Search"):
    response = requests.post(API_URL + "/search/", json={"prompt": prompt, "n": n})
    if response.status_code == 200:
        results = response.json()
        for result in results:
            score = result["score"]
            result_prompt = result["description"]
            st.write(f"Score: {score:.4f}, Prompt: {result_prompt}")
    else:
        st.error(f"Error: Could not retrieve results. Status code: {response.status_code}")
