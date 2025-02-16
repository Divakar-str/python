import os
import re
import fitz 
import mammoth
import pandas as pd

pattern = re.compile(r'\+91[\s]?\d{5}[\s]?\d{5}')


def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file_path):
        with open(file_path, "rb") as docx_file:
            result = mammoth.extract_raw_text(docx_file)
            return result.value 


def extract_text_from_csv(file_path):
    df = pd.read_csv(file_path)
    return " ".join(df.astype(str).values.flatten())

def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def extract_matches(text):
    return pattern.findall(text)

folder_path = "data"

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if file_name.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_name.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    elif file_name.endswith(".csv"):
        text = extract_text_from_csv(file_path)
    elif file_name.endswith(".txt"):
        text = extract_text_from_txt(file_path)
    else:
        continue

    matches = extract_matches(text)

    if matches:
        print(f"Matches in {file_name}: {matches}")
