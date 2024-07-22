# Prompt Search Engine

## Overview
This project develops a prompt search engine leveraging FastAPI and Streamlit, utilizing a pre-trained model for vectorizing and comparing text prompts. Designed to accept a text prompt and return the top `n` most similar prompts, the application showcases how to integrate advanced machine learning techniques with modern web frameworks for practical applications.

## Environment Setup
Follow these steps to set up and run the project on your local machine:

### Clone the Repository
Clone the project repository to your local machine:

git clone https://github.com/lazarkrstic99/prompt_search_engine.git

cd prompt_search_engine

### Install Dependencies
Install the required dependencies using the provided `requirements.txt`:

pip install -r requirements.txt

### Prepare the Model and Data
Ensure the `engine.pickle` file is generated from your model training process and placed in the root directory of the project.

## Running the Application

### Start the FastAPI Server
Run the following command to start the FastAPI server:

python run.py

### Launch the Streamlit UI
Open another terminal and start the Streamlit UI:

streamlit run ui/streamlit_app.py

The FastAPI server will run on `http://localhost:8000`, and the Streamlit UI will be available at `http://localhost:8501`.

## API Endpoints
The application provides a RESTful API for interacting with the prompt search engine:

### POST /search/
- **Description**: Receives a user prompt and returns the top `n` similar prompts.


