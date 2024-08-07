"""
Utilities
"""

from dataclasses import dataclass
import requests


@dataclass
class ProgrammimgLanguage:
    """A programming language."""

    monaco_id: str
    judge0_id: int


class LanguageLabels:
    """Language labels as seen by users."""

    Python = "Python"
    JavaScript = "JavaScript"
    Java = "Java"
    CPP = "C++"
    HTML_CSS = "HTML/CSS"


# supported programming languages and their IDs in judge0 and monaco
# https://ce.judge0.com/#statuses-and-languages-active-and-archived-languages
SUPPORTED_LANGUAGE_MAP = {
    LanguageLabels.Python: ProgrammimgLanguage(
        monaco_id="python", judge0_id=92
    ),  # Python (3.11.2)
    LanguageLabels.JavaScript: ProgrammimgLanguage(
        monaco_id="javascript", judge0_id=93
    ),  # JavaScript (Node.js 18.15.0)
    LanguageLabels.Java: ProgrammimgLanguage(
        monaco_id="java", judge0_id=91
    ),  # Java (JDK 17.0.6)
    LanguageLabels.CPP: ProgrammimgLanguage(
        monaco_id="cpp", judge0_id=54
    ),  # C++ (GCC 9.2.0)
    # Monaco's HTML support includes CSS support within the 'style' tag.
    LanguageLabels.HTML_CSS: ProgrammimgLanguage(
        monaco_id="html", judge0_id=-1
    ),  # no exec
}


JUDGE0_BASE_CE_URL = "https://judge0-ce.p.rapidapi.com"


def submit_code(api_key: str, code: str, language: str) -> str:
    """
    Submit code to the judge0 API.
    """
    url = f"{JUDGE0_BASE_CE_URL}/submissions?base64_encoded=false&wait=false"
    headers = {"content-type": "application/json", "x-rapidapi-key": api_key}

    data = {
        "source_code": code,
        "language_id": SUPPORTED_LANGUAGE_MAP[language].judge0_id,
    }

    response = requests.post(url, headers=headers, json=data, timeout=10)
    response.raise_for_status()
    result = response.json()
    sub_id = result["token"]

    return sub_id


def get_submission_result(api_key: str, submission_id: str):
    """
    Get result from Judge0 submission.
    """

    url = f"{JUDGE0_BASE_CE_URL}/submissions/{submission_id}?base64_encoded=false&fields=*"
    headers = {"content-type": "application/json", "x-rapidapi-key": api_key}

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    result = response.json()

    return result
