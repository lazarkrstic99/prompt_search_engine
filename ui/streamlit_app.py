"""
This Streamlit application interfaces with a FastAPI backend to search for prompts based on user input.

The user can enter a prompt and specify the number of similar results they want to retrieve.
The application then sends a request to the FastAPI endpoint and displays the results.
"""

import requests
import streamlit as st

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
