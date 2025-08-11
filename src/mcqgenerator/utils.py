import os
from PyPDF2 import PdfReader
import json
import traceback


def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                # extract_text() can return None if the page has no text layer
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text.strip()

        except Exception as e:
            raise Exception("error reading the PDF file") from e

    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")

    else:
        raise Exception(
            "Unsupported file format — only PDF and text files are supported."
        )

import json
import traceback

import json
import traceback
import re

def get_table_data(quiz_str):
    if not quiz_str or not quiz_str.strip():
        print("⚠️ Quiz string is empty or None")
        return False

    try:
        # Remove triple backticks and optional "json" language tag
        quiz_str = re.sub(r"^```(?:json)?", "", quiz_str.strip(), flags=re.IGNORECASE).strip()
        quiz_str = re.sub(r"```$", "", quiz_str).strip()

        # Convert to dict
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key, value in quiz_dict.items():
            mcq = value.get("mcq", "")
            options = " || ".join(
                f"{option}-> {option_value}"
                for option, option_value in value.get("options", {}).items()
            )
            correct = value.get("correct", "")
            quiz_table_data.append({
                "MCQ": mcq,
                "Choices": options,
                "Correct": correct
            })

        return quiz_table_data

    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON after cleanup: {e}")
        print("Raw cleaned quiz_str:", quiz_str)
        traceback.print_exc()
        return False

    except Exception as e:
        print("❌ Unexpected error in get_table_data:")
        traceback.print_exc()
        return False

