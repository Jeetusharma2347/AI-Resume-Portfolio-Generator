import json
import re


REQUIRED_FIELDS = [
    "name",
    "headline",
    "professional_summary",
    "skills",
    "education",
    "experience",
    "projects",
    "achievements",
    "contact",
    "links"
]


def clean_gemini_response(response_text):

    if not response_text:
        return None

    response_text = response_text.strip()

    response_text = re.sub(
        r"^```json\s*",
        "",
        response_text,
        flags=re.IGNORECASE
    )

    response_text = re.sub(
        r"^```\s*",
        "",
        response_text
    )

    response_text = re.sub(
        r"\s*```$",
        "",
        response_text
    )

    return response_text.strip()


def parse_gemini_json(response_text):

    try:

        cleaned_response = clean_gemini_response(
            response_text
        )

        if not cleaned_response:
            print("ERROR: Gemini response is empty.")
            return None

        portfolio_data = json.loads(
            cleaned_response
        )

        return portfolio_data

    except json.JSONDecodeError as error:

        print(
            "ERROR: Invalid JSON received from Gemini."
        )

        print(error)

        return None


def validate_portfolio_data(data):

    if not isinstance(data, dict):

        print(
            "ERROR: Portfolio data must be a JSON object."
        )

        return False

    for field in REQUIRED_FIELDS:

        if field not in data:

            print(
                f"ERROR: Missing field: {field}"
            )

            return False

    if not isinstance(
        data["skills"],
        list
    ):
        return False

    if not isinstance(
        data["education"],
        list
    ):
        return False

    if not isinstance(
        data["experience"],
        list
    ):
        return False

    if not isinstance(
        data["projects"],
        list
    ):
        return False

    if not isinstance(
        data["achievements"],
        list
    ):
        return False

    if not isinstance(
        data["contact"],
        dict
    ):
        return False

    if not isinstance(
        data["links"],
        dict
    ):
        return False

    return True


def process_gemini_response(response_text):

    portfolio_data = parse_gemini_json(
        response_text
    )

    if portfolio_data is None:
        return None

    if not validate_portfolio_data(
        portfolio_data
    ):
        return None

    return portfolio_data
