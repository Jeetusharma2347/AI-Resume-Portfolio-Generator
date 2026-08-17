import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


def get_gemini_client():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Please add your API key to .env file."
        )

    return genai.Client(
        api_key=api_key
    )


def create_gemini_prompt(cleaned_resume):

    prompt = f"""
You are an AI assistant that converts a student's resume into
structured portfolio data.

IMPORTANT RULES:

1. Use ONLY information present in the resume.
2. Do NOT invent information.
3. Do NOT invent skills.
4. Do NOT invent projects.
5. Do NOT invent companies.
6. Do NOT invent dates.
7. Do NOT invent education.
8. Do NOT invent experience.
9. Do NOT invent achievements.
10. Do NOT invent email addresses.
11. Do NOT invent phone numbers.
12. Do NOT invent LinkedIn links.
13. Do NOT invent GitHub links.
14. If information is missing, use an empty string or empty array.
15. Return VALID JSON ONLY.
16. Do NOT return Markdown.
17. Do NOT add explanations outside JSON.
18. Keep professional summary concise and factual.

Return EXACTLY this JSON structure:

{{
    "name": "",
    "headline": "",
    "professional_summary": "",
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "achievements": [],
    "contact": {{
        "email": "",
        "phone": ""
    }},
    "links": {{
        "linkedin": "",
        "github": ""
    }}
}}

For education use objects like:

{{
    "degree": "",
    "institution": "",
    "year": ""
}}

For experience use objects like:

{{
    "role": "",
    "company": "",
    "duration": "",
    "description": ""
}}

For projects use objects like:

{{
    "title": "",
    "description": "",
    "technologies": []
}}

RESUME:

{cleaned_resume}
"""

    return prompt


def call_gemini(cleaned_resume):

    try:

        client = get_gemini_client()

        prompt = create_gemini_prompt(
            cleaned_resume
        )

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        if not response.text:
            raise ValueError(
                "Gemini returned an empty response."
            )

        return response.text

    except Exception as error:

        print("\nGemini API Error:")
        print(error)

        return None