import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Predefined skill database
SKILLS_DATABASE = {
    'programming_languages': [
        'python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 'swift', 'kotlin', 'go', 'rust',
        'typescript', 'html', 'css', 'sql', 'r', 'matlab', 'scala', 'perl', 'bash', 'shell'
    ],
    'web_frameworks': [
        'django', 'flask', 'fastapi', 'spring', 'express', 'react', 'angular', 'vue', 'laravel', 'ruby on rails',
        'asp.net', 'jquery', 'bootstrap', 'tailwind', 'sass', 'less'
    ],
    'data_science': [
        'machine learning', 'deep learning', 'natural language processing', 'nlp', 'computer vision',
        'data analysis', 'data visualization', 'statistical modeling', 'predictive modeling',
        'neural networks', 'tensorflow', 'pytorch', 'keras', 'scikit-learn', 'pandas', 'numpy',
        'matplotlib', 'seaborn', 'plotly', 'tableau', 'power bi'
    ],
    'databases': [
        'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite', 'oracle', 'sql server', 'cassandra',
        'elasticsearch', 'dynamodb', 'firebase'
    ],
    'cloud_technologies': [
        'aws', 'azure', 'google cloud', 'docker', 'kubernetes', 'terraform', 'jenkins', 'ci/cd',
        'serverless', 'lambda', 's3', 'ec2', 'rds'
    ],
    'tools_methodologies': [
        'git', 'github', 'gitlab', 'jira', 'agile', 'scrum', 'devops', 'rest api', 'graphql',
        'microservices', 'oauth', 'jwt', 'linux', 'unix'
    ]
}

# Flatten the skills database into a single list
ALL_SKILLS = []
for category in SKILLS_DATABASE.values():
    ALL_SKILLS.extend(category)

# Load spaCy model
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Please download the spaCy English model by running:")
    print("python -m spacy download en_core_web_sm")
    nlp = None

def extract_skills(text):
    """
    Extract skills from resume text using spaCy NER and keyword matching
    
    Args:
        text (str): Resume text
        
    Returns:
        list: List of extracted skills
    """
    if not text:
        return []
    
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    # Find skills using keyword matching
    found_skills = set()
    
    # Direct keyword matching
    for skill in ALL_SKILLS:
        # Use regex for whole word matching
        if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
            found_skills.add(skill.title())
    
    # Use spaCy for additional entity recognition if available
    if nlp:
        doc = nlp(text)
        
        # Extract entities that might be skills (ORG, PRODUCT, etc.)
        for ent in doc.ents:
            if ent.label_ in ['ORG', 'PRODUCT', 'TECH']:
                ent_text_lower = ent.text.lower()
                if any(skill in ent_text_lower for skill in ALL_SKILLS):
                    found_skills.add(ent.text.title())
    
    return sorted(list(found_skills))

def preprocess_text(text):
    """
    Preprocess text for similarity comparison
    
    Args:
        text (str): Input text
        
    Returns:
        str: Preprocessed text
    """
    # Convert to lowercase and remove extra whitespace
    text = text.lower().strip()
    
    # Remove special characters but keep words
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    return text

def compare_with_job_description(resume_text, job_description):
    """
    Compare resume with job description using TF-IDF and cosine similarity
    
    Args:
        resume_text (str): Text from resume
        job_description (str): Job description text
        
    Returns:
        float: Similarity percentage (0-100)
    """
    if not resume_text.strip() or not job_description.strip():
        return 0.0
    
    # Preprocess texts
    processed_resume = preprocess_text(resume_text)
    processed_jd = preprocess_text(job_description)
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
    
    try:
        # Fit and transform the texts
        tfidf_matrix = vectorizer.fit_transform([processed_resume, processed_jd])
        
        # Calculate cosine similarity
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
        
        # Convert to percentage
        similarity_percentage = cosine_sim[0][0] * 100
        
        return min(similarity_percentage, 100)  # Cap at 100%
    
    except Exception as e:
        print(f"Error calculating similarity: {str(e)}")
        return 0.0

def get_missing_skills(resume_skills, job_description):
    """
    Identify skills mentioned in job description but missing in resume
    
    Args:
        resume_skills (list): List of skills from resume
        job_description (str): Job description text
        
    Returns:
        list: List of missing skills
    """
    if not job_description.strip():
        return []
    
    jd_skills = extract_skills(job_description)
    resume_skills_lower = [skill.lower() for skill in resume_skills]
    
    missing_skills = []
    for skill in jd_skills:
        if skill.lower() not in resume_skills_lower:
            missing_skills.append(skill)
    
    return missing_skills