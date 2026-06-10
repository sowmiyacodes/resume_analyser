import os

from parser import extract_text_from_pdf

from skills import (
    load_skills,
    extract_skills,
    extract_job_skills
)

from experience import (
    extract_experience
)

from education import (
    extract_education
)

from scorer import *

from ranker import rank_candidates

from database import (
    insert_candidate
)

skills_db = load_skills(
    "../data/skills.txt"
)

with open(
        "../data/job_description.txt",
        "r"
) as file:

    jd = file.read()

jd_skills = extract_job_skills(
    jd,
    skills_db
)

resume_folder = "../data/resumes"

candidates = []

for file in os.listdir(
        resume_folder
):

    if file.endswith(".pdf"):

        path = os.path.join(
            resume_folder,
            file
        )

        text = extract_text_from_pdf(
            path
        )

        skills = extract_skills(
            text,
            skills_db
        )

        experience = extract_experience(
            text
        )

        education = extract_education(
            text
        )

        skill_score = calculate_skill_score(
            skills,
            jd_skills
        )

        exp_score = calculate_experience_score(
            experience
        )

        edu_score = calculate_education_score(
            education
        )

        final_score = calculate_final_score(
            skill_score,
            exp_score,
            edu_score
        )

        candidate = {

            "name":
            file.replace(".pdf", ""),

            "skills":
            skills,

            "education":
            education,

            "experience":
            experience,

            "score":
            final_score

        }

        candidates.append(
            candidate
        )

ranked = rank_candidates(
    candidates
)

for candidate in ranked:

    insert_candidate(
        candidate
    )

print("\n===== ATS RANKINGS =====\n")

for candidate in ranked:

    print(
        f"Rank {candidate['rank']} | "
        f"{candidate['name']} | "
        f"{candidate['score']}%"
    )