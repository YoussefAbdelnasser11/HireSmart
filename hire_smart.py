import re
import json
from typing import List, Dict, Any
from langchain.document_loaders import PyPDFLoader
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers.structured import StructuredOutputParser
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import io
import os
from huggingface_hub import login

# Hugging Face login (replace with your token or set as env var)
os.environ['HF_TOKEN'] = 'your_huggingface_token_here'  # Set this securely
login(token=os.environ.get('HF_TOKEN'))

# Load model and tokenizer
model_name = "mistralai/Mistral-Nemo-Instruct-2407"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Define schemas
full_name_schema = ResponseSchema(name="full_name", description="The full name of the candidate")
email_schema = ResponseSchema(name="email", description="The email address of the candidate")
education_schema = ResponseSchema(name="education", description="List of education entries, each with degree, institution, and year")
skills_schema = ResponseSchema(name="skills", description="List of skills possessed by the candidate")
experience_schema = ResponseSchema(name="experience", description="List of work experience entries, each with role, company, and years")

response_schemas = [full_name_schema, email_schema, education_schema, skills_schema, experience_schema]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

# CV parsing template
cv_parsing_template = """
You are an HR assistant. Extract ONLY the following information from the CV:

- Full name
- Email
- Education history (degree, institution, year)
- Skills
- Work experience (role, company, years)

Return the answer ONLY as a valid JSON object, no extra text, no explanation. 

The JSON MUST match exactly this format:
{format_instructions}

CV Text:
{cv_text}
"""

def generate_text(prompt, max_length=1500, num_return_sequences=1):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
    )
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

def extract_text_from_pdf(file_content: bytes) -> str:
    try:
        # Use io.BytesIO to handle uploaded file bytes
        loader = PyPDFLoader(io.BytesIO(file_content))
        documents = loader.load()
        full_text = "\n".join([doc.page_content for doc in documents])
        return full_text
    except Exception as e:
        raise ValueError(f"Error loading PDF: {str(e)}")

def extract_json_block(text: str) -> str:
    pattern = r'```json\s*(.*?)\s*```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        return f"```json\n{matches[-1]}\n```"
    raise ValueError("No JSON block found in response")

def parse_cv_content(cv_text: str):
    prompt = PromptTemplate(
        template=cv_parsing_template,
        input_variables=["cv_text", "format_instructions"]
    ).format(cv_text=cv_text, format_instructions=format_instructions)
    
    response = generate_text(prompt)[0]
    json_text = extract_json_block(response)
    try:
        output_data = output_parser.parse(json_text)
        return output_data
    except Exception as e:
        raise ValueError(f"Error parsing output: {str(e)}")
