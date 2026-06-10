def calculate_skill_score(
        resume_skills,
        jd_skills):

    matched = len(
        set(resume_skills)
        &
        set(jd_skills)
    )

    return (
        matched /
        len(jd_skills)
    ) * 100


def calculate_experience_score(
        years):

    if years >= 3:
        return 100

    elif years == 2:
        return 75

    elif years == 1:
        return 50

    return 20


def calculate_education_score(
        education):

    if education in [
        "B.Tech",
        "B.E",
        "M.Tech"
    ]:
        return 100

    elif education == "MCA":
        return 90

    return 60


def calculate_final_score(
        skill_score,
        exp_score,
        edu_score):

    return round(

        skill_score * 0.6 +

        exp_score * 0.2 +

        edu_score * 0.2,

        2
    )