from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resume(resume_text, job_description):
    texts = [resume_text, job_description]

    vectorizer = CountVectorizer()

    matrix = vectorizer.fit_transform(texts)

    similarity = cosine_similarity(
        matrix[0],
        matrix[1]
    )[0][0]

    return round(similarity * 100, 2)