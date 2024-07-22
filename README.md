# Prompt Search Engine

## Overview
This project develops a prompt search engine leveraging FastAPI and Streamlit, utilizing a pre-trained SBERT model for vectorizing and comparing text prompts. Designed to accept a text prompt and return the top `n` most similar prompts used for Stable Diffusion.

## Environment Setup
Follow these steps to set up and run the project on your local machine:

### Clone the Repository
Clone the project repository to your local machine:
```
git clone https://github.com/lazarkrstic99/prompt_search_engine.git
```
Position to root directory:
```
cd prompt_search_engine
```
### Install Dependencies
Install the required dependencies using the provided `requirements.txt`:
```
pip install -r requirements.txt
```
## Running the Application

### Start the FastAPI Server
Position to root directory and run the following command to start the FastAPI server:
```
python run.py
```
### Launch the Streamlit UI
Open another terminal and start the Streamlit UI:
```
streamlit run ui/streamlit_app.py
```
The FastAPI server will run on `http://localhost:7860`, and the Streamlit UI will be available at `http://localhost:8501`.

## API Endpoints
The application provides a RESTful API for interacting with the prompt search engine:

### POST /search/
- **Description**: Receives a user prompt and returns the top `n` similar prompts.

## Docker Container

### Building the Docker Image
Build the Docker image with the following command:
```
docker build -t search-engine .
```
### Running the Docker Container
Run the Docker container:
```
docker run search-engine
```
## Deployment Details

This section provides detailed instructions for deploying the Prompt Search Engine both locally and on Hugging Face Spaces. The application combines a FastAPI backend with a Streamlit frontend for interactive prompt searching.

### Local Deployment

1. **Prerequisites**:
   - Ensure Python 3.9 is installed on your system.
   - Clone the project repository:
     ```
     git clone https://yourrepository.git
     cd prompt_search_engine
     ```
   - Install all required dependencies:
     ```
     pip install -r requirements.txt
     ```

2. **Start the FastAPI Server**:
   - Navigate to the project directory and execute the following command to start the FastAPI server, which will serve the API:
     ```
     python run.py
     ```

3. **Launch Streamlit**:
   - Open another terminal window and launch the Streamlit application that interfaces with the FastAPI backend:
     ```
     streamlit run ui/streamlit_app.py
     ```

4. **Accessing the Application**:
   - The Streamlit UI is accessible at `http://localhost:8501`.
   - The FastAPI server is accessible at `http://localhost:8000`, and its API documentation is available at `http://localhost:8000/docs`.

### Deployment on Hugging Face Spaces

The API for the application is deployed at [Hugging Face Spaces](https://krstakis-prompt-search-engine.hf.space/search/). The deployment utilizes multi-staging in Docker to optimize the build process. This approach ensures that the engine is not rebuilt and re-vectorized unnecessarily. Instead, it is only rebuilt when there are changes to the engine itself or the underlying database.

## Using the UI
To use the UI, navigate to `http://localhost:8501` in your web browser or it will automatically open when you run streamlit. Enter a prompt and adjust the number of results using the slider, then click "Search" to retrieve similar prompts.
