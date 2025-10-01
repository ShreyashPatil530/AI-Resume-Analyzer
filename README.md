# 🎯 AI-Powered Resume Analyzer

An intelligent web application that analyzes resumes, extracts skills, and compares them with job descriptions using Natural Language Processing and Machine Learning.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 📄 **Resume Parsing**: Supports PDF and DOCX formats
- 🔍 **Skill Extraction**: Automatically identifies technical skills using NLP
- 🎯 **Job Matching**: Compares resume with job descriptions using TF-IDF and cosine similarity
- 📊 **Match Score**: Provides percentage match between resume and job requirements
- 💾 **History Tracking**: Stores analysis results in SQLite database
- 🎨 **Modern UI**: Clean, responsive interface with gradient design

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/ShreyashPatil530/AI-Resume-Analyzer
cd ai-resume-analyzer
```

2. **Create virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download spaCy language model**
```bash
python -m spacy download en_core_web_sm
```

5. **Set up environment variables**
```bash
# Create .env file
cp .env.example .env

# Edit .env and add your secret key
```

6. **Run the application**
```bash
python app.py
```

7. **Open your browser**
```
http://localhost:5000
```

## 📁 Project Structure

```
ai-resume-analyzer/
├── app.py                      # Main Flask application
├── resume_parser.py            # Resume text extraction
├── skill_extractor.py          # Skill extraction and matching logic
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── LICENSE                     # License file
├── templates/
│   └── index.html             # HTML template
├── static/
│   └── style.css              # CSS styling
├── uploads/                    # Uploaded resumes (auto-created)
└── resume_analysis.db         # SQLite database (auto-created)
```

## 🔧 Configuration

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here-change-this-in-production
FLASK_ENV=development
MAX_FILE_SIZE=16777216  # 16MB in bytes
```

## 📖 Usage

1. **Upload Resume**: Click "Choose File" and select your PDF or DOCX resume
2. **Add Job Description** (Optional): Paste the job description in the text area
3. **Analyze**: Click "Analyze Resume" button
4. **View Results**:
   - Extracted skills from your resume
   - Match percentage with job description
   - Preview of extracted text

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **NLP**: spaCy (Natural Language Processing)
- **ML**: scikit-learn (TF-IDF vectorization, cosine similarity)
- **PDF Processing**: PyPDF2
- **DOCX Processing**: python-docx
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Jinja2 templating

## 📊 Skill Database

The application recognizes skills in the following categories:

- Programming Languages (Python, Java, JavaScript, C++, etc.)
- Web Frameworks (Django, Flask, React, Angular, etc.)
- Data Science (Machine Learning, TensorFlow, Pandas, etc.)
- Databases (MySQL, MongoDB, PostgreSQL, etc.)
- Cloud Technologies (AWS, Azure, Docker, Kubernetes, etc.)
- Tools & Methodologies (Git, Agile, REST API, etc.)

## 🧪 Testing

Run the import test to verify all dependencies:

```bash
python test_imports.py
```

## 🐛 Known Issues

- Ensure spaCy model is downloaded before first use
- Large resumes (>16MB) will be rejected
- Complex PDF layouts may affect text extraction accuracy

## 🔜 Roadmap

- [ ] User authentication system
- [ ] Export results to PDF
- [ ] Advanced ATS (Applicant Tracking System) score
- [ ] Resume formatting suggestions
- [ ] Skill gap analysis
- [ ] Compare multiple resumes
- [ ] API endpoints for integration
- [ ] Docker containerization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## 👤 Author

**Shreyash Patil**
- GitHub: https://github.com/ShreyashPatil530
- LinkedIn: https://www.linkedin.com/in/shreyash-patil-ba921737b/

## 🙏 Acknowledgments

- spaCy for NLP capabilities
- scikit-learn for ML algorithms
- Flask community for excellent documentation
- All contributors who help improve this project

## 📧 Contact

For questions or feedback, please open an issue or contact [your.email@example.com]

---

⭐ If you find this project helpful, please consider giving it a star!

