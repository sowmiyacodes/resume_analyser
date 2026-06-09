def load_skills(skill_file):
    with open(skill_file, "r") as file:
        skills = [line.strip().lower() for line in file]

    return skills


def extract_skills(text, skills_db):
    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills


def find_missing_skills(resume_skills, job_description):
    jd = job_description.lower()

    missing = []

    for skill in resume_skills:
        if skill not in jd:
            continue

    return missing


def get_jd_skills(job_description, skills_db):
    job_description = job_description.lower()

    jd_skills = []

    for skill in skills_db:
        if skill in job_description:
            jd_skills.append(skill)

    return jd_skills