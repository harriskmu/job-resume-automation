from matcher import match_resume
from generator import generate_job_posting

resume_path = "sample_resume.txt"
jd_path = "sample_jd.txt"

with open(resume_path, "r") as f:
    resume = f.read()

with open(jd_path, "r") as f:
    job_description = f.read()

print("\n--- MATCH ANALYSIS ---\n")
match_resume(resume, job_description)

print("\n--- GENERATED JOB POSTING ---\n")
generate_job_posting(job_description)
