HireSmart
Overview
HireSmart is a FastAPI-based application designed to extract key information from CVs in PDF format. It processes CVs to retrieve details such as full name, email, education history, skills, and work experience, returning the results in a structured JSON format. The application leverages the LangChain framework and a pre-trained language model (Mistral-Nemo-Instruct-2407) for natural language processing and text extraction.
Features

PDF CV Parsing: Upload a PDF CV and extract structured information.
Structured Output: Returns extracted data in a consistent JSON format.
AI-Powered Extraction: Utilizes the Mistral-Nemo-Instruct-2407 model for accurate information extraction.
Scalable API: Built with FastAPI for high-performance, asynchronous processing.

Requirements
The following dependencies are required to run the project. They are listed in requirements.txt:

fastapi
uvicorn
langchain
langchain-community
langchain-core
pypdf
sentence-transformers
transformers
torch
faiss-cpu
python-multipart
huggingface_hub

Installation

Clone the Repository:
git clone <repository_url>
cd hiresmart


Install Dependencies:
pip install -r requirements.txt


Set Hugging Face Token:Set your Hugging Face API token as an environment variable:
export HF_TOKEN='your_huggingface_token_here'


Run the Application:Start the FastAPI server using:
bash run.sh

Alternatively, run directly:
uvicorn app:app --host 0.0.0.0 --port 8000 --reload



Usage

API Endpoint:

Endpoint: POST /parse_cv/
Input: Upload a PDF file containing a CV.
Output: A JSON object with the following fields:{
  "full_name": "string",
  "email": "string",
  "education": "string",
  "skills": "string",
  "experience": "string"
}




Example Request (using curl):
curl -X POST "http://localhost:8000/parse_cv/" -F "file=@path_to_cv.pdf"


Example Response:
{
  "full_name": "Yousef Abdelnasser",
  "email": "youssef.abdalnasser54@gmail.com",
  "education": "Beni Suef National University, Bachelor of Artificial Intelligence (Grade: Very Good), Beni Suef, Egypt, Oct. 2022 – Jun. 2026",
  "skills": "Python, Java, C++, TensorFlow, PyTorch, Keras, Scikit-learn, SVM, Decision Trees, KNN, OpenCV, Image Processing, Feature Extraction, Pandas, NumPy, Matplotlib, Seaborn, SQL Server, MySQL, PostgreSQL, Jupyter Notebook, Google Colab, VS Code",
  "experience": "Technocolabs Softwares, Data Scientist Intern (Remote), Feb. 2025 – Apr. 2025"
}



Project Structure

app.py: FastAPI application with the main API endpoint for CV parsing.
cv_parser.py: Core logic for CV text extraction and parsing using LangChain and the language model.
requirements.txt: List of Python dependencies.
run.sh: Shell script to run the FastAPI server.
Dockerfile: Docker configuration for containerizing the application.

Docker Setup
To run the application in a Docker container:

Build the Docker image:docker build -t hiresmart .


Run the container:docker run -p 8000:8000 -e HF_TOKEN='your_huggingface_token_here' hiresmart



Notes

Ensure the Hugging Face token is set securely as an environment variable.
The application assumes the input PDF is a valid CV with structured text. Non-standard formats may affect parsing accuracy.
The Mistral-Nemo-Instruct-2407 model requires significant computational resources, especially GPU support for optimal performance.

License
This project is licensed under the MIT License.
