import re
import os
import tempfile
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

import streamlit as st
import matplotlib.pyplot as plt
from pypdf import PdfReader

from skill_matcher import skill_is_present, find_skill_match


st.set_page_config(
    page_title="AI Resume & Job Match Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume & Job Match Analyzer")
st.write(
    "Compare a resume with a job description, "
    "review skill gaps, and explore match scores."
)

st.info(
    "This tool uses rule-based skill matching and text overlap. "
    "Its scores are estimates, not predictions of hiring outcomes."
)

resume_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste the job description",
    height=220
)

analyze_button = st.button(
    "Analyze Resume",
    type="primary",
    use_container_width=True
)


def extract_resume_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    pages = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)

    return "\n".join(pages)


def load_skills():
    required = []
    preferred = []
    section = None

    with open("skills.txt", "r", encoding="utf-8") as file:
        for line in file:
            skill = line.strip()

            if not skill:
                continue

            if skill.upper() == "REQUIRED":
                section = "required"
                continue

            if skill.upper() == "PREFERRED":
                section = "preferred"
                continue

            if section == "required":
                required.append(skill.lower())
            elif section == "preferred":
                preferred.append(skill.lower())

    return required, preferred

def create_pdf_report(
    overall_score,
    skill_score,
    text_score,
    match_level,
    recommendation,
    matching_skills,
    missing_skills,
    skill_gap_priority
):
    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    styles = getSampleStyleSheet()
    story = []

    story.append(
        Paragraph(
            "AI Resume &amp; Job Match Analyzer",
            styles["Title"]
        )
    )
    story.append(Spacer(1, 16))

    story.append(
        Paragraph("Analysis Summary", styles["Heading2"])
    )

    summary_data = [
        ["Metric", "Result"],
        ["Overall Match", f"{overall_score:.2f}%"],
        ["Weighted Skill Match", f"{skill_score:.2f}%"],
        ["Text Overlap Similarity", f"{text_score:.2f}%"],
        ["Match Level", match_level],
        ["Recommendation", recommendation]
    ]

    summary_table = Table(summary_data, colWidths=[200, 280])
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP")
    ]))

    story.append(summary_table)
    story.append(Spacer(1, 18))

    story.append(
        Paragraph("Matching Skills", styles["Heading2"])
    )

    if matching_skills:
        for skill in matching_skills:
            story.append(Paragraph(f"- {skill}", styles["Normal"]))
    else:
        story.append(
            Paragraph("No matching skills detected.", styles["Normal"])
        )

    story.append(Spacer(1, 12))
    story.append(
        Paragraph("Missing Skills", styles["Heading2"])
    )

    if missing_skills:
        for skill in missing_skills:
            story.append(Paragraph(f"- {skill}", styles["Normal"]))
    else:
        story.append(
            Paragraph("No missing skills identified.", styles["Normal"])
        )

    story.append(Spacer(1, 12))
    story.append(
        Paragraph("Skill Gap Priorities", styles["Heading2"])
    )

    if skill_gap_priority:
        for skill, priority in skill_gap_priority:
            story.append(
                Paragraph(
                    f"{priority}: {skill}",
                    styles["Normal"]
                )
            )
    else:
        story.append(
            Paragraph("No skill gaps identified.", styles["Normal"])
        )

    document.build(story)
    buffer.seek(0)

    return buffer.getvalue()

