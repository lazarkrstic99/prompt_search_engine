import streamlit as st
import requests


API_URL = "http://localhost:8000/search/"

st.title("Prompt Search Engine")

prompt = st.text_input("Enter a prompt")
n = st.slider("Number of results", 1, 20, 5)

if st.button("Search"):
    response = requests.post(API_URL, json={"prompt": prompt, "n": n})
    if response.status_code == 200:
        results = response.json()
        for result in results:
            score = result["score"]
            result_prompt = result["description"]
            st.write(f"Score: {score:.4f}, Prompt: {result_prompt}")
    else:
        st.error("Error: Could not retrieve results")
