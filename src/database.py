import mysql.connector


def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2024506096",
        database="resume_ranker"
    )

    return connection

from database import get_connection


def insert_candidate(candidate):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO candidates
    (
        name,
        education,
        experience,
        score,
        skills,
        ranking
    )
    VALUES(%s,%s,%s,%s,%s,%s)
    """

    values = (
        candidate["name"],
        candidate["education"],
        candidate["experience"],
        candidate["score"],
        ",".join(candidate["skills"]),
        candidate["rank"]
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()