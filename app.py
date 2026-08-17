from flask import Flask, render_template, request

from input_handler import clean_resume
from gemini_handle import call_gemini
from json_handler import process_gemini_response


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        resume_text = request.form.get("resume", "").strip()

        # Check empty resume
        if not resume_text:
            return render_template(
                "template.html",
                error="Please paste your resume."
            )

        # Clean resume
        cleaned_resume = clean_resume(resume_text)

        # Check resume length
        if len(cleaned_resume) < 50:
            return render_template(
                "template.html",
                error="Resume is too short. Please paste a complete resume."
            )

        print("\nSending resume to Gemini...")

        # Send resume to Gemini
        gemini_response = call_gemini(cleaned_resume)

        if gemini_response is None:
            return render_template(
                "template.html",
                error="Gemini request failed. Please check your API key."
            )

        print("Gemini response received successfully.")

        # Convert Gemini response into JSON
        portfolio_data = process_gemini_response(
            gemini_response
        )

        if portfolio_data is None:
            return render_template(
                "template.html",
                error="Could not process Gemini response."
            )

        print("Portfolio data processed successfully.")

        # Show portfolio
        return render_template(
            "portfolio.html",
            portfolio=portfolio_data
        )

    # GET request
    return render_template("template.html")


if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )