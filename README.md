# Resume Analyser

A simple Python-based Applicant Tracking System (ATS) prototype that scores and ranks PDF resumes against a job description using keyword matching, education extraction, and experience estimation.

## What it does

- Loads a target job description from `data/job_description.txt`
- Loads a skills dictionary from `data/skills.txt`
- Reads PDF resumes from `data/resumes/`
- Extracts text from each resume using `PyPDF2`
- Identifies matching skills, education level, and experience
- Calculates a final score for each candidate
- Stores ranked candidates in a MySQL database
- Prints candidate rankings to the console

## Project structure

- `src/app.py` - main script that orchestrates resume processing, scoring, ranking, and database insertion
- `src/parser.py` - extracts text from PDF files
- `src/skills.py` - loads skills list and extracts matching skills from text
- `src/experience.py` - extracts years of experience from resume text
- `src/education.py` - extracts education level from resume text
- `src/scorer.py` - computes skill, experience, education, and final scores
- `src/ranker.py` - sorts candidates by score and assigns rank
- `src/database.py` - inserts ranked candidates into MySQL
- `data/` - contains sample job descriptions, skills list, and resumes

## Requirements

- Python 3.x
- `PyPDF2`
- `scikit-learn` (listed in requirements, but not currently used in code)
- MySQL server

Install dependencies with:

```bash
pip install -r requirements.txt
```

## MySQL setup

Create a database and table for candidate results.

Example SQL:

```sql
CREATE DATABASE resume_ranker;
USE resume_ranker;

CREATE TABLE candidates (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  education VARCHAR(100),
  experience INT,
  score DECIMAL(5,2),
  skills TEXT,
  ranking INT
);
```

Update the database credentials in `src/database.py` if needed.

## Usage

Run the application from the project root:

```bash
python src/app.py
```

The script will process each PDF in `data/resumes`, calculate scores, store the results in the MySQL table, and print the ranked candidates.

## Scoring logic

- Skill score: percent of job-description skills found in the resume
- Experience score:
  - 3+ years = 100
  - 2 years = 75
  - 1 year = 50
  - otherwise = 20
- Education score:
  - `B.Tech`, `B.E`, `M.Tech` = 100
  - `MCA` = 90
  - otherwise = 60
- Final score = `0.6 * skill_score + 0.2 * experience_score + 0.2 * education_score`

## Notes

- Resumes must be PDFs in `data/resumes/`
- Job description and skills are matched using simple substring checks
- Education and experience extraction are heuristic-based and may require improvements for production use
- `scikit-learn` is included in `requirements.txt` but not currently leveraged by the application
