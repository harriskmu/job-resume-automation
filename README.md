# Job Resume Automation

A Python tool that compares a resume against a job description and returns a match score, gap analysis, and a generated job posting — all in one run.

Built this because I got tired of manually reading through JDs and guessing how well a resume fits. Now I just run the script.

---

## What it does

- Scores how well a resume matches a job description (0–100)
- Lists skills and keywords the resume is missing
- Flags strengths that align well with the role
- Generates a clean, professional job posting based on the role input

---

## Setup

1. Clone the repo
2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key to a `.env` file
OPENAI_API_KEY=your_key_here

4. Run it

```bash
python main.py
```

---

## File structure
job-resume-automation/
├── main.py
├── matcher.py
├── generator.py
├── sample_resume.txt
├── sample_jd.txt
├── requirements.txt
└── .env.example

---

## Notes

- Works best with plain text resumes and job descriptions
- Designed for internal HR workflows but works for personal use too
- GPT-4o recommended for best results, but gpt-3.5-turbo works fine

---

## Requirements

- Python 3.9+
- OpenAI API key
