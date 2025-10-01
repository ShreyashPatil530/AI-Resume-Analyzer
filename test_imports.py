# test_imports.py
try:
    import flask
    import PyPDF2
    import docx
    import spacy
    import sklearn
    print("All imports successful!")
except ImportError as e:
    print(f"Import error: {e}")