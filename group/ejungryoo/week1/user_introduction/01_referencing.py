
import os
import google.generativeai as genai
from dotenv import load_dotenv

# API 설정
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel("gemini-2.0-flash-exp")

with open("reference.txt", "r", encoding="utf-8") as file:
    reference_text = file.read()

reference_prompt = f"""
You are a citation formatting expert specialized in academic writing and reference management.
You have deep expertise in APA 7th edition style and are skilled at converting raw reference text into perfectly formatted references.
Your goal is to convert the given reference information into APA 7th edition format, ensuring consistency, accuracy, and professional formatting suitable for publication in peer-reviewed journals.

Follow these steps precisely:
	1.	Check the reference type (journal article, book, book chapter, conference paper, thesis, or report).
	2.	Apply APA 7th rules for each type:
	•	Journal article: Author(s). (Year). Title of the article. Journal Name, Volume(Issue), page range. https://doi.org/…
	•	Book: Author(s). (Year). Book title. Publisher.
	•	Conference paper: Author(s). (Year). Title of the paper. In Editor(s) (Ed(s).), Conference Title (pp. xx–xx). Publisher.
	3.	Ensure correct order: Author(s), Year, Title, Journal/Publisher, Volume(Issue), Page range, DOI.
	4.	Remove unnecessary metadata such as URLs, retrieval dates, or database names unless required by APA 7th.
	5.	Ensure spacing and punctuation strictly follow APA conventions.

 Constraints
	•	Do not paraphrase or summarize titles.
	•	Do not invent missing information (e.g., DOI) — if unavailable, leave it blank.
	•	If multiple references are given, return them as a numbered list.
	•	Output must be plain text, ready to copy into a reference section.

Input:
{reference_text}

Output:
Formatted reference list in APA 7th edition style.
"""

# Generate Responses
reference_response = model.generate_content(reference_prompt)
print('\n--------APA 7th edition formatted reference list--------\n')
print(reference_response.text)

with open("reference_list_APA.txt", "w", encoding="utf-8") as f:
    f.write(reference_response.text)