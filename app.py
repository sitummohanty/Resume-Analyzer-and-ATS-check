"""
=== DEVELOPMENT HISTORY ===

Created by:  Situm Mohanty
Date:        August 31, 2025
Description: ATS Resume Tracker - A Streamlit App for Resume Analysis using Google's Gemini AI
             This app helps job seekers analyze their resumes against job descriptions using AI.
             It provides feedback on resume alignment, improvement suggestions, and ATS matching scores.

Development Timeline:

1. Initial Setup
   - Created virtual environment (.venv)
   - Set up requirements.txt with necessary packages
   - Configured Python environment for the project
   - Need to do brew install poppler, in mac os/windows os at system level
   - this code will work in Python 3.12 and above

2. Package Installation & Configuration
   - Installed streamlit, google-generativeai, python-dotenv, pdf2image, Pillow
   - Resolved pdf2image dependency issues (required Poppler installation)
   - Fixed virtual environment activation and package visibility issues

3. Core Functionality Development
   - Built PDF to image conversion function (input_pdf_setup)
   - Implemented Gemini AI integration (get_gemini_response)
   - Created Streamlit interface with file upload and text input
   - Added three analysis types: Resume Analysis, Improvement Suggestions, ATS Matching

4. Bug Fixes & Improvements
   - Fixed "Document stream is empty" error by reading PDF file only once
   - Updated Gemini model from "gemini-pro-vision" to "gemini-1.5-flash"
   - Resolved duplicate element key errors in Streamlit
   - Added comprehensive comments for beginner understanding

5. Code Organization
   - Structured code with clear section headers
   - Added detailed function documentation
   - Implemented error handling for file uploads
   - Created clean, readable code with educational comments

Current Features:
- PDF resume upload and processing
- Job description input
- Three types of AI-powered analysis
- Error handling and user feedback
- Beginner-friendly code documentation

"""

# ===== IMPORT REQUIRED LIBRARIES =====
from dotenv import load_dotenv  # For loading environment variables from .env file

load_dotenv()  # Load environment variables (like API keys)

import streamlit as st  # For creating the web app interface

import os  # For accessing environment variables

from PIL import Image  # For image processing

import pdf2image  # For converting PDF pages to images

import google.generativeai as genai  # Google's Generative AI library

import io  # For handling byte streams

import base64  # For encoding image data

# ===== CONFIGURE GOOGLE GENERATIVE AI =====
# Get the API key from environment variables and configure the AI service
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ===== FUNCTION DEFINITIONS =====

def get_gemini_response(input_text, pdf_content, prompt):
    """
    Send a request to Google's Gemini AI model with text and image inputs.
    
    Args:
        input_text: The job description text from user
        pdf_content: The processed PDF resume as image data (list of pages)
        prompt: The specific instruction for the AI model
    
    Returns:
        AI-generated response as text
    """
    # Create a Gemini model instance that can handle both text and images
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Prepare content list with job description, prompt, and all PDF pages
    content_list = [prompt, input_text]
    content_list.extend(pdf_content)  # Add all pages to the content
    
    # Send the request with job description, all resume pages, and specific prompt
    response = model.generate_content(content_list) 
    
    # Return the text response from the AI
    return response.text

def input_pdf_setup(uploaded_file):
    """
    Convert an uploaded PDF file to image format for AI processing.
    
    Args:
        uploaded_file: The PDF file uploaded by the user
    
    Returns:
        A list containing the first page of PDF as base64-encoded image data
    """
    if uploaded_file is not None:
        # Read the uploaded file as bytes (only read once to avoid empty stream)
        file_bytes = uploaded_file.read()
        
        # Convert PDF pages to images using pdf2image library
        pdf_images = pdf2image.convert_from_bytes(file_bytes)
        
        # Process all pages of the PDF
        pdf_parts = []
        
        for i, page in enumerate(pdf_images):
            # Create an in-memory byte stream to store each page image
            image_byte_arr = io.BytesIO()
            
            # Save each page as PNG image to the byte stream
            page.save(image_byte_arr, format='PNG')
            
            # Get the actual byte data from the stream
            image_byte_arr = image_byte_arr.getvalue()

            # Prepare each page's image data in the format expected by Gemini AI
            page_data = {
                "mime_type": "image/jpeg",  # Specify the image format
                "data": base64.b64encode(image_byte_arr).decode()  # Encode image as base64 string
            }
            pdf_parts.append(page_data)

        return pdf_parts
    else:
        # Raise an error if no file was uploaded
        raise ValueError("No file uploaded")

