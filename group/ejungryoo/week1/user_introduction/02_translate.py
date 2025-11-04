import os
import google.generativeai as genai
from openai import OpenAI
from dotenv import load_dotenv

# API 설정
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-exp")

with open("reference_list_APA.txt", "r", encoding="utf-8") as file:
    reference_list = file.read()
with open("korean_intro.txt", "r", encoding="utf-8") as file:
    korean_intro = file.read()

role = """You are a professional academic translator specialized in psychology and neuroscience research papers."""
# generate zero-shot proposal 
kor2eng_prompt = f"""
Translate the following Korean text into natural, publication-quality academic English, keeping the original meaning as accurately as possible.
	•	Avoid paraphrasing or over-smoothing expressions; stay close to the source.
	•	Maintain formal academic tone and precise terminology.
	•	Do not omit or add information.
	•	If an English technical term already exists in the literature, use that version.
    •	Use citation placeholders (e.g., (Author, Year)) where necessary. 
    - If numeric citations such as [1], [2], [3] appear in the text, replace each with the corresponding author-year format using the provided reference list.
    - For example, if [1] refers to Smith et al., 2020, then write it as (Smith, 2020) in the text.
    - Ensure that all references mentioned in the text correspond correctly to the given reference list.

Input: {korean_intro}
reference_list: {reference_list}

Output: 
English translation of Introduction section suitable for submission to an academic journal (e.g., Cerebral Cortex, Nature Human Behaviour).
"""

# Generate Responses
kor2eng_response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": role},
        {"role": "user", "content": kor2eng_prompt}
    ],
    temperature=0.2,   # 최대한 원문에 충실하게 번역
)

with open("english_translation.txt", "w", encoding="utf-8") as f:
    f.write(kor2eng_response.choices[0].message.content)