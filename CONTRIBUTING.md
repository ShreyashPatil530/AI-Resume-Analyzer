# Contributing to AI Resume Analyzer

First off, thank you for considering contributing to AI Resume Analyzer! 🎉

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Screenshots** if applicable
- **Environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Detailed explanation** of the proposed feature
- **Examples** of how it would work
- **Why this enhancement would be useful**

### Pull Requests

1. **Fork the repository**
2. **Create a branch** (`git checkout -b feature/AmazingFeature`)
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
6. **Push to the branch** (`git push origin feature/AmazingFeature`)
7. **Open a Pull Request**

## 📝 Code Style Guidelines

### Python Code Style

- Follow **PEP 8** style guide
- Use **4 spaces** for indentation
- Maximum line length: **88 characters** (Black formatter)
- Use **meaningful variable names**
- Add **docstrings** to all functions

Example:
```python
def extract_skills(text):
    """
    Extract skills from resume text using spaCy NER and keyword matching
    
    Args:
        text (str): Resume text
        
    Returns:
        list: List of extracted skills
    """
    # Your code here
    pass
```

### HTML/CSS Style

- Use **semantic HTML5** elements
- **Indent with 4 spaces**
- Keep CSS **organized and commented**
- Use **meaningful class names**

### Git Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests

Examples:
```
Add skill recommendation feature
Fix PDF parsing for complex layouts
Update README with new installation steps
```

## 🧪 Testing

Before submitting a PR:

1. **Test your changes** thoroughly
2. **Run existing tests** (if available)
3. **Add new tests** for new features
4. **Check for Python errors**: `python test_imports.py`
5. **Test on different file types** (PDF and DOCX)

## 📋 Project Structure

```
ai-resume-analyzer/
├── app.py                 # Main Flask application
├── resume_parser.py       # Resume text extraction
├── skill_extractor.py     # Skill extraction logic
├── config.py              # Configuration management
├── templates/             # HTML templates
├── static/                # CSS, JS, images
└── tests/                 # Test files (if added)
```

## 🎯 Areas for Contribution

### High Priority
- [ ] Unit tests and integration tests
- [ ] API documentation
- [ ] Performance optimization
- [ ] Security improvements
- [ ] Error handling enhancements

### Medium Priority
- [ ] User authentication system
- [ ] Export results to PDF
- [ ] Advanced analytics dashboard
- [ ] Resume comparison feature
- [ ] Skill recommendations

### Nice to Have
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Internationalization (i18n)
- [ ] Dark mode theme
- [ ] Mobile app version

## 🔍 Review Process

1. Maintainers will review your PR
2. May request changes or improvements
3. Once approved, PR will be merged
4. Your contribution will be acknowledged

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

Feel free to open an issue with the tag `question` or reach out to the maintainers.

## 🙏 Thank You!

Every contribution helps make this project better. Thank you for your time and effort!

---

**Happy Contributing! 🚀**