# ATS Resume Tracker 🤖

A Streamlit-based web application that uses Google's Gemini AI to analyze resumes against job descriptions, providing insights for ATS (Applicant Tracking System) optimization.

## 📋 Description

This application helps job seekers analyze their resumes against specific job descriptions using AI-powered analysis. It provides three types of feedback:
- Resume analysis and alignment with job requirements
- Improvement suggestions for better job matching
- ATS percentage match scoring

## ✨ Features

- **PDF Resume Upload**: Support for multi-page PDF resumes
- **AI-Powered Analysis**: Uses Google's Gemini 1.5 Flash model
- **Three Analysis Types**:
  - Resume Analysis & Job Alignment
  - Improvement Suggestions
  - ATS Match Score Calculation
- **Multi-Page Support**: Processes complete resumes across all pages
- **User-Friendly Interface**: Clean Streamlit web interface

## 🛠️ Technologies Used

- **Python 3.12+**
- **Streamlit** - Web interface
- **Google Generative AI (Gemini)** - AI analysis
- **pdf2image** - PDF processing
- **Pillow (PIL)** - Image processing
- **python-dotenv** - Environment variable management

## 📦 Installation

### Prerequisites

1. **Python 3.12 or higher**
2. **Poppler** (required for pdf2image):
   - **macOS**: `brew install poppler`
   - **Windows**: Download from [Poppler for Windows](https://blog.alivate.com.au/poppler-windows/)
   - **Linux**: `sudo apt-get install poppler-utils`

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ATS-LLM
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv .venv
   
   # On macOS/Linux:
   source .venv/bin/activate
   
   # On Windows:
   .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. **Get Google API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key for Gemini
   - Add it to your `.env` file

## 🚀 Usage

1. **Start the application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Use the application**:
   - Enter the job description in the text area
   - Upload your resume as a PDF file
   - Choose one of the three analysis options:
     - "Tell me about resume" - General analysis
     - "How can I improve my resume?" - Improvement suggestions
     - "ATS percentage match" - Score calculation

## 📁 Project Structure

```
ATS-LLM/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .venv/             # Virtual environment
└── README.md          # Project documentation
```

## 🔧 Configuration

The application uses the following environment variables:

- `GOOGLE_API_KEY`: Your Google Generative AI API key

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Situm Mohanty**
- Date: August 31, 2025

## 🐛 Troubleshooting

### Common Issues

1. **ModuleNotFoundError: No module named 'pdf2image'**
   - Ensure Poppler is installed on your system
   - Verify virtual environment is activated
   - Reinstall requirements: `pip install -r requirements.txt`

2. **Google API Error**
   - Check your API key is correctly set in `.env`
   - Ensure API key has Gemini access enabled
   - Verify API quota hasn't been exceeded

3. **PDF Processing Error**
   - Ensure PDF is not corrupted
   - Check PDF is not password protected
   - Verify Poppler is properly installed

## 🔮 Future Enhancements

- [ ] Support for Word documents (.docx)
- [ ] Batch processing of multiple resumes
- [ ] Resume template suggestions
- [ ] Export analysis results to PDF
- [ ] Integration with job boards
- [ ] Resume scoring dashboard

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Create an issue in the repository
3. Contact the maintainer

---

**Made with ❤️ using Python and AI by Situm Mohanty**
