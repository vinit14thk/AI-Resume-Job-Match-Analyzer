import os
import re
import pandas as pd
import matplotlib.pyplot as plt

from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


print("=" * 60)
print("AI RESUME & JOB MATCH ANALYZER")
print("=" * 60)


# ==========================================
# READ RESUME FROM PDF
# ==========================================

pdf_files = [
    file for file in os.listdir(".")
    if file.lower().endswith(".pdf")
]

print("\nAvailable Resume PDFs:")

for i, file in enumerate(pdf_files, start=1):
    print(f"{i}. {file}")

resume_choice = int(
    input("\nEnter the number of the resume PDF: ")
)

resume_file = pdf_files[resume_choice - 1]

reader = PdfReader(resume_file)

resume_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        resume_text += text + "\n"


# ==========================================
# JOB DESCRIPTION
# ==========================================

# ==========================================
# READ JOB DESCRIPTION FROM TEXT FILE
# ==========================================

job_files = [
    file for file in os.listdir(".")
    if file.lower().endswith(".txt")
]

print("\nAvailable Job Description Files:")

for i, file in enumerate(job_files, start=1):
    print(f"{i}. {file}")

job_choice = int(
    input("\nEnter the number of the job description: ")
)

job_file = job_files[job_choice - 1]

with open(job_file, "r", encoding="utf-8") as file:
    job_description = file.read()

# Convert text to lowercase
resume_lower = resume_text.lower()
job_lower = job_description.lower()


# ==========================================
# SKILL ANALYSIS
# ==========================================

required_skills = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "scikit-learn",
    "git",
    "github"
]

preferred_skills = [
    "machine learning",
    "data analysis",
    "business analytics",
    "statistics",
    "data visualization",
    "communication",
    "problem-solving",
    "analytical thinking"
]

skills = required_skills + preferred_skills

matching_skills = []
missing_skills = []

for skill in skills:

    if skill in job_lower:

        if skill in resume_lower:
            matching_skills.append(skill)

        else:
            missing_skills.append(skill)


# ==========================================
# TF-IDF MATCH SCORE
# ==========================================

documents = [
    resume_text,
    job_description
]

vectorizer = TfidfVectorizer(
    stop_words="english"
)

tfidf_matrix = vectorizer.fit_transform(documents)

similarity_score = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:2]
)[0][0]

match_percentage = similarity_score * 100


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\nRESUME ANALYSIS")
print("-" * 40)

print(
    f"Resume-Job Match Score: {match_percentage:.2f}%"
)


print("\nMatching Skills:")

if matching_skills:

    for skill in matching_skills:
        print("✓", skill)

else:
    print("No matching skills detected.")


print("\nMissing Skills:")

if missing_skills:

    for skill in missing_skills:
        print("✗", skill)

else:
    print("No missing skills detected.")


print("\nResume text extracted from PDF successfully!")

print("\nAnalysis completed successfully!")

# ==========================================
# WEIGHTED SKILL MATCH SCORE
# ==========================================

required_job_skills = [
    skill for skill in required_skills
    if skill in job_lower
]

preferred_job_skills = [
    skill for skill in preferred_skills
    if skill in job_lower
]

required_matches = [
    skill for skill in required_job_skills
    if skill in resume_lower
]

preferred_matches = [
    skill for skill in preferred_job_skills
    if skill in resume_lower
]

required_score = (
    len(required_matches) / len(required_job_skills) * 70
    if required_job_skills else 0
)

preferred_score = (
    len(preferred_matches) / len(preferred_job_skills) * 30
    if preferred_job_skills else 0
)

weighted_skill_score = required_score + preferred_score
overall_match_score = (
    weighted_skill_score * 0.70
    + match_percentage * 0.30
)


print("\nWeighted Skill Match Score:")
print(f"{weighted_skill_score:.2f}%")

print("\nOverall Resume–Job Match Score:")
print(f"{overall_match_score:.2f}%")

print("\nRequired Skills:", len(required_job_skills))
print("Required Skills Matched:", len(required_matches))

print("Preferred Skills:", len(preferred_job_skills))
print("Preferred Skills Matched:", len(preferred_matches))

# ==========================================
# RECOMMENDATIONS
# ==========================================

print("\nRecommendations:")
print("-" * 40)

if missing_skills:

    print("Consider improving or adding these skills:")

    for skill in missing_skills:
        print("→", skill)

else:

    print("Your resume covers all identified job skills!")

# ==========================================
# WEIGHTED SKILL MATCH VISUALIZATION
# ==========================================

categories = [
    "Required Matched",
    "Required Missing",
    "Preferred Matched",
    "Preferred Missing"
]

values = [
    len(required_matches),
    len(required_job_skills) - len(required_matches),
    len(preferred_matches),
    len(preferred_job_skills) - len(preferred_matches)
]

plt.figure(figsize=(9, 5))

plt.bar(categories, values)

plt.title("Resume Skill Match Analysis")
plt.xlabel("Skill Category")
plt.ylabel("Number of Skills")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig("skill_match_chart.png")

plt.show()

print("\nSkill match chart updated successfully!")