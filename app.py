from flask import Flask, render_template, request
from input_handler import clean_resume, extract_pdf_text
from gemini_handle import call_gemini
from json_handler import process_gemini_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Get uploaded PDF
        pdf_file = request.files.get("resume_pdf")

        # PDF uploaded
        if pdf_file and pdf_file.filename:

            if not pdf_file.filename.lower().endswith(".pdf"):
                return render_template(
                    "template.html",
                    error="Please upload a PDF file only."
                )

            try:
                resume_text = extract_pdf_text(pdf_file)

            except Exception as error:
                print("PDF Error:")
                print(error)

                return render_template(
                    "template.html",
                    error="Could not read the PDF. Please upload a valid PDF."
                )

        # Resume pasted as text
        else:

            resume_text = request.form.get(
                "resume",
                ""
            ).strip()

        # Check resume
        if not resume_text:

            return render_template(
                "template.html",
                error="Please upload your PDF resume or paste your resume."
            )

        # Clean resume
        cleaned_resume = clean_resume(resume_text)

        if len(cleaned_resume) < 50:

            return render_template(
                "template.html",
                error="Resume is too short. Please provide a complete resume."
            )

        print("\nResume loaded successfully!")

        # Send to Gemini
        print("Sending resume to Gemini AI...")

        gemini_response = call_gemini(
            cleaned_resume
        )

        if gemini_response is None:

            return render_template(
                "template.html",
                error="Gemini request failed. Please check your API key."
            )

        print("Gemini response received successfully!")

        # Process JSON
        portfolio_data = process_gemini_response(
            gemini_response
        )

        if portfolio_data is None:

            return render_template(
                "template.html",
                error="Could not process Gemini response."
            )

        print("Portfolio data processed successfully!")

        # Show portfolio
        return render_template(
            "portfolio.html",
            portfolio=portfolio_data
        )

    # Home page
    return render_template("template.html")


if __name__ == "__main__":
    app.run(debug=True)
