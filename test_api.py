import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ API not successful")
    exit()

print("✅ API key successfull")

try:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="Say hello in one sentence."
    )

    print("✅ Gemini API working!")
    print("Response:")
    print(response.text)

except Exception as e:
    print("❌ API request failed")
    print(e)