# ===== STREAMLIT APP INTERFACE =====

# Configure the web page settings
st.set_page_config(page_title="Gemini - ATS Resume Tracker", page_icon="🤖")

# Display the main header
st.header("Resume Analyzer & ATS Tracker 🤖")

# Create a text area for job description input
input_text = st.text_area("Job description", key="job_description")

# Create a file uploader widget for PDF resumes
uploaded_file = st.file_uploader("Upload a Resume in PDF format", type=["pdf"])

# ===== PROCESS UPLOADED RESUME =====
pdf_content = None  # Initialize variable to store processed PDF data

# If a file is uploaded, process it immediately
if uploaded_file is not None:
    st.write("PDF uploaded successfully!")  # Show success message
    pdf_content = input_pdf_setup(uploaded_file)  # Convert PDF to AI-readable format

# ===== CREATE INTERFACE BUTTONS =====
submit_1 = st.button("Tell me about resume")  # Button for general resume analysis
submit_2 = st.button("How can I improve my resume?")  # Button for improvement suggestions
submit_3 = st.button("ATS percentage match")  # Button for ATS score calculation

# ===== AI PROMPTS FOR DIFFERENT ANALYSIS TYPES =====

# Prompt for general resume analysis
input_prompt_1 = """
You are an expert technical recruiter specializing in Full Stack Development, AI/ML, Data Engineering, DevOps, and Data Analyst roles.
Please review the candidate's resume against the provided job description. Give detailed, constructive feedback on: 
1. How well the candidate's profile aligns with the job requirements.
2. Relevant strengths and skills
3. If candidate is not suitable for the job description, then in which role he will fit.
"""

# Prompt for improvement suggestions
input_prompt_2 = """
You are an expert technical recruiter specializing in Full Stack Development, AI/ML, Data Engineering, DevOps, and Data Analyst roles.
Please review the candidate's resume against the provided job description. Give detailed, constructive feedback on: 
1. Gaps or areas for improvement.
2. Suggestions to better tailor the resume for this role.
"""

# Prompt for ATS percentage matching
input_prompt_3 = """
You are an skilled Applicant Tracking System (ATS) evaluator with a deep understanding of recruitment processes in Full Stack Development, 
AI/ML, Data Engineering, DevOps, Data Analyst roles and ATS functionality. Analyze the following candidate resume and job description. 
Calculate and provide an estimated percentage match between the resume and the job description, based on skills, work experience, and 
relevant keywords. Briefly explain the main factors that influenced the match score.
"""

# ===== HANDLE BUTTON CLICKS AND DISPLAY RESULTS =====

# Handle "Tell me about resume" button click
if submit_1:
    if uploaded_file is not None and pdf_content is not None:
        # Get AI response using the general analysis prompt
        response = get_gemini_response(input_prompt_1, pdf_content, input_text)
        st.subheader("Resume Analysis:")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Handle "How can I improve my resume?" button click
elif submit_2:
    if uploaded_file is not None and pdf_content is not None:
        # Get AI response using the improvement suggestions prompt
        response = get_gemini_response(input_prompt_2, pdf_content, input_text)
        st.subheader("Improvement Suggestions:")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Handle "ATS percentage match" button click
elif submit_3:
    if uploaded_file is not None and pdf_content is not None:
        # Get AI response using the ATS matching prompt
        response = get_gemini_response(input_prompt_3, pdf_content, input_text)
        st.subheader("ATS Match Score:")
        st.write(response)
    else:
        st.write("Please upload the resume")
