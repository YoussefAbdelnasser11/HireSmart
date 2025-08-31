import streamlit as st
from hire_smart import extract_text_from_pdf, parse_cv_content

# Streamlit page configuration
st.set_page_config(page_title="HireSmart CV Parser", layout="wide", page_icon="📄")

# Custom CSS
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

# Title
st.markdown('<div class="title">HireSmart CV Parser</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a PDF CV to extract key information instantly</div>', unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload a CV (PDF)", type=["pdf"], help="Select a PDF file to parse")

if uploaded_file is not None:
    if not uploaded_file.name.endswith(".pdf"):
        st.markdown('<div class="error">Error: Only PDF files are allowed.</div>', unsafe_allow_html=True)
    else:
        with st.spinner("Parsing CV... This may take a moment."):
            try:
                cv_text = extract_text_from_pdf(uploaded_file.read())
                data = parse_cv_content(cv_text)

                st.markdown('<div class="success">CV parsed successfully!</div>', unsafe_allow_html=True)

                # Candidate Info
                st.markdown('<div class="section-header">Candidate Information</div>', unsafe_allow_html=True)
                st.markdown(f"**Full Name**: {data.get('full_name', 'Not found')}")
                st.markdown(f"**Email**: {data.get('email', 'Not found')}")

                # Education
                st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)
                education = data.get('education', 'Not found')
                if isinstance(education, list) and education:
                    st.table([
                        {"Degree": edu.get("degree", ""), "Institution": edu.get("institution", ""), "Year": edu.get("year", "")}
                        for edu in education
                    ])
                else:
                    st.markdown(education if education else "Not found")

                # Skills
                st.markdown('<div class="section-header">Skills</div>', unsafe_allow_html=True)
                skills = data.get('skills', 'Not found')
                if isinstance(skills, list) and skills:
                    for skill in skills:
                        st.markdown(f"- {skill}")
                else:
                    st.markdown(skills if skills else "Not found")

                # Experience
                st.markdown('<div class="section-header">Work Experience</div>', unsafe_allow_html=True)
                experience = data.get('experience', 'Not found')
                if isinstance(experience, list) and experience:
                    st.table([
                        {"Role": exp.get("role", ""), "Company": exp.get("company", ""), "Years": exp.get("years", "")}
                        for exp in experience
                    ])
                else:
                    st.markdown(experience if experience else "Not found")

            except Exception as e:
                st.markdown(f'<div class="error">Error: {str(e)}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | HireSmart CV Parser © 2025", unsafe_allow_html=True)
import streamlit as st
from hire_smart import extract_text_from_pdf, parse_cv_content

# Streamlit page configuration
st.set_page_config(page_title="HireSmart CV Parser", layout="wide", page_icon="📄")

# Custom CSS
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

# Title
st.markdown('<div class="title">HireSmart CV Parser</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload a PDF CV to extract key information instantly</div>', unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload a CV (PDF)", type=["pdf"], help="Select a PDF file to parse")

if uploaded_file is not None:
    if not uploaded_file.name.endswith(".pdf"):
        st.markdown('<div class="error">Error: Only PDF files are allowed.</div>', unsafe_allow_html=True)
    else:
        with st.spinner("Parsing CV... This may take a moment."):
            try:
                cv_text = extract_text_from_pdf(uploaded_file.read())
                data = parse_cv_content(cv_text)

                st.markdown('<div class="success">CV parsed successfully!</div>', unsafe_allow_html=True)

                # Candidate Info
                st.markdown('<div class="section-header">Candidate Information</div>', unsafe_allow_html=True)
                st.markdown(f"**Full Name**: {data.get('full_name', 'Not found')}")
                st.markdown(f"**Email**: {data.get('email', 'Not found')}")

                # Education
                st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)
                education = data.get('education', 'Not found')
                if isinstance(education, list) and education:
                    st.table([
                        {"Degree": edu.get("degree", ""), "Institution": edu.get("institution", ""), "Year": edu.get("year", "")}
                        for edu in education
                    ])
                else:
                    st.markdown(education if education else "Not found")

                # Skills
                st.markdown('<div class="section-header">Skills</div>', unsafe_allow_html=True)
                skills = data.get('skills', 'Not found')
                if isinstance(skills, list) and skills:
                    for skill in skills:
                        st.markdown(f"- {skill}")
                else:
                    st.markdown(skills if skills else "Not found")

                # Experience
                st.markdown('<div class="section-header">Work Experience</div>', unsafe_allow_html=True)
                experience = data.get('experience', 'Not found')
                if isinstance(experience, list) and experience:
                    st.table([
                        {"Role": exp.get("role", ""), "Company": exp.get("company", ""), "Years": exp.get("years", "")}
                        for exp in experience
                    ])
                else:
                    st.markdown(experience if experience else "Not found")

            except Exception as e:
                st.markdown(f'<div class="error">Error: {str(e)}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | HireSmart CV Parser © 2025", unsafe_allow_html=True)
