import streamlit as st
import requests
import json
from pathlib import Path

# Streamlit page configuration
st.set_page_config(page_title="HireSmart CV Parser", layout="wide", page_icon="📄")

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main { background-color: #f5f7fa; padding: 20px; }
    .title { font-size: 2.5em; color: #1e3a8a; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .subtitle { font-size: 1.2em; color: #4b5563; text-align: center; margin-bottom: 30px; }
    .section-header { font-size: 1.5em; color: #1e3a8a; font-weight: bold; margin-top: 20px; }
    .stButton>button { background-color: #1e3a8a; color: white; border-radius: 5px; padding: 10px 20px; }
    .stButton>button:hover { background-color: #3b82f6; }
    .error { color: #dc2626; font-weight: bold; }
    .success { color: #16a34a; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title">HireSmart CV Parser</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a PDF CV to extract key information instantly</div>', unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload a CV (PDF)", type=["pdf"], help="Select a PDF file to parse")

if uploaded_file is not None:
    # Validate file
    if not uploaded_file.name.endswith(".pdf"):
        st.markdown('<div class="error">Error: Only PDF files are allowed.</div>', unsafe_allow_html=True)
    else:
        # Display loading spinner while processing
        with st.spinner("Parsing CV... This may take a moment."):
            try:
                # Prepare file for API request
                files = {"file": (uploaded_file.name, uploaded_file.read(), "application/pdf")}
                # Send request to FastAPI backend
                response = requests.post("http://localhost:8000/parse_cv/", files=files)

                # Check response status
                if response.status_code == 200:
                    data = response.json()
                    st.markdown('<div class="success">CV parsed successfully!</div>', unsafe_allow_html=True)

                    # Display results in sections
                    st.markdown('<div class="section-header">Candidate Information</div>', unsafe_allow_html=True)
                    st.markdown(f"**Full Name**: {data.get('full_name', 'Not found')}")
                    st.markdown(f"**Email**: {data.get('email', 'Not found')}")

                    # Education section
                    st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)
                    education = data.get('education', 'Not found')
                    if isinstance(education, list) and education:
                        st.table([
                            {"Degree": edu.get("degree", ""), "Institution": edu.get("institution", ""), "Year": edu.get("year", "")}
                            for edu in education
                        ])
                    else:
                        st.markdown(education if education else "Not found")

                    # Skills section
                    st.markdown('<div class="section-header">Skills</div>', unsafe_allow_html=True)
                    skills = data.get('skills', 'Not found')
                    if isinstance(skills, list) and skills:
                        for skill in skills:
                            st.markdown(f"- {skill}")
                    else:
                        st.markdown(skills if skills else "Not found")

                    # Experience section
                    st.markdown('<div class="section-header">Work Experience</div>', unsafe_allow_html=True)
                    experience = data.get('experience', 'Not found')
                    if isinstance(experience, list) and experience:
                        st.table([
                            {"Role": exp.get("role", ""), "Company": exp.get("company", ""), "Years": exp.get("years", "")}
                            for exp in experience
                        ])
                    else:
                        st.markdown(experience if experience else "Not found")

                else:
                    st.markdown(f'<div class="error">Error: {response.json().get("detail", "Failed to parse CV")}</div>', unsafe_allow_html=True)
            except requests.exceptions.ConnectionError:
                st.markdown('<div class="error">Error: Could not connect to the backend. Ensure the FastAPI server is running at http://localhost:8000.</div>', unsafe_allow_html=True)
            except Exception as e:
                st.markdown(f'<div class="error">Error: {str(e)}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | HireSmart CV Parser © 2025", unsafe_allow_html=True)