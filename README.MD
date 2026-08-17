# AI-Assisted Resume Portfolio Generator
## About the Project

The AI-Assisted Resume Portfolio Generator is a Python-based project that uses AI to convert resume information into a structured portfolio webpage.

## Technologies Used

- Python
- Gemini API
- JSON
- HTML
- CSS
- GitHub

## Project Workflow

resume.txt → Read and Clean → Gemini AI → JSON → Parse JSON → Build HTML → portfolio.html

## Project Structure

- main.py - Main Python program
- resume.txt - Resume input file
- template.html - HTML template
- style.css - Portfolio styling
- portfolio.html - Generated portfolio
- requirements.txt - Python dependencies
- README.md - Project documentation
- .gitignore - Prevents unwanted files and secrets from being uploaded
- .env.example - Shows required environment variables

## Testing

The project is tested for:

1. Missing resume.txt
2. Empty or very short resume
3. Valid resume
4. Missing resume sections
5. Missing API key
6. API failure
7. Invalid JSON

## Expected Result

For a valid resume, the application should generate a portfolio.html file successfully.

## Safety

API keys and other secret information should not be uploaded to GitHub.

## Team

This project is developed as part of the AIML GLA Bootcamp '26.