if analyze_button:
    if resume_file is None:
        st.error("Please upload a resume PDF.")

    elif not job_description.strip():
        st.error("Please enter a job description.")

    else:
        try:
            resume_text = extract_resume_text(resume_file)

            if not resume_text.strip():
                st.error(
                    "No readable text was found in this PDF. "
                    "Scanned PDFs may need OCR."
                )
                st.stop()

            resume_lower = resume_text.lower()
            job_lower = job_description.lower()

            required_skills, preferred_skills = load_skills()

            all_skills = required_skills + preferred_skills

            job_skills = [
                skill for skill in all_skills
                if skill_is_present(skill, job_lower)
            ]

            matching_skills = [
                skill for skill in job_skills
                if skill_is_present(skill, resume_lower)
            ]

            missing_skills = [
                skill for skill in job_skills
                if not skill_is_present(skill, resume_lower)
            ]

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

            stop_words = {
                "the", "and", "for", "with", "that", "this", "from",
                "are", "you", "your", "our", "will", "have", "has",
                "was", "were", "into", "about", "job", "role", "work",
                "experience", "skills", "skill", "candidate", "required",
                "preferred"
            }

            resume_words = set(
                re.findall(r"\b[a-zA-Z0-9+#.]+\b", resume_lower)
            )
            job_words = set(
                re.findall(r"\b[a-zA-Z0-9+#.]+\b", job_lower)
            )

            resume_words -= stop_words
            job_words -= stop_words

            text_overlap_score = (
                len(resume_words & job_words) / len(job_words) * 100
                if job_words else 0
            )

            skill_component = weighted_skill_score * 0.70
            similarity_component = text_overlap_score * 0.30

            overall_match_score = (
                skill_component + similarity_component
            )

            if overall_match_score >= 80:
                match_level = "Excellent Match"
                recommendation = "Strong Fit - Apply"
            elif overall_match_score >= 60:
                match_level = "Good Match"
                recommendation = (
                    "Good Fit - Apply after improving missing skills"
                )
            elif overall_match_score >= 40:
                match_level = "Moderate Match"
                recommendation = (
                    "Moderate Fit - Consider improving skills first"
                )
            else:
                match_level = "Low Match"
                recommendation = "Low Fit - Significant skill gaps"

            priority_order = {
                "HIGH": 1,
                "MEDIUM": 2,
                "LOW": 3
            }

            skill_gap_priority = []

            for skill in missing_skills:
                if skill in required_job_skills:
                    priority = "HIGH"
                elif skill in preferred_job_skills:
                    priority = "MEDIUM"
                else:
                    priority = "LOW"

                skill_gap_priority.append((skill, priority))

            skill_gap_priority.sort(
                key=lambda item: priority_order[item[1]]
            )

            st.divider()
            st.header("Analysis Results")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Overall Match",
                f"{overall_match_score:.2f}%"
            )
            col2.metric(
                "Weighted Skill Match",
                f"{weighted_skill_score:.2f}%"
            )
            col3.metric(
                "Text Overlap Similarity",
                f"{text_overlap_score:.2f}%"
            )

            st.subheader(match_level)
            st.write(f"*Recommendation:* {recommendation}")

            st.subheader("Matching Skills")

            if matching_skills:
                for skill in matching_skills:
                    phrase = find_skill_match(skill, resume_lower)
                    st.write(
                        f"✓ *{skill}* — matched phrase: "
                        f"{phrase}"
                    )
            else:
                st.write("No matching skills detected.")

            st.subheader("Missing Skills")

            if missing_skills:
                for skill in missing_skills:
                    st.write(f"✗ {skill}")
            else:
                st.success("All identified job skills were matched.")

            st.subheader("Skill Gap Priorities")

            if skill_gap_priority:
                for skill, priority in skill_gap_priority:
                    st.write(f"*{priority}:* {skill}")
            else:
                st.write("No skill gaps identified.")

            st.subheader("Score Breakdown")

            st.write(
                f"Skill match contribution (70%): "
                f"{skill_component:.2f}%"
            )
            st.write(
                f"Text overlap contribution (30%): "
                f"{similarity_component:.2f}%"
            )

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

            fig, ax = plt.subplots(figsize=(9, 5))
            ax.bar(categories, values)
            ax.set_title("Resume Skill Match Analysis")
            ax.set_ylabel("Number of Skills")
            ax.tick_params(axis="x", rotation=15)
            fig.tight_layout()

            st.pyplot(fig)
            plt.close(fig)

            st.caption(
                "The score depends on the skills configured in "
                "skills.txt and the text extracted from the resume."
            )

            pdf_report = create_pdf_report(
                overall_match_score,
                weighted_skill_score,
                text_overlap_score,
                match_level,
                recommendation,
                matching_skills,
                missing_skills,
                skill_gap_priority
            )

            st.download_button(
                label="Download Analysis Report (PDF)",
                data=pdf_report,
                file_name="resume_analysis_report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        except Exception as error:
            st.error(
                "Analysis failed. Check that skills.txt exists and "
                "that the uploaded PDF is readable."
            )
            st.exception(error)