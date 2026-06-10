def load_skills(path):

    with open(path, "r") as file:

        skills = [
            line.strip().lower()
            for line in file
        ]

    return skills


def extract_skills(text, skills_db):

    text = text.lower()

    found = []

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return found


def extract_job_skills(jd, skills_db):

    jd = jd.lower()

    found = []

    for skill in skills_db:

        if skill in jd:
            found.append(skill)

    return found