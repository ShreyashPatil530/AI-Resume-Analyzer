from flask import Flask, render_template, request, flash, redirect, url_for
import os
from werkzeug.utils import secure_filename
from resume_parser import extract_resume_text
from skill_extractor import extract_skills, compare_with_job_description
import sqlite3
from datetime import datetime
from config import config
import logging

# Initialize Flask app
app = Flask(__name__)

# Load configuration
env = os.getenv('FLASK_ENV', 'development')
app.config.from_object(config[env])

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def init_db():
    """Initialize SQLite database"""
    try:
        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS analysis_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                skills TEXT,
                job_description TEXT,
                match_percentage REAL,
                analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise

def save_to_db(filename, skills, job_description, match_percentage):
    """Save analysis results to database"""
    try:
        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        c = conn.cursor()
        c.execute('''
            INSERT INTO analysis_results (filename, skills, job_description, match_percentage)
            VALUES (?, ?, ?, ?)
        ''', (filename, ','.join(skills), job_description, match_percentage))
        conn.commit()
        conn.close()
        logger.info(f"Analysis saved for file: {filename}")
    except Exception as e:
        logger.error(f"Error saving to database: {str(e)}")
        raise

def cleanup_old_files():
    """Delete uploaded files after processing"""
    try:
        upload_folder = app.config['UPLOAD_FOLDER']
        if os.path.exists(upload_folder):
            for filename in os.listdir(upload_folder):
                file_path = os.path.join(upload_folder, filename)
                # Delete files older than 1 hour
                if os.path.isfile(file_path):
                    file_age = datetime.now().timestamp() - os.path.getmtime(file_path)
                    if file_age > 3600:  # 1 hour in seconds
                        os.remove(file_path)
                        logger.info(f"Deleted old file: {filename}")
    except Exception as e:
        logger.error(f"Error cleaning up files: {str(e)}")

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main route for resume analysis"""
    if request.method == 'POST':
        # Check if file was uploaded
        if 'resume' not in request.files:
            flash('No file selected', 'error')
            return redirect(request.url)
        
        file = request.files['resume']
        job_description = request.form.get('job_description', '')
        
        if file.filename == '':
            flash('No file selected', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            try:
                # Save uploaded file
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                logger.info(f"File uploaded: {filename}")
                
                # Extract text from resume
                resume_text = extract_resume_text(filepath)
                
                if not resume_text.strip():
                    flash('Could not extract text from the resume. Please check the file format.', 'error')
                    logger.warning(f"No text extracted from: {filename}")
                    return redirect(request.url)
                
                # Extract skills
                skills = extract_skills(resume_text)
                logger.info(f"Extracted {len(skills)} skills from resume")
                
                # Calculate match percentage
                match_percentage = 0
                if job_description.strip():
                    match_percentage = compare_with_job_description(resume_text, job_description)
                    logger.info(f"Match percentage calculated: {match_percentage}%")
                
                # Save to database
                save_to_db(filename, skills, job_description, match_percentage)
                
                # Prepare results for display
                results = {
                    'skills': skills,
                    'match_percentage': round(match_percentage, 2),
                    'resume_text_preview': resume_text[:500] + '...' if len(resume_text) > 500 else resume_text,
                    'filename': filename
                }
                
                # Clean up old files
                cleanup_old_files()
                
                flash('Resume analyzed successfully!', 'success')
                return render_template('index.html', results=results)
                
            except Exception as e:
                logger.error(f"Error processing file: {str(e)}")
                flash(f'Error processing file: {str(e)}', 'error')
                return redirect(request.url)
        else:
            flash('Please upload a PDF or DOCX file only', 'error')
            return redirect(request.url)
    
    return render_template('index.html', results=None)

@app.route('/history')
def history():
    """View analysis history"""
    try:
        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('''
            SELECT id, filename, skills, match_percentage, analysis_date
            FROM analysis_results
            ORDER BY analysis_date DESC
            LIMIT 50
        ''')
        results = c.fetchall()
        conn.close()
        return render_template('history.html', results=results)
    except Exception as e:
        logger.error(f"Error fetching history: {str(e)}")
        flash('Error loading history', 'error')
        return redirect(url_for('index'))

@app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'healthy', 'timestamp': datetime.now().isoformat()}, 200

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    flash('File too large. Maximum size is 16MB', 'error')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal error: {str(error)}")
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Create uploads folder if it doesn't exist
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
        logger.info(f"Created upload folder: {app.config['UPLOAD_FOLDER']}")
    
    # Initialize database
    init_db()
    
    # Run the application
    logger.info(f"Starting application in {env} mode")
    app.run(
        debug=app.config['DEBUG'],
        host=app.config['HOST'],
        port=app.config['PORT']
    )