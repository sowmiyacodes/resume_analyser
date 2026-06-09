from parser import extract_text_from_pdf
from scorer import load_skills, extract_skills, get_jd_skills
from matcher import match_resume

# ==========================
# CONFIGURATION
# ==========================

RESUME_PATH = "../data/sample_resume.pdf"

JOB_DESCRIPTION = """
Looking for a Python Developer with experience in
SQL, Flask, Git, HTML, CSS and Machine Learning.
"""

# ==========================
# LOAD SKILLS DATABASE
# ==========================

skills_db = load_skills("../data/skills.txt")

# ==========================
# EXTRACT RESUME TEXT
# ==========================

resume_text = extract_text_from_pdf(RESUME_PATH)

# ==========================
# EXTRACT SKILLS
# ==========================

resume_skills = extract_skills(
    resume_text,
    skills_db
)

jd_skills = get_jd_skills(
    JOB_DESCRIPTION,
    skills_db
)

# ==========================
# FIND MATCHING SKILLS
# ==========================

matched_skills = []

for skill in jd_skills:
    if skill in resume_skills:
        matched_skills.append(skill)

# ==========================
# FIND MISSING SKILLS
# ==========================

missing_skills = []

for skill in jd_skills:
    if skill not in resume_skills:
        missing_skills.append(skill)

# ==========================
# ATS SKILL SCORE
# ==========================

if len(jd_skills) > 0:
    skill_match_score = round(
        (len(matched_skills) / len(jd_skills)) * 100,
        2
    )
else:
    skill_match_score = 0

# ==========================
# COSINE SIMILARITY SCORE
# ==========================

resume_skills_text = " ".join(resume_skills)
jd_skills_text = " ".join(jd_skills)

cosine_score = match_resume(
    resume_skills_text,
    jd_skills_text
)

# ==========================
# PRINT RESULTS
# ==========================

print("\n========== AI RESUME ANALYZER ==========\n")

print("Skills Found:")
for skill in resume_skills:
    print(f"- {skill}")

print("\nJob Skills:")
for skill in jd_skills:
    print(f"- {skill}")

print("\nMatched Skills:")
for skill in matched_skills:
    print(f"- {skill}")

print("\nMissing Skills:")
for skill in missing_skills:
    print(f"- {skill}")

print("\n---------------------------")
print(f"ATS Skill Match Score : {skill_match_score}%")
print(f"Cosine Similarity     : {cosine_score}%")
print("---------------------------")

# ==========================
# FEEDBACK
# ==========================

if skill_match_score >= 85:
    print("\nExcellent Match")
elif skill_match_score >= 70:
    print("\nGood Match")
elif skill_match_score >= 50:
    print("\nAverage Match")
else:
    print("\nNeeds Improvement")

if missing_skills:
    print("\nRecommended Skills To Learn:")
    for skill in missing_skills:
        print(f"- {skill}")