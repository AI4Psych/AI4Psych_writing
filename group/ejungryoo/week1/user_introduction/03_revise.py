
import os
import google.generativeai as genai
from openai import OpenAI
from dotenv import load_dotenv

# API 설정
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-exp")

with open("english_translation.txt", "r", encoding="utf-8") as file:
    intro_text = file.read()

role = """You are an academic editor specializing in cognitive neuroscience and psychology."""
# generate two-shot proposal, refering my previous HWs
revise_prompt = f"""
Prompt:
Revise the following English text to make it more natural, fluent, and academically appropriate, while preserving all original meaning and content.

Editing goals:
• Improve flow and coherence between sentences.
• Replace casual or repetitive phrases with concise academic expressions.
• Avoid generic transitions (“In addition”, “Moreover”) unless necessary; vary sentence openings.
• Keep the tone formal, objective, and publication-ready.

Additional stylistic and structural rules:
	1.	Put actions in verbs rather than nouns. For example, prefer using “to regulate” instead of “regulation,” and “to delineate” instead of “delineation.”
	2.	Put characters (agents) in subjects. For example, rather than writing “Identification of features common among primates or unique to humans will require several primate genomes,” prefer “Several primate genomes are needed to identify features common to primates or unique to humans.”
	3.	Keep subjects near verbs. For example, instead of saying “Peanuts, shrimp, almonds, milk or anything else with lactose, and wheat or anything with gluten all represent things that people are commonly allergic to,” prefer “People are commonly allergic to things like peanuts, shrimp, milk, or wheat.”
	4.	Use passive voice judiciously. Favor active voice when it improves clarity and engagement, but retain passive constructions when they enhance objectivity or readability.
	5.	Ensure paragraph cohesion. The first and last sentences of each paragraph should align in theme and tone, forming a coherent logical boundary.
	6.	Use concise academic alternatives in place of verbose or redundant expressions.
	•	Prefer using “whether” instead of “the question as to whether.”
	•	Prefer “doubtless” instead of “there is no doubt but that.”
	•	Prefer “used for fuel” instead of “used for fuel purposes.”
	•	Prefer “carefully” instead of “in a careful manner.”
	•	Prefer “this subject” instead of “this is a subject that.”
	•	Prefer “most” instead of “a large majority of.”
	•	Prefer “can” instead of “has the capacity to.”
	•	Prefer “whether” instead of “whether or not.”
	•	Prefer “agree” instead of “are in agreement.”
	•	Prefer “before” instead of “prior to.”
	•	Prefer “after” instead of “subsequent to.”
	•	Prefer “now” instead of “at this point in time.”
	•	Prefer “because” instead of “due to the fact that.”
	•	Prefer “if” instead of “in the event that.”
	•	Prefer “an initiative” instead of “a new initiative.”
	•	Prefer “unique” or “rare” instead of “nearly unique.”
	•	Prefer “is essential to” instead of “plays a key role in.”
	•	Prefer “the cultures were equally affected” instead of “both cultures were equally affected.”

Input:
{intro_text}

Output:
A revised version that meets all the above criteria and is ready for submission to a top-tier academic journal.
"""

# 실행 및 출력
#revise_response = model.generate_content(revise_prompt)
#print('\n--------Revised Introduction--------\n')
#print(revise_response.text)

#with open("revised_introduction.txt", "w", encoding="utf-8") as f:
#    f.write(revise_response.text)

# Generate Responses
revise_response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": role},
        {"role": "user", "content": revise_prompt}
    ],
    temperature=0.1,   # 최대한 원문에 충실하게 번역
)

with open("revised_introduction.txt", "w", encoding="utf-8") as f:
    f.write(revise_response.choices[0].message.content)