# 🚀 Complete Setup Guide for AI Resume Analyzer

## 📋 Prerequisites

Before you begin, ensure you have:
- **Python 3.8+** installed ([Download here](https://www.python.org/downloads/))
- **pip** (Python package manager - comes with Python)
- **Git** (optional, for cloning) ([Download here](https://git-scm.com/))

## 🛠️ Installation Steps

### Step 1: Clone or Download the Project

**Option A: Using Git**
```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```

**Option B: Download ZIP**
1. Download the project ZIP file
2. Extract it to your desired location
3. Open terminal/command prompt in that folder

### Step 2: Create Project Structure

Create the following folder structure:
```
ai-resume-analyzer/
├── app.py
├── resume_parser.py
├── skill_extractor.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── LICENSE
├── templates/
│   ├── index.html
│   ├── history.html
│   ├── 404.html
│   └── 500.html
├── static/
│   └── style.css
└── uploads/  (will be created automatically)
```

### Step 3: Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- PyPDF2 (PDF parsing)
- python-docx (Word document parsing)
- spaCy (Natural Language Processing)
- scikit-learn (Machine Learning)
- python-dotenv (Environment variables)
- And other dependencies

### Step 5: Download spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

This downloads the English language model needed for NLP.

### Step 6: Set Up Environment Variables

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` file and change the secret key:
```env
SECRET_KEY=your-unique-secret-key-here-make-it-random-and-long
FLASK_ENV=development
FLASK_DEBUG=True
```

**Generate a secure secret key:**
```python
# Run this in Python to generate a secure key
import secrets
print(secrets.token_hex(32))
```

### Step 7: Verify Installation

Run the test script:
```bash
python test_imports.py
```

You should see: `All imports successful!`

### Step 8: Run the Application

```bash
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

### Step 9: Access the Application

Open your web browser and go to:
```
http://localhost:5000
```

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed successfully
- [ ] spaCy model downloaded
- [ ] `.env` file created with secret key
- [ ] Test imports successful
- [ ] Application starts without errors
- [ ] Can access http://localhost:5000

## 🐛 Troubleshooting

### Issue: "spacy module not found"
**Solution:**
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

### Issue: "ModuleNotFoundError: No module named 'dotenv'"
**Solution:**
```bash
pip install python-dotenv
```

### Issue: "Permission denied" when creating folders
**Solution:**
- Run terminal as administrator (Windows)
- Use `sudo` on macOS/Linux
- Or create the `uploads` folder manually

### Issue: Port 5000 already in use
**Solution:**
Change port in `.env`:
```env
PORT=5001
```

### Issue: PDF text extraction not working
**Solution:**
- Ensure PDF is not password-protected
- Try a different PDF file
- Check if PyPDF2 is installed: `pip install PyPDF2`

### Issue: Large files failing to upload
**Solution:**
Increase file size limit in `.env`:
```env
MAX_FILE_SIZE=33554432  # 32MB
```

## 🔧 Development Setup

For development with auto-reload:

1. Set environment to development:
```env
FLASK_ENV=development
FLASK_DEBUG=True
```

2. Run with auto-reload:
```bash
python app.py
```

Any code changes will automatically reload the server.

## 📦 Production Deployment

### Using Gunicorn (Recommended for Production)

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Create `requirements-prod.txt`:
```
Flask==2.3.3
PyPDF2==3.0.1
python-docx==0.8.11
spacy==3.7.2
scikit-learn==1.3.0
python-dotenv==1.0.0
gunicorn==21.2.0
```

3. Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Environment Variables for Production

Update `.env` for production:
```env
SECRET_KEY=your-very-secure-production-key
FLASK_ENV=production
FLASK_DEBUG=False
```

## 🐳 Docker Setup (Optional)

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .

ENV FLASK_ENV=production

EXPOSE 5000

CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t resume-analyzer .
docker run -p 5000:5000 resume-analyzer
```

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [spaCy Documentation](https://spacy.io/usage)
- [scikit-learn Documentation](https://scikit-learn.org/)

## 💡 Tips

1. Always activate virtual environment before working
2. Keep dependencies updated: `pip list --outdated`
3. Use `.gitignore` to avoid committing sensitive files
4. Regularly backup your database
5. Monitor logs in `app.log` file

## 🆘 Getting Help

If you encounter issues:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review error messages in `app.log`
3. Open an issue on GitHub
4. Check if all dependencies are installed correctly

---

**Happy Coding! 🚀**