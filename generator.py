from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def generate_job_posting(job_description: str):
    prompt = f"""
You are an HR copywriter. Based on the job description below, write a clean and professional job posting.

Include:
- Role summary (3-4 sentences)
- Key responsibilities (bullet points)
- Required qualifications
- Nice to haves
- A short closing line about the team or culture

Keep the tone professional but human. Avoid corporate buzzwords.

--- JOB DESCRIPTION ---
{job_description}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)
