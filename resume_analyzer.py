import os
import re
import pandas as pd
import matplotlib.pyplot as plt

from pypdf import PdfReader
from report_generator import generate_report
from skill_matcher import skill_is_present

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
    and file.lower() != "skills.txt"
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

required_skills = []
preferred_skills = []

current_section = None

with open("skills.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        if line.upper() == "REQUIRED":
            current_section = "required"
            continue

        if line.upper() == "PREFERRED":
            current_section = "preferred"
            continue

        if current_section == "required":
            required_skills.append(line.lower())

        elif current_section == "preferred":
            preferred_skills.append(line.lower())

# ==========================================
# SKILL MATCHING WITH SYNONYMS
# ==========================================

resume_lower = resume_text.lower()
job_lower = job_description.lower()

skills = required_skills + preferred_skills

matching_skills = []
missing_skills = []

for skill in skills:
    if skill_is_present(skill, job_lower):
        if skill_is_present(skill, resume_lower):
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)


# ==========================================
# TEXT OVERLAP MATCH SCORE
# ==========================================

resume_lower = resume_text.lower()
job_lower = job_description.lower()

resume_words = set(re.findall(r"\b[a-zA-Z0-9+#.]+\b", resume_lower))
job_words = set(re.findall(r"\b[a-zA-Z0-9+#.]+\b", job_lower))

stop_words = {
    "the", "and", "for", "with", "that", "this", "from",
    "are", "you", "your", "our", "will", "have", "has",
    "was", "were", "into", "about", "job", "role", "work",
    "experience", "skills", "skill", "candidate", "required",
    "preferred"
}

resume_words -= stop_words
job_words -= stop_words

if job_words:
    match_percentage = (
        len(resume_words & job_words) / len(job_words)
    ) * 100
else:
    match_percentage = 0.0


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
    if skill_is_present(skill, job_lower)
]

preferred_job_skills = [
    skill for skill in preferred_skills
    if skill_is_present(skill, job_lower)
]

required_matches = [
    skill for skill in required_job_skills
    if skill_is_present(skill, resume_lower)
]

preferred_matches = [
    skill for skill in preferred_job_skills
    if skill_is_present(skill, resume_lower)
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
skill_component = weighted_skill_score * 0.70
similarity_component = match_percentage * 0.30
overall_match_score = (
    weighted_skill_score * 0.70
    + match_percentage * 0.30
)


print("\nWeighted Skill Match Score:")
print(f"{weighted_skill_score:.2f}%")

print("\nOverall Resume–Job Match Score:")
print(f"{overall_match_score:.2f}%")

print("\nScore Breakdown:")
print(f"Skill Match Contribution (70%): {skill_component:.2f}%")
print(f"Text Overlap Similarity Contribution (30%): {similarity_component:.2f}%")

if overall_match_score >= 80:
    match_level = "Excellent Match"

elif overall_match_score >= 60:
    match_level = "Good Match"

elif overall_match_score >= 40:
    match_level = "Moderate Match"

else:
    match_level = "Low Match"

if overall_match_score >= 80:
    job_recommendation = "Strong Fit - Apply"

elif overall_match_score >= 60:
    job_recommendation = "Good Fit - Apply after improving missing skills"

elif overall_match_score >= 40:
    job_recommendation = "Moderate Fit - Consider improving skills first"

else:
    job_recommendation = "Low Fit - Significant skill gaps"

skill_gap_priority = []

for skill in missing_skills:

    if skill in required_job_skills:
        priority = "HIGH"

    elif skill in preferred_job_skills:
        priority = "MEDIUM"

    else:
        priority = "LOW"

    skill_gap_priority.append(
        (skill, priority)
    )

priority_order = {
    "HIGH": 1,
    "MEDIUM": 2,
    "LOW": 3
}

skill_gap_priority.sort(
    key=lambda item: priority_order[item[1]]
)


print(f"Match Level: {match_level}")
print(f"Job Recommendation: {job_recommendation}")

print("\nRequired Skills:", len(required_job_skills))
print("Required Skills Matched:", len(required_matches))

print("Preferred Skills:", len(preferred_job_skills))
print("Preferred Skills Matched:", len(preferred_matches))

# ==========================================
# RECOMMENDATIONS
# ==========================================

print("\nSkill Gap Priority:")
print("-" * 40)

for skill, priority in skill_gap_priority:
    print(f"{skill}: {priority}")

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

plt.savefig("skill_match_chart.png", format="png", bbox_inches="tight")

plt.show()

print("\nSkill match chart updated successfully!")

generate_report(
    resume_file=resume_file,
    job_file=job_file,
    tfidf_score=match_percentage,
    weighted_skill_score=weighted_skill_score,
    overall_match_score=overall_match_score,
    skill_component=skill_component,
    similarity_component=similarity_component,
    match_level=match_level,
    job_recommendation=job_recommendation,
    required_job_skills=required_job_skills,
    required_matches=required_matches,
    preferred_job_skills=preferred_job_skills,
    preferred_matches=preferred_matches,
    matching_skills=matching_skills,
    missing_skills=missing_skills,
    skill_gap_priority=skill_gap_priority
)