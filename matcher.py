from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def match_resume(resume: str, job_description: str):
    prompt = f"""
You are a hiring assistant. Compare the resume below against the job description and return:

1. A match score from 0 to 100
2. A short summary of why (2-3 sentences max)
3. Skills or keywords the resume is missing
4. Strengths that align well with the role

Be direct. No fluff.

--- RESUME ---
{resume}

--- JOB DESCRIPTION ---
{job_description}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)
