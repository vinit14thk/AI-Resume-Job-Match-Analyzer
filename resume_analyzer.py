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

reader = PdfReader("resume.pdf")

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

with open("job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

# Convert text to lowercase
resume_lower = resume_text.lower()
job_lower = job_description.lower()


# ==========================================
# SKILL ANALYSIS
# ==========================================

skills = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "data analysis",
    "business analytics",
    "statistics",
    "data visualization",
    "git",
    "github",
    "java",
    "c++",
    "html",
    "communication",
    "problem-solving",
    "analytical thinking"
]


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
# SKILL MATCH SCORE
# ==========================================

required_skills = [
    skill for skill in skills
    if skill in job_lower
]

if required_skills:

    skill_match_score = (
        len(matching_skills) / len(required_skills)
    ) * 100

else:

    skill_match_score = 0


print("\nSkill Match Score:")
print(
    f"{skill_match_score:.2f}%"
)


print("\nTotal Job Skills:", len(required_skills))
print("Matching Skills:", len(matching_skills))
print("Missing Skills:", len(missing_skills))

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
# SKILL MATCH VISUALIZATION
# ==========================================

labels = ["Matching Skills", "Missing Skills"]
values = [len(matching_skills), len(missing_skills)]

plt.figure(figsize=(8, 5))

plt.bar(labels, values)

plt.title("Resume Skill Match Analysis")
plt.xlabel("Skill Category")
plt.ylabel("Number of Skills")

plt.tight_layout()

plt.savefig("skill_match_chart.png")

plt.show()

print("\nSkill match chart saved successfully!")