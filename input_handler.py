import re
from pypdf import PdfReader


MIN_LENGTH = 50


def clean_resume(text):
    if not text:
        return ""

    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        line = line.strip()
        line = re.sub(r"[ \t]+", " ", line)

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def extract_pdf_text(pdf_file):
    """
    Extract text from uploaded PDF resume.
    """

    reader = PdfReader(pdf_file)
    extracted_text = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            extracted_text.append(text)

    final_text = "\n".join(extracted_text)

    return clean_resume(final_text)


def check_sections(text):
    sections = {
        "Name": False,
        "Headline": False,
        "Education": False,
        "Skills": False,
        "Experience": False,
        "Projects": False,
        "Achievements": False,
        "Contact": False
    }

    lines = text.splitlines()

    for line in lines:
        line = line.strip().lower()

        if line.startswith("name:"):
            sections["Name"] = True

        elif line.startswith("headline:"):
            sections["Headline"] = True

        elif line.startswith("education:"):
            sections["Education"] = True

        elif line.startswith("skills:"):
            sections["Skills"] = True

        elif line.startswith("experience:"):
            sections["Experience"] = True

        elif line.startswith("projects:"):
            sections["Projects"] = True

        elif line.startswith("achievements:"):
            sections["Achievements"] = True

        elif line.startswith("contact:"):
            sections["Contact"] = True

    return sections
